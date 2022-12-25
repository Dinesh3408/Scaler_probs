#Bathes problem
# A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

# Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

# All students who know each other are placed in one batch.

# Strength of a batch is equal to sum of the strength of all the students in it.

# Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

# Find the number of batches selected.

# NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.

# Problem Constraints

# 1 <= A <= 105

# 1 <= M <= 2*105

# 1 <= B[i] <= 104

# 1 <= C[i][0], C[i][1] <= A

# 1 <= D <= 109



# Input Format

# The first argument given is an integer A.
# The second argument given is an integer array B.
# The third argument given is a matrix C.
# The fourth argument given is an integer D.



# Output Format

# Return the number of batches selected in IB.



# Example Input

# Input 1:

#  A = 7
#  B = [1, 6, 7, 2, 9, 4, 5]
#  C = [  [1, 2]
#         [2, 3] 
#        `[5, 6]
#         [5, 7]  ]
#  D = 12
# Input 2:

#  A = 5
#  B = [1, 2, 3, 4, 5]
#  C = [  [1, 5]
#         [2, 3]  ]
#  D = 6


# Example Output

# Output 1:

#  2
# Output 2:

#  1


# Example Explanation

# Explanation 1:

#  Initial Batches :
#     Batch 1 = {1, 2, 3} Batch Strength = 1 + 6 + 7 = 14
#     Batch 2 = {4} Batch Strength = 2
#     Batch 3 = {5, 6, 7} Batch Strength = 9 + 4 + 5 = 18
#     Selected Batches are Batch 1 and Batch 2.
# Explanation 2:

#  Initial Batches :
#     Batch 1 = {1, 5} Batch Strength = 1 + 5  = 6
#     Batch 2 = {2, 3} Batch Strength = 5
#     Batch 3 = {4} Batch Strength = 4  
#     Selected Batch is only Batch 1.
class Disjointset:
    def __init__(self, n):
        self.parent = [ i for i in range(n)]
        self.rank = [0 for i in range(n)]


class Solution:
    def solve(self, A, B, C, D):

        self.dsu = Disjointset(A+1)
        dsu = self.dsu
        print(dsu.parent)
        print(dsu.rank)
        for i in range(len(C)):
            self.unionbyrank(C[i][0], C[i][1])
        print(dsu.parent)
        print(dsu.rank)
        for i in range( A+1):
            dsu.parent[i] = self.findparent(i)
        print(dsu.parent)
        dict ={}
        selected = 0
        for i in range(1, A+1):
            if(dsu.parent[i] not in dict):
                dict[dsu.parent[i]] = B[i-1]
            else:
                dict[dsu.parent[i]] += B[i-1]
        for key, val in dict.items():
            if val >= D:
                selected +=1
        return selected
        
    def findparent(self, node):
        dsu = self.dsu
        if(node == dsu.parent[node]):
            return node
        dsu.parent[node] = self.findparent(dsu.parent[node])
        return dsu.parent[node]
    def unionbyrank(self, U, V):
        dsu = self.dsu
        parent_u = self.findparent(U)
        parent_v = self.findparent(V)
        if(parent_u == parent_v): return
        if(dsu.rank[parent_u] < dsu.rank[parent_v]):
            dsu.parent[parent_u] = parent_v
        elif(dsu.rank[parent_v] < dsu.rank[parent_u]):
            dsu.parent[parent_v] = parent_u
        else:
            dsu.parent[parent_v] = parent_u
            dsu.rank[parent_u] =  dsu.rank[parent_u] + 1
        

              

s = Solution()
# A = 7
# B = [1, 6, 7, 2, 9, 4, 5]
# C = [   [1, 2],
#         [2, 3],
#         [5, 6],
#         [5, 7]  ]
# D = 12

A = 14
B = [ 7, 5, 7, 3, 9, 4, 4, 6, 3, 1, 4, 8, 7, 6 ]
C = [
  [1, 2],
  [2, 6],
  [2, 7],
  [4, 13],
  [5, 8],
  [5, 13],
  [6, 12],
  [7, 10],
  [10, 14],
  [13, 14],
]
D = 2
print(s.solve(A, B, C ,D))

