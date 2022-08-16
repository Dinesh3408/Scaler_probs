from pyclbr import Class


class Solution:
    def solve(self, A):


        for i in range(len(A)):
            if not (A[i].isalpha()):
                
                
                return 0
        return 1
    
            

A = ['S', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
s= Solution()
print(s.solve(A))



