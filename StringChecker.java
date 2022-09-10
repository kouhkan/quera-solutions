import java.util.Scanner;

public class StringChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String strOne = scanner.nextLine();
        String strTwo = scanner.nextLine();

        String message = strOne.charAt(0) == strTwo.charAt(strTwo.length() - 1) ? "YES" : "NO";

        System.out.println(message);
    }
}
