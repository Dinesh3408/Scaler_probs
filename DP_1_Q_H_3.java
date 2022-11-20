// Q3. Ways to Decode

// Problem Description:
// A message containing letters from A-Z is being encoded to numbers using the following mapping:

// 'A' -> 1
// 'B' -> 2
// ...
// 'Z' -> 26
// Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.



// Problem Constraints
// 1 <= length(A) <= 105



// Input Format
// The first and the only argument is a string A.



// Output Format
// Return an integer, representing the number of ways to decode the string modulo 109 + 7.



// Example Input
// Input 1:

//  A = "12"
// Input 2:

//  A = "8"


// Example Output
// Output 1:

//  2
// Output 2:

//  1


// Example Explanation
// Explanation 1:

//  Given encoded message "8", it could be decoded as only "H" (8).
//  The number of ways decoding "8" is 1.
// Explanation 2:

//  Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
//  The number of ways decoding "12" is 2.



public class DP_1_Q_H_3 {
    public int numDecodings(String A) {
        //Bottom up approach constant space
        int n = A.length();
        if(n==0 || A.charAt(0)== '0') return 0;
        long less_two = 1;
        long less_one = 1;
        long mod = 1000000007;

        for(int i = 2; i <= n; i++){
            char currentchar = A.charAt(i-1);
            long cur =0;
            if(currentchar != '0')  cur = less_one%mod;
            char previouschar= A.charAt(i-2);
            if((previouschar == '1') || (previouschar == '2' && (currentchar >= '0' && currentchar <= '6'))){
                cur += less_two;

            }
            less_two = less_one;
            less_one = cur;
        }
        
        return (int) (less_one % mod);
    }
    public static void main(String[] args){
        String A = "12134";
        DP_1_Q_H_3 obj = new DP_1_Q_H_3();
        System.out.println(obj.numDecodings(A));



    }

    
}

