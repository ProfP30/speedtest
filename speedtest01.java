public class speedtest01 {       
    public static final int END_LOOP = 1_000_000_000;    
    public static void main(String[] args) {
        // Loop from 1 to 
        int last_number = 0;
        for (int i = 0; i < END_LOOP; i++) {
            last_number = i;
        }
        System.out.println("last_number=" + last_number);
    }
}
