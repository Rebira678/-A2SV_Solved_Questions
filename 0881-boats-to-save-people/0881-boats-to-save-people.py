class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ptr1=0
        ptr2=len(people)-1
        count = 0
        
        while ptr1 <= ptr2:
            total=people[ptr1] + people[ptr2]
            if total <= limit:
                ptr1 += 1
            ptr2 -= 1
            count += 1
        
        return count
            
        

