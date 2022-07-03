import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();
        Integer m = sc.nextInt();
        int[][] arr = new int[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j] = sc.nextInt();
            }
        }
        int searchElement = sc.nextInt();
        int low = 0;
        int high = (n*m);
        int result = -1;
        while(low<high){
            int mid = (low+high)/2;
            System.out.println(mid);
            int row = mid/n;//some operation;

            int col = mid%n%m;//some other operation;
            
            if(searchElement == arr[row][col]){
                result = mid;

                break;
            }else if (searchElement< arr[row][col]){
                high = mid-1;
            }else{
                low = mid+1;
            }
        }   
        if(result!=-1){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
        sc.close();


    }
}