import board.GPIO;
import board.test.Boo;

public class test {
    
    public static void main(String[] args) {

        Boo boo = new Boo();
        boo.sayBoo();

        GPIO gpio = new GPIO();
        gpio.read(4);
        gpio.pullUp(4);
        
        while (true) {
            boolean isOn = gpio.read(4);
            gpio.write(13, !isOn);
        }
    }
}
