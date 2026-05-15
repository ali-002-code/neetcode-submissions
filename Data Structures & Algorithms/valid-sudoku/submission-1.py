class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() #set is unordered collection of values
        for row in range(9): #check each value in the row
            for col in range(9): #check each value in column
                val = board[row][col] #get the value from the board
                if val == ".": #if value is a . skip this iteration
                    continue
                #create a key for row, column and box
                row_key = ("row", row, val) 
                col_key = ("col", col, val)
                box_key = ("box", row // 3, col // 3, val)

                #if key seen before false
                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                #add keys to seen
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True