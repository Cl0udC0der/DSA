# Neetcode solution
# One pass cycle through the entire input where 2 iterations happen 
# Check if empty, continue
# Check if duplicates in row, col, or square (via squares[r // 3, col // 3] to floor division into the right square)
# If a dupe exists in any, return false, otherwise add the entry into the hashmap to check in next
# If it all continues without error/s, return true

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True