public class DP_1_Q_A_2 {
    public static long fib(long n){
        if(n == 0 || n == 1) return 1;
        return fib(n-1) + fib(n-2);
    }
    public static void main(String[] args){
        System.out.println(DP_1_Q_A_2.fib(10));
    }
    
}

//The above code gives the time complexity of O(2^2) as we are calculating the same funtion again and again. This is called overlapping sub problems. This can be avoid by using storing already calcualted results in a storage.
// This process is called memoization.
//Since, in fibonacii, the current number is explicitly depending upon previous two numbers , we are using two variables to to solve the problem.

//The above code cabe rewritten as

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