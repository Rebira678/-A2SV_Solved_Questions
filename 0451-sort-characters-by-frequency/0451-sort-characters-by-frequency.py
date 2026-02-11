class Solution:
    def frequencySort(self, s: str) -> str:
        s=Counter(s)
        sorted_s=sorted(s.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for i in sorted_s:
            for j in range(i[1]):
                ans+= i[0]
        
        return ans


    