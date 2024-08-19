public class speedtest01 {
    public static void main(String[] args) {
        int last_number = 0;
        // Loop from 1 to 1.000.000.000
        for (int i = 0; i < 1_000_000_000; i++) {
            last_number = i;
        }
        System.out.println("last_number: " + last_number );
    }
}
