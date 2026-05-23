class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None

        row = len(board)
        col = len(board[0])

        queue = deque()
        
        for i in range(row):
            for j in range(col):
                if (i in [0, row - 1] or j in [0, col - 1]) and board[i][j] == "O":
                    board[i][j] = "#"
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < row and 0 <= nc < col) and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
