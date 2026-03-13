class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dif_container=[]
        i=0
        for num in costs:
            dif_container.append([num[0]-num[1],i])
            i+=1
        
        dif_container.sort()

        cityA=[]
        cityB=[]
        for i in costs:
            cityA.append(i[0])
            cityB.append(i[1])
        
        total=0
        n=len(costs)
        m=len(costs)//2
        for i in range(n):
            if i<m:
                total+=cityA[dif_container[i][1]]
            else:
                total+=cityB[dif_container[i][1]]
        
        return total
        

        