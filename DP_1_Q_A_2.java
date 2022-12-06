public class DP_1_Q_A_2 {
    public static long fib(long n){
        if(n == 0 || n == 1) return 1;
        return fib(n-1) + fib(n-2);
    }
    public static void main(String[] args){
        System.out.println(DP_1_Q_A_2.fib(10));
    }
    
}

//The above code gives the time complexity of O(2^n) where n is the the input number.Since, we are calculating the same function repeatedly which in turn leading to take more time to get the result. This is called overlapping sub problem. This can be avoid by using storing already calcualted results in a storage.
// This process is called memoization.

//I know the above does not make sense at first glance, but for more details, please go through the below link.

//https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/

//Since, in fibonacii, the current number is explicitly depending upon previous two numbers , we are using two variables to to solve the problem.

// To tackle, overlapping subproblems, there are two approaches
// 1. Topdown (Memoization) - We use recursion and storing the values in array(or lookup table) which are already been calculated for later use while writing code.
// 2. BottomUp (Tabulation) - We are totallly depending upon the array and storing the values from bottom to top and using them when required for processing.

//The above code cabe rewritten as following.

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # I am choosing bottom up approach to solve the problem
    n = int(input())
    first  = 0
    second = 1
    ans = 1
    for i in range(2, n+1):
        ans = first + second
        first = second
        second = ans
    print(ans)


    return 0

if __name__ == '__main__':
    main()


// Topdown Approach using Java

public class fibonacci_topdown {
    int n;
    int[] lookup;
    fibonacci_topdown(int n){ // used constructor initialize lookup array
        this.n = n;
        this.lookup = new int[n+1];
    }

  
    int fib(int n){
        if(n <= 1) lookup[n] = n;
        else lookup[n] = fib(n-1) + fib(n-2);
        return lookup[n];
    }
    public static void main(String[] args){
        int n = 40;
        //int[] lookup = new int[n+1];
        fibonacci_topdown f = new fibonacci_topdown(n);
        System.out.println(f.fib(n));
    }


