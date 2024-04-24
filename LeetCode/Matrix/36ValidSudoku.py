class Solution:
    """def isValidSudoku(self, board: List[List[str]]) -> bool:
        # counter for 
        # line
        # column
        # squares

        # array size 9 direction down / right
        for i in range(0,9):
            # check for each numbers from 1 to 9
            for m in range(1,10):
                n = str(m)
                
                # reset count for each number
                count_c = 0
                count_l = 0
                sount_s = 0
                
                # check line
                if  board[i].count(n) > 1:
                    return False

                # check column
                for j in range(0,9):
                    # check column
                    if board[j][i] == n:
                        count_c += 1
                    
                    if count_c > 1:
                        return False

                
                
                
        for i in range(0,3):
            for j in range(0,3):
                for m in range(1,10):
                    n = str(m)
                    count_s = 0
                    print("_________")
                    print("n: " + n)
                    for a in range(0,3):
                        for b in range(0,3):
                            print("i*3 + a: " + str(i*3 + a) + " j*3 + b: " + str(j*3 + b))
                            print(board[i*3 + a][j*3 + b])
                            if board[i*3 + a][j*3 + b] == n:
                                count_s += 1
                            
                            if count_s > 1:
                                return False
                        
        return True"""
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np        
        # create 2D array for counter for line, column, and square: 3
        # each inner counter array show the count of n in the specified line, column or square line
        # counter[0][0]: shows the count of n in the 0th line of the sudoku
        # counter[1][5]: shows the count of n in the 5th column of the sudoku
        # counter[2][8]: shows the count of n in the 8th(last) square of the sudoku
        counter = np.empty((3, 9))

        # check for all numbers from 1 to 9
        for m in range(1,10):
            n = str(m)
            # reset counter for each number
            counter[counter<10] = 0

            # check all cells in the sudoku: 9x9 = 81 cell
            for i in range(0,9):
                for j in range(0,9):

                    # check line
                    if board[i][j] == n:
                        if counter[0][i] > 0:
                            return False
                        counter[0][i] += 1
                    
                    # check column
                    if board[j][i] == n:
                        if counter[1][i] > 0:
                            return False
                        counter[1][i] += 1

                    # There is 9 square in the sudoku
                    # find in which line the current numbers's square
                    #l = i // 3
                    # find in which column the current numbers's square
                    #c = j // 3

                    
                    if board[i][j] == n:
                        if counter[2][3*(i//3) + j//3] > 0:
                            return False
                        counter[2][3*(i//3) + j//3] += 1
                    
        return True