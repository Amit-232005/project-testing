import java.util.Scanner;

public class maximum_path_sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        sc.close();
        System.out.println(path_sum(arr, 0, 0));
    }

    private static int path_sum(int[][] arr, int i, int j) {
        if (i >= arr.length || j >= arr[0].length) {
            return Integer.MIN_VALUE;
        }
        if (i == arr.length - 1 && j == arr[0].length - 1) {
            return arr[i][j];
        }
        return arr[i][j] + Math.max(path_sum(arr, i + 1, j), path_sum(arr, i, j + 1));
    }
}