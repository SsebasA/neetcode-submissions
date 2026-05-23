class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                coord = (i, j)
                elem = grid[i][j]
                if coord not in visited and elem != "0":
                    count += 1
                    self.bfs(i, j, visited, grid)
        
        return count

    def bfs(self, i, j, visited, grid):
        queue = deque([(i, j)])
        visited.add((i, j))

        while queue:
            actual_node = queue.popleft()
            up_neighbor = (actual_node[0]+1, actual_node[1])
            down_neighbor = (actual_node[0]-1, actual_node[1])
            left_neighbor = (actual_node[0], actual_node[1] - 1)
            right_neighbor = (actual_node[0], actual_node[1] + 1)

            neighbors = [up_neighbor, down_neighbor, left_neighbor, right_neighbor]
            for node_neighbor in neighbors:
                if (node_neighbor not in visited and   
                    0 <= node_neighbor[0] < len(grid) and
                    0 <= node_neighbor[1] < len(grid[0]) and 
                    grid[node_neighbor[0]][node_neighbor[1]] == "1"
                ):
                    queue.append(node_neighbor)
                    visited.add(node_neighbor)

        


