# Problem Description
# Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

# Problem Constraints
# 1 <= A <= 105

# Input Format
# First and only argument is an integer A.

# Output Format
# Return an integer denoting the minimum count.

# Example Input
# Input 1:

#  A = 6
# Input 2:

#  A = 5


# Example Output
# Output 1:

#  3
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
#  Minimum count of numbers, sum of whose squares is 6 is 3. 
# Explanation 2:

#  We can represent 5 using only 2 numbers i.e. 12 + 22 = 5

class Solution:
    def utilityfunc(self,A, dp):
        if dp[A]  != -1:
            return dp[A]
        ans = A
        i = 1
        while i*i <= A:
            ans = min(ans, 1+ self.utilityfunc(A - i*i, dp))
            i +=1
        dp[A] = ans
        return ans

    def solve(self, A):

        dp = [-1] * (A+1)
        dp[0], dp[1] = 0,1
        print(self.utilityfunc(A, dp))
        
s = Solution()
A = 8
s.solve(A)


 

