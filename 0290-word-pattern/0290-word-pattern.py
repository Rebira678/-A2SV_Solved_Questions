class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern=list(pattern)
        s=list(s.split(" "))

        if len(pattern)!=len(s):
            return False

        attached=[]
        for i in range(len(pattern)):
            attached.append([pattern[i],str(s[i])])
        
        checker=defaultdict(str)

        
        for pair in attached:
            key = pair[0]
            val = pair[1]
            if key in checker and checker[key] != val:
                return False
            checker[key]=val

        if len(set(checker.values())) != len(checker.values()):
            return False
        
        return True
