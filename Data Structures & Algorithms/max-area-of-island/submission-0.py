class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        row = len(grid)
        cols = len(grid[0])

        for i in range(row):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] != 0:
                    area = self.bfs(i, j, visited, grid)
                    max_area = max(max_area, area)
        
        return max_area

    
    def bfs(self, i, j, visited, grid) -> int:
        cola = deque([(i, j)])
        visited.add((i,j))
        area = 1 
        while cola:
            actual_node = cola.popleft()
            nh_up = (actual_node[0]+1, actual_node[1])
            nh_down = (actual_node[0]-1, actual_node[1])
            nh_left = (actual_node[0], actual_node[1]-1)
            nh_right = (actual_node[0], actual_node[1]+1)
            nhs = [nh_up, nh_down, nh_left, nh_right]
            for nh_node in nhs:
                if(nh_node not in visited and
                   0 <= nh_node[0] < len(grid) and
                   0 <= nh_node[1] < len(grid[0]) and 
                   grid[nh_node[0]][nh_node[1]] == 1
                ):
                    area += 1
                    visited.add(nh_node)
                    cola.append(nh_node)
        
        return area
            




