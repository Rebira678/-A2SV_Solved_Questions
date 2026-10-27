class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if stack:
                    if dic[stack[-1]]==i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False