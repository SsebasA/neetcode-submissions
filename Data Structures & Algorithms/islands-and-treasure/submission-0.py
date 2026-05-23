class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        INF = 2**31 - 1

        queue = deque()
        seen = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        
        while queue:
            i, j = queue.popleft()
            vec_izq = (i, j - 1)
            vec_der = (i, j + 1)
            vec_up = (i - 1, j)
            vec_down = (i + 1, j)

            vecinos = [vec_izq, vec_der, vec_up, vec_down]
            for vecino in vecinos:
                if 0 <= vecino[0] < n and 0 <= vecino[1] < m:
                    if grid[vecino[0]][vecino[1]] == INF and (vecino[0],vecino[1]) not in seen:
                        grid[vecino[0]][vecino[1]] = grid[i][j] + 1
                        seen.add((vecino[0], vecino[1]))
                        queue.append((vecino[0], vecino[1]))

        