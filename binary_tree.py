
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, A):
        #recursive way
        '''
        if A:
            self.inorderTraversal(A.left)
            print(A.val)
            self.inorderTraversal(A.right)
        '''
        output = []
        stack = []
        temp = A
        while temp or len(stack) !=0:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            output.append(temp.val)
            temp = temp.right
        print(output)
    def preordertraversal(self,A):
        #using recursive way
        '''
        if A:
            print(A.val)
            self.preordertraversal(A.left)
            self.preordertraversal(A.right)
        '''
        output  = []
        stack = []
        temp = A
        stack.append(temp)
        while len(stack) != 0:

            temp = stack.pop()
            output.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
                
        print(output)
    def postordertraversal(self,A):
        #recursive solution
        '''
        if A:
            self.postordertraversal(A.left)
            self.postordertraversal(A.right)
            print(A.val)
        '''
        output = []
        stack1 = []
        
        
        temp = A
        stack1.append(temp)
        while len(stack1) != 0:
            temp = stack1.pop()
            output.append(temp.val)
            if temp.left:
                stack1.append(temp.left)
                
            if temp.right:
                stack1.append(temp.right)
                
        print(output[::-1])
    def tree_height(self,A):
        if not A:
            return 0
        stack = []
        height = 0
        stack.append(A)
        while len(stack)> 0:
            node_count = len(stack)
            while node_count:
                popped = stack.pop(0)
                if popped.left:
                    stack.append(popped.left)
                if popped.right:
                    stack.append(popped.right)
                node_count = node_count -1
            height = height + 1
        print(height)
        
            
            
            
            


           
            
            

s = Solution()
t = TreeNode(1)
t.right = TreeNode(3)
t.left = TreeNode(2)
t.left.left= TreeNode(4)
t.left.right = TreeNode(5)

t.right.right = TreeNode(6)
s.inorderTraversal(t)
s.preordertraversal(t)
s.postordertraversal(t)
s.tree_height(t)
        