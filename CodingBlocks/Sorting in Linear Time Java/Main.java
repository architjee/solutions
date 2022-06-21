import java.util.*;
public class Main {
    public static void main(String args[]) {
        // Your Code Here
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();
        int[] arr = new int[n];        
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        sc.close();
        int low=0, mid=0, high = n-1;
        while(mid<=high){
            if(arr[mid]==0){
                Integer temp = arr[mid];
                arr[mid]=arr[low];
                arr[low] = temp;
                low++; mid++;
            }
            else if(arr[mid]==1){
                    mid++;
            }else{
                // Arr[mid]==2;
                Integer temp = arr[high];
                arr[high] = arr[mid];
                arr[mid] = temp;
                high--;
            }
        }
        for (int j = 0; j < arr.length; j++) {
            System.out.println(arr[j]);
            
        }
    }
}
