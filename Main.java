import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Integer t=sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            Long[] arr = new Long[n];
            Long sum  = 0L;
            Long maxSoFar = 0L;
            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextLong();
                sum += arr[j];
                maxSoFar= Math.max(maxSoFar,sum);
                if(sum<0){
                    sum = 0L;
                }
            }
            System.out.println(maxSoFar);
        }

        sc.close();
    }
}