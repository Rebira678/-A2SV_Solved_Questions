class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ptr1=0
        ptr2=len(skill)-1
        checker=set()
        ans=0

        while ptr1<ptr2:

            total=skill[ptr1]+skill[ptr2]
            checker.add(total)
            ans+=skill[ptr1]*skill[ptr2]
            if len(checker)!=1:
                return -1
            
            ptr1+=1
            ptr2-=1
        
        return ans
            
        

        