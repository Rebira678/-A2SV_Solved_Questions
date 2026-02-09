#609. Find Duplicate File in System
#https://leetcode.com/problems/find-duplicate-file-in-system/
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for i in paths:
            m=i.split(" ")
            root=m[0]
            for j in range(1,len(m)):
                n= m[j].split("(")
                path=n[0]
                content=n[-1]
                content=content[:-1]
                if content in dic:
                    dic[content].append(root + "/" + path)
                else:
                    dic[content]=[root+"/"+ path]
            
        ans=[]
        for i in dic:
            if len(dic[i])>1:
                ans.append(dic[i])

        return ans
