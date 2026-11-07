class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available=[(w,i) for i,w in enumerate(servers)]
        heapq.heapify(available)
        busy=[]
        ans=[]
        time=0

        for i,d in enumerate(tasks):
            time=max(time,i)
            while busy and busy[0][0]<=time:
                t,w,j=heapq.heappop(busy)
                heapq.heappush(available,(w,j))
            if not available:
                time=busy[0][0]
                while busy and busy[0][0]<=time:
                    t,w,j=heapq.heappop(busy)
                    heapq.heappush(available,(w,j))
            w,j=heapq.heappop(available)
            ans.append(j)
            heapq.heappush(busy,(time+d,w,j))
        return ans