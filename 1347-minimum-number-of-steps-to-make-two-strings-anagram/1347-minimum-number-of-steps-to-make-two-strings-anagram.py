class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first=list(s)
        second=list(t)

        dic_first=defaultdict(int)
        for i in first:
            dic_first[i]+=1
        
        dic_second=defaultdict(int)
        for i in second:
            dic_second[i]+=1

        count=0
        for i in dic_first:
            if i in dic_second:
                m=dic_first[i]-dic_second[i]
                if m>=0:
                    count+=m
            else:
                count+=dic_first[i]
        return count


        