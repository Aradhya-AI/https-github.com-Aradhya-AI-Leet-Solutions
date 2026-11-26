class Solution:
    def canAliceWin(self, n: int) -> bool:
        moves = 10
        count = 0

        while n >= moves:
            n -= moves
            count += 1
            moves -= 1

        return count % 2 == 1