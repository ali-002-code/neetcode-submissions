class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for item in board:
            for char in item:
                if item.count(char) > 1 and char!='.':
                    valid = False
        for i in range(0,9):
            column = []
            for j in range(0,9):
                column.append(board[j][i])
            for char in column:
                if column.count(char) > 1 and char!='.':
                    valid = False
        # check 3x3 boxes
        for box_row in range(0, 9, 3): #start, stop, step
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                for char in box:
                    if char != "." and box.count(char) > 1:
                        return False
        return valid