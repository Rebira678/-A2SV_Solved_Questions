class Solution:
    def isHappy(self, n: int) -> bool:
        checkers = set()
        while n!=1 and n not in checkers:
            checkers.add(n)
            str_num=str(n)
            nums=0
            for i in str_num:
                nums+=int(i)*int(i)
            n=nums
        return n==1
        