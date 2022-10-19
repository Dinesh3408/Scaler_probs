def isvowel(ch):
    if(ord(ch) == 65 or ord(ch) == 69 or ord(ch) == 73
       or ord(ch) == 79 or ord(ch) == 85
       or ord(ch) == 97 or ord(ch) == 101 or ord(ch) == 105
       or ord(ch) == 111 or ord(ch) == 117):
       return True
    else:
        return False
class Solution:
    def solve(self, A):
        count = 0

        for i in range(len(A)):
            if isvowel:
                count = count + ((len(A)-i-1))%10003
                
        print(count)

s = Solution()
A= 'ABEC'
s.solve(A)