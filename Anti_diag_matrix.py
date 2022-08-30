#Getting all Antidiagonals of the matrix in a matri format
A =[[ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]]


M = len(A)
N = len(A[0])
output = [[]  for i in range(M+N-1)]

c = 0
r = 0
oj = 0
while r < M:
    i = r
    j = c
      
    
    while  i < M and j >= 0 :
        #print(A[i][j], end = ' ')
        output[oj].append(A[i][j])        
        i = i+1
        j = j-1
        
    
    if c < N-1:
        c = c +1
    else:
        r = r +1
    oj = oj +1
for oj in range(M+N-1):
    while len(output[oj])< N:
        output[oj].append(0)
print(output)

'''
sizeOfMatrix = len(A)
        B = [[] for _ in range(2* sizeOfMatrix -1)]
        # print(B)
        Bj =0
        for j in range(sizeOfMatrix):
            i = 0
            while(j >= 0 ):
                # print(i,j)
                B[Bj].append(A[i][j])
                i+=1
                j-=1
            Bj+=1
        # print(B)
        for i in range(1,sizeOfMatrix):
            j = sizeOfMatrix-1
            while(i < sizeOfMatrix ):
                # print(i,j)
                B[Bj].append(A[i][j])
                i+=1
                j-=1
            Bj+=1
        for Bi in range(2 *sizeOfMatrix -1):
            while (len(B[Bi])< sizeOfMatrix):
                B[Bi].append(0)
        # print(B)
        return B
'''
       
    
    


     



