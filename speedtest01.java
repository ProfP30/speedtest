public class speedtest01 {       
    public static final int END_LOOP = 1_000_000_000; // 1 Mrd.
    public static void main(String[] args) {
        // Loop from 1 to 
        int last_number = 0;
        for (int i = 0; i < END_LOOP; i++) {
            last_number++;
        }
        System.out.println("Java:last_number=" + last_number + "\n");
    }
}
