# Q3. Flip Array


# Given an array A of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible).

# Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.



# Problem Constraints

# 1 <= length of(A) <= 100

# Sum of all the elements will not exceed 10,000.



# Input Format

# First and only argument is an integer array A.



# Output Format

# Return an integer denoting the minimum number of elements whose sign needs to be flipped.



# Example Input

# Input 1:

#  A = [15, 10, 6]
# Input 2:

#  A = [14, 10, 4]


# Example Output

# Output 1:

#  1
# Output 2:

#  1


# Example Explanation

# Explanation 1:

#  Here, we will flip the sign of 15 and the resultant sum will be 1.
# Explanation 2:

#  Here, we will flip the sign of 14 and the resultant sum will be 0.
#  Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there sign are not minimum.

class Solution:
    def solve(self, A):
        total = sum(A)//2
        dp = [[0 for i in range(total+1)]for i in range(len(A)+1)]
        for i in range(len(A)+1):
            for j in range(total+1):
                if i==0 and j > 0:
                    dp[i][j] = float('inf')
                elif A[i-1] <= j and dp[i-1][j-A[i-1]] != float('inf'): 
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-A[i-1]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
        #i = total
        while(dp[len(A)][total] == float('inf')):
            total = total -1
        print(dp[len(A)][total])
    

        #print(dp)
s = Solution()
A = [ 8, 4, 5, 7, 6, 2 ]
s.solve(A)



