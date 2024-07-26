import board.GPIO;
import board.test.Boo;

public class Main {

    public static void main(String[] args) {

        Boo boo = new Boo();
        boo.sayBoo();

        GPIO gpio = new GPIO();
        gpio.dRead(4);
        gpio.pullUp(4);

        while (true) {
            boolean isOn = !gpio.dRead(4);
            while (isOn) {
                isOn = !gpio.dRead(4);

                gpio.dWrite(13, true);
                gpio.dWrite(13, false);
            }
        }
    }
}
