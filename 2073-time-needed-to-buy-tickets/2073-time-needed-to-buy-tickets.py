class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        n=len(tickets)
        for i in range(0,n):
            if i<=k:
                time+=min(tickets[i], tickets[k])
            if i > k:
                time+=min(tickets[i], tickets[k]-1)
        return time


        