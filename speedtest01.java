public class Main {
    public static void main(String[] args) {
        int last_number = 0;
        // Loop from 1 to 1.000.000.000
        for (int i = 1; i <= 1000000000; i++) {
            last_number = i;
        }
        System.out.println("last_number: " + last_number );
    }
}
