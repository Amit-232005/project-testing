import java.util.*;

public class array_sum{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int r=sc.nextInt();
        int c=sc.nextInt();

        int[][] a=new int[r][c];
        int[][] b = new int[r][c];

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                a[i][j]=sc.nextInt();
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                b[i][j] = sc.nextInt();
            }
        }
        sc.close();
        sum(a, b, 0, r, c);
    }

        public static void sum(int[][] a,int[][] b,int i,int r,int c){
            if(i==r) return ;
            for (int j=0;j<c;j++){
                System.out.print(a[i][j]+b[i][j]+" ");
            }
            System.out.println();
            sum(a, b, i+1, r, c);
        }


        
    
}