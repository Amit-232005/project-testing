import java.util.Scanner;

public class Student {
    String name;
    int rollNo;
    int marks;
    private static final Scanner sc = new Scanner(System.in);

    private void input() {
        System.out.print("Enter Name: ");
        name = sc.nextLine();

        System.out.print("Enter Roll no: ");
        rollNo = Integer.parseInt(sc.nextLine());

        System.out.print("Enter marks: ");
        marks = Integer.parseInt(sc.nextLine());
    }

    private void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Marks: " + marks);

        if (isPassed()) {
            System.out.println("Status: Passed");
        } else {
            System.out.println("Status: Failed");
        }
        System.out.println("----------------------------");

    }

    private boolean isPassed() {
        return marks >= 40;
    }

    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student();
        s1.input();
        s2.input();

        s1.display();
        s2.display();

        s1.isPassed();
        s2.isPassed();
    }
}
