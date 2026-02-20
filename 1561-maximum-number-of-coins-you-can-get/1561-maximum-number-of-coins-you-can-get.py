class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        if len(piles)==3:
            return piles[1]

        me=0
        count=0
        check=int(len(piles))//3
        for i in range(len(piles)):
            if i%2==1:
                me+=piles[i]
                count+=1
            if count==check:
                return me
        
    
            

