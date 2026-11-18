import java.util.Scanner;

public class array_avg {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int n=sc.nextInt();
        int[] arr=new int[n];

        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        sc.close();
        float avg= (float) sum(arr, n, 0)/n;
        System.out.printf("%.6f",avg);

    }
    public static long sum(int[] arr,int n,int i) {
        if (i==n){
            return 0;
        }
        return arr[i]+sum(arr,n,i+1);
    }
}