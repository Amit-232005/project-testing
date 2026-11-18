import java.util.*;

public class CSES_BookShop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] price = new int[n];
        for (int i = 0; i < n; i++) {
            price[i] = sc.nextInt();
        }
        int[] pages = new int[n];
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }
        sc.close();

        // tabulation
        int[][] dp = new int[n + 1][x + 1];

        dp[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= x; j++) {
                int notpick = dp[i - 1][j];

                int pick = 0;
                if (j >= price[i - 1]) {
                    pick = dp[i - 1][j - price[i - 1]] + pages[i - 1];
                }
                dp[i][j] = Math.max(notpick, pick);
            }

        }
        System.out.println(dp[n][x]);

    }
}
