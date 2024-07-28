# CircuitJava
CircuitJava is a Java 8 JVM made to run on most CircuitPython compatible microcontrollers.
CircuitJava was made for onboarding new programmers for the FRC team 2472.
Writing it in Python made it faster to ship, but makes it harder for low-end boards to run effectively.
CircuitJava supports microcontroller-related functions natively in the `board` java package.
A C++ version for RP2040-based boards using the Pico SDK may come in the future.

## Installation/Setup
To install CircuitJava onto a microcontroller:
1. Download and Install CircuitPython for your board from [their website](https://circuitpython.org/downloads).
2. Clone/Download this repo and move it into the `CIRCUITPY` drive.
3. Modify the pins in the `_int_2_pin()` function in `Jboard.py` to work with your board by asigning a number to each named pin from CircuitPython. (Its currently set up for the Feather RP2040)

## Usage
To run a Java Class in CircuitJava, either write the Java project in the `CIRCUITPY` drive, or copy the `board` directory to the folder where your Java project is.
Then compile your *.java files using the `javac` command. (If you don't have a Java 8 SDK, you can get one [here](https://adoptium.net/temurin/releases/?version=8).
The class containing the main function should be called `Main`. (Or the name of the main class can be specified in `settings.toml`)
Copy the *.class files back to the `CIRCUITPY` drive if they aren't in it already.
Restart the microcontroller, and it should run.

## Limitations
CircuitJava is not perfect and can't do the following *yet*:
1. Run long programs quickly or precisely
2. StringBuilder is not implemented yet (this prevents adding strings with other variables like in `System.out.println("Value: " + i)`)
3. CircuitJava can't run jar files

## If You Run Into Issues...
File an Issue! I'd love to help you add your microcontroller to the list, or work on fixing the holes in the JVM. Feel free to fork and help too! My knowledge of JVM's is not perfect, so I'd really appreciate any insite you have.
