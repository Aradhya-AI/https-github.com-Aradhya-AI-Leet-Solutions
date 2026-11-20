class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            board[r][c] = 1 if i % 2 == 0 else 2

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return "A" if board[i][0] == 1 else "B"

            if board[0][i] == board[1][i] == board[2][i] != 0:
                return "A" if board[0][i] == 1 else "B"

        if board[0][0] == board[1][1] == board[2][2] != 0:
            return "A" if board[0][0] == 1 else "B"

        if board[0][2] == board[1][1] == board[2][0] != 0:
            return "A" if board[0][2] == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"