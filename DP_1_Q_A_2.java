public class DP_1_Q_A_2 {
    public static long fib(long n){
        if(n == 0 || n == 1) return 1;
        return fib(n-1) + fib(n-2);
    }
    public static void main(String[] args){
        System.out.println(DP_1_Q_A_2.fib(10));
    }
    
}
