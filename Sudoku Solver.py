class Solution(object):
    def solveSudoku(self, board):
        
        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3

            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack():
            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":
                        
                        for num in "123456789":

                            if isValid(row, col, num):
                                board[row][col] = num

                                if backtrack():
                                    return True

                                # Undo the choice
                                board[row][col] = "."

                        return False

            return True

        backtrack()