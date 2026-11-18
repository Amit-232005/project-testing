import java.util.*;

public class Zuma_607B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                int res = 1 + dp[i + 1][j];
                if (arr[i] == arr[j]) {
                    res = Math.min(res,
                            Math.max(1, dp[i + 1][j - 1]));
                }
                for (int k = i + 1; k < j; k++) {
                    res = Math.min(res,
                            dp[i][k] + dp[k + 1][j]);
                }
                dp[i][j] = res;
            }
        }
        System.out.println(dp[0][n - 1]);

        // System.out.println("DP Table");
        // for (int[] row : dp) {
        // for (int i : row) {
        // System.out.print(i + " ");
        // }
        // System.out.println();
        // }
    }

}

// failing test case with else
// 1 2 1 1 3 1

// correct ans=2
// but with else it gives 3