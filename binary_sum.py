def addBinary(A, B):
    sum = 0
    
    maxlength = max(len(A), len(B))
    A = A.zfill(maxlength)
    B = B.zfill(maxlength)
    print(A)
    print(B)
   
    res = ''
   
    carry = 0
    for i in range(maxlength-1, -1, -1):
        
        sum = carry + int(A[i])+int(B[i])
        
        if sum > 1:
            res = str(sum % 2) + res
            carry = sum//2
        
        else:
            carry = sum //2
            res = str(sum) + res
    
    print(res)
    
    
  
A  = "1010110111001101101000"
B  = "1000011011000000111100110"
addBinary(A, B)