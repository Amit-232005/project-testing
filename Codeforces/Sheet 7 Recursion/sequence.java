import java.util.Scanner;

public class sequence {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(length(n));
        sc.close();

    }

    public static int length(int n) {
        if (n == 1)
            return 1;
        if (n % 2 == 0)
            return 1 + length(n / 2);
        return 1 + length(3 * n + 1);
    }
}
