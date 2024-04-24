class Solution:
    # GOOD FOR MEMORY, BAD FOR RUNTIME
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
                        
        return True