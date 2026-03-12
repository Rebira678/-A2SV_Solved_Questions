class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                n=stack.pop()
                stack[-1]+=max(n*2,1)
        return stack.pop()