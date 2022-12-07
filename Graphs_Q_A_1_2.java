// Problem Description
// You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

// Given 2 towns find whether you can reach the first town from the second without repeating any edge.

// B C : query to find whether B is reachable from C.

// Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

// There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

// NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.



// Problem Constraints
// 1 <= N <= 100000



// Input Format
// First argument is vector A

// Second argument is integer B

// Third argument is integer C



// Output Format
// Return 1 if reachable, 0 otherwise.



// Example Input
// Input 1:

//  A = [1, 1, 2]
//  B = 1
//  C = 2
// Input 2:

//  A = [1, 1, 2]
//  B = 2
//  C = 1


// Example Output
// Output 1:

//  0
// Output 2:

//  1


// This is to calcuate the depth first search of the given input
import java.util.*;
public class Graphs_Q_A_1_2 {
    public void dfs(ArrayList<Integer>[] graph, int[] A, int C, boolean[] visted){
        if(visted[C]==true) return;
        visted[C] = true;
        for(int i=0; i< graph[C].size();i++){
            int node = graph[C].get(i);
            if(visted[node] == false)
                dfs(graph, A, node, visted);       
        }
    }
 
    public void solve(int[] A, final int B, final int C){
        //first I need to build a graph out of the given array
        int n = A.length;
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i =0; i <=n;i++){
            graph[i] = new ArrayList<Integer>();
        }
        for(int i=0; i < n;i++){
            graph[A[i]].add(i+1);
        }
        for(int i =0; i < graph.length;i++){
            ArrayList<Integer> l = graph[i];
            System.out.println(l);
        }
        boolean visted[] = new boolean[n+1];
        dfs(graph, A, C, visted);
        if(visted[B] == true) System.out.println("yes");
        else System.out.println("False");

        

          
    }
    public static void main(String[] args){
        int A[] = {1,1,2};
        int B = 2;
        int C = 1;
        Graphs_Q_A_1_2 graph = new Graphs_Q_A_1_2();
        graph.solve(A, B, C);

        // need to find the path if exist from C to B;
    }
}
