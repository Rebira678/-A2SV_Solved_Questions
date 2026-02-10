class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        prev_value=0
        for i in reversed(s):
            if dic[i] < prev_value:
                total -= dic[i]
            else:
                total +=dic[i]
                prev_value=dic[i]
        return total

        