class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count=0

        hashTable = defaultdict(int)

        for char in arr:
            rem = char %k 
            comp = (k-rem) %k

            if hashTable[comp] >0:
                count+=1
                hashTable[comp]-=1
            else:
                hashTable[rem]+=1
        
        return count==(len(arr)//2)