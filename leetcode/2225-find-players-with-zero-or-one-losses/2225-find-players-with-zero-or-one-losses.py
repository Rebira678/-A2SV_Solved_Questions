class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners=set()
        loser=defaultdict(int)
        for i in matches:
            winners.add(i[0])
            loser[i[1]]+=1
        
        not_de=[]
        only_one=[]
        for i in loser:
            if loser[i]==1:
                only_one.append(i)
        
        for i in winners:
            if i not in loser:
                not_de.append(i)
        
        not_de.sort()
        only_one.sort()
        return (not_de,only_one)

