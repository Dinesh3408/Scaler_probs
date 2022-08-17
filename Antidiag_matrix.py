# This is to print the anti diagnals of the matrix
#pleas go through the code for understating the code
class Solution:
    def solve(self, A):
        
        N = len(A)
        for col in  range(N):
            startcol = col-1
            startrow = 0
            
            while startcol >= 0 and startrow < N:
                
                print(A[startrow][startcol], end = " ")
                
                startcol = startcol -1
                startrow = startrow +1
            print()
        for row in range(N):
            startrow = row
            startcol = N-1
            while startrow < N and startcol >=0:
                print(A[startrow][startcol], end = " ")
                startcol = startcol - 1
                startrow = startrow + 1
            print()
                 
s = Solution()
A = [[1,2,3], [4,5,6],[7,8,9]]
s.solve(A)