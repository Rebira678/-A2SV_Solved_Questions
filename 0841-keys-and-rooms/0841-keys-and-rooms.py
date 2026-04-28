class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque(rooms[0])
        
        visited.add(0)  
        while queue:
            room = queue.popleft()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        queue.append(key)
        
        return len(visited) == len(rooms)   

