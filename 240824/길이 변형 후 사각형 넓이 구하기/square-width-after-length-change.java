import java.util.Scanner;

public class Main {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); // - 기호가 나오기 전까지 입력 진행
        int b = sc.nextInt(); // - 기호가 나오기 전까지 입력 진행
        a+=8;
        b*=3;
        System.out.println(a);
        System.out.println(b);
        System.out.println(a*b);
    }
}