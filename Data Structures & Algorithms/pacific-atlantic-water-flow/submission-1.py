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
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 0 <= nc < col) and (nr, nc) not in coordinates and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
                        coordinates.add((nr, nc))
                        
        BFS(pac_reachable)
        BFS(atl_reachable)

        res = list(pac_reachable & atl_reachable)
        return res 
                
        


