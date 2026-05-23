class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: 
            return []

        row = len(heights)            
        col = len(heights[0])

        pac_reachable = set()
        atl_reachable = set()

        for c in range(0, col):
            pac_reachable.add((0, c))
            atl_reachable.add((row - 1, c))
        
        for r in range(0, row):
            pac_reachable.add((r, 0))
            atl_reachable.add((r, col - 1))
        
        def BFS(coordinates):
            queue = deque(coordinates)
            while queue:
                r, c = queue.popleft()
                up_n = (r - 1, c)
                down_n = (r + 1, c)
                left_n = (r, c - 1)
                right_n = (r, c + 1)
                neighbors = [up_n, down_n, left_n, right_n]
                for neighbor in neighbors:
                    if neighbor not in coordinates:
                        if (0 <= neighbor[0] < row and 0 <= neighbor[1] < col) and heights[neighbor[0]][neighbor[1]] >= heights[r][c]:
                            queue.append((neighbor[0], neighbor[1]))
                            coordinates.add((neighbor[0], neighbor[1]))
                        
        BFS(pac_reachable)
        BFS(atl_reachable)

        res = list(pac_reachable & atl_reachable)
        return res 
                
        


