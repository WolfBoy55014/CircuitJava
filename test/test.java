import board.GPIO;
import board.test.Boo;

public class test {
    
    public static void main(String[] args) {

        Boo boo = new Boo();
        boo.sayBoo();

        GPIO gpio = new GPIO();

        while (true) {
            gpio.write(13, true);
            gpio.write(13, false);
        }
    }
}
