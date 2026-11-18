import java.util.*;

public class combination {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();

        sc.close();
        long ans = fun(n, r);
        System.out.println(ans);
    }

    public static long fun(int n, int r) {
        if(n<0 || r<0 || n<r) return 0;
        if (n == r || r == 0) {
            return 1;
        }
        return fun(n - 1, r - 1) + fun(n - 1, r);
    }
}