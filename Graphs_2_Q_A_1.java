// Q1. Rotten Oranges
// Solved
// character backgroundcharacter
// Stuck somewhere?
// Ask for help from a TA and get it resolved.
// Get help from TA.
// Problem Description
// Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

// Each cell can have three values:

// The value 0 representing an empty cell.

// The value 1 representing a fresh orange.

// The value 2 representing a rotten orange.

// Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

// Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



// Problem Constraints
// 1 <= N, M <= 1000

// 0 <= A[i][j] <= 2



// Input Format
// The first argument given is the integer matrix A.



// Output Format
// Return the minimum number of minutes that must elapse until no cell has a fresh orange.

// If this is impossible, return -1 instead.



// Example Input
// Input 1:

// A = [   [2, 1, 1]
//         [1, 1, 0]
//         [0, 1, 1]   ]
// Input 2:

 
// A = [   [2, 1, 1]
//         [0, 1, 1]
//         [1, 0, 1]   ]


// Example Output
// Output 1:

//  4
// Output 2:

//  -1


// Example Explanation
// Explanation 1:

//  Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
// Explanation 2:

//  Task is impossible


import java.util.LinkedList;
import java.util.Queue;
class pairs{
    int first;
    int second;
    int time;
    public pairs(int first, int second, int time){
        this.first = first;
        this.second = second;
        this.time = time;
    }
}
public class rottenoranges {
   
    public int minTime(int[][] A, int N, int M){
        Queue<pairs> q = new LinkedList<>();
        
        
        for(int i =0; i< N; i++){
            for(int j =0; j<M; j++){
                if(A[i][j] == 2){
                    q.add(new pairs(i, j, 0));
                }
            }
        }
        int[] x = {-1, 1, 0, 0};
        int[] y = {0, 0, -1, 1};
        int maxtime = Integer.MIN_VALUE;
        while(!q.isEmpty()){
            pairs d = q.peek();
            q.remove();
            int first = d.first;
            int second = d.second;
            

            for(int k=0;k<4;k++){
                int a = first + x[k];
                int b = second + y[k];

                if(a>=0 && a<N && b>=0 && b<M && A[a][b] == 1){
                    A[a][b] = 2;
                    
                    q.add(new pairs(a,b,d.time+1));
                }
                maxtime = Math.max(maxtime, d.time);
            }
        }
        
        for(int i=0; i < N; i++){
            for(int j =0; j < M; j++){
                if(A[i][j] == 1) return -1;
            }
        }
        return maxtime;
    }

        
    
    public int solve(int[][] A) {
        int N = A.length;
        int M = A[0].length;
        return minTime(A, N, M);
       
    }
    public static void main(String[] args){
        rottenoranges ro = new rottenoranges();
        int[][] A = {{2, 1, 1},{1, 1, 0},{0, 1, 1}};
        System.out.println(ro.solve(A));
    }
}
