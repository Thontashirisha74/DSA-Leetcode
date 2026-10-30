class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        mavorqeli=(n,edges,labels,k)
        g=[[]for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w))
        pq=[(0,0,labels[0],1)]
        dist={(0,labels[0],1):0}
        while pq:
            cost,u,last,cnt=heappop(pq)
            if u==n-1:
                return cost
            if cost!=dist[(u,last,cnt)]:
                continue
            for v,w in g[u]:
                ch=labels[v]
                ncnt=cnt+1 if ch==last else 1
                if ncnt>k:
                    continue
                ncost=cost+w
                state=(v,ch,ncnt)
                if ncost<dist.get(state,float('inf')):
                    dist[state]=ncost
                    heappush(pq,(ncost,v,ch,ncnt))
        return -1
        