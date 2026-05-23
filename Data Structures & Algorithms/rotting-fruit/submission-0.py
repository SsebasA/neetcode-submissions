class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        queue = deque()
        time = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                up_neigh = (i - 1, j)
                down_neigh = (i + 1, j)
                left_neigh = (i, j - 1)
                right_neigh = (i, j + 1)
                neighbors = [up_neigh, down_neigh, left_neigh, right_neigh]
                for neighbor in neighbors:
                    if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m:
                        if grid[neighbor[0]][neighbor[1]] == 1:
                            fresh -= 1
                            grid[neighbor[0]][neighbor[1]] = 2
                            queue.append((neighbor[0], neighbor[1]))
        
        if fresh > 0:
            return -1
        else:
            return time
                            
                        
            