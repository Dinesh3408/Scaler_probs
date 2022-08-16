from sys import maxsize


class Solution:
    # @param A : tuple of integers
    # @return an integer
    import sys
    def maxSubArray(self, A):
        ans = -maxsize
        sum = 0
        for i in range(len(A)):
            sum = sum + A[i]
            ans = max(ans,sum)
            if sum < 0:
                sum = 0
        return ans

s = Solution()
A = [1, 2, 3, 4, -10]
print(s.maxSubArray(A))