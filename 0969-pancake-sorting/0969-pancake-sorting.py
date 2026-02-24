class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            
            # Find index of max element in arr[0:size]
            max_index = arr.index(max(arr[:size]))
            
            if max_index == size - 1:
                continue  # already in correct position
            
            # Step 1: Bring max to front (if not already there)
            if max_index != 0:
                res.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
            
            # Step 2: Move max to its correct position
            res.append(size)
            arr[:size] = reversed(arr[:size])
        
        return res