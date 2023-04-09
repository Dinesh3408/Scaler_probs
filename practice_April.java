package Java_April_Practice;



public class practice_April {
    public int binarysearch(int[] A, int left, int right, int B){
        int mid;
        while(left <= right){
            mid = (left+right)/2;
            System.out.println(mid);
            if(A[mid]  == B) return mid;
            else if (A[mid] > B) right = mid-1;
            else left = mid+1;
         
        }
        return right+1;
    }
    public int searchInsert(int[] A, int B){
        int left=0;
        int right = A.length-1;
        return binarysearch(A, left, right, B);
        
        
    //lowerbound int problem in the meaning of the things

    }
    public static void main(String[] args){
        int A[] = {2,3,5,6};
        int B = 1;
        practice_April obj = new practice_April();
        System.out.println(obj.searchInsert(A, B));
    }
   
}
