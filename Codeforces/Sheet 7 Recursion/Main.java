
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        while (n-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            long ans = expo(a, b);
            System.out.println(ans);
        }

    }

    private static long expo(int a, int b) {
        if (b == 0)
            return 1;

        long half = expo(a, b / 2);

        if (b % 2 == 0)
            return half * half;

        return half * half * a;
    }
}
