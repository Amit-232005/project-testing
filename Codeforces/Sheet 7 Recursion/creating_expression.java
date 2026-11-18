
import java.util.Scanner;

public class creating_expression {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int x=sc.nextInt();
        int[] arr=new int[n];

        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }

        sc.close();
        int sum=arr[0];
        if(check(arr, 1, x,sum)){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }

    }
    private static boolean check(int[] arr,int i,int x,int sum){
        if(i==arr.length){
            return sum==x;
        }
        boolean plus=check(arr, i+1, x, sum+arr[i]);
        boolean minus=check(arr, i+1, x, sum-arr[i]);
        return plus || minus;
    }
}
