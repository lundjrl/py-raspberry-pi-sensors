import atexit
from sense_hat import SenseHat



sense = SenseHat()
temp = sense.get_temperature()

sense.set_rotation(180)


def exit_handler():
    print("exiting program...")
    sense.clear()


def convertCelsiusToFahrenheit():
    print(round(temp, 1))
    return round(temp * 1.8 + 32, 1)


def main():
    print("starting temp reader...")
    
    while True:
        sense.show_message(str(convertCelsiusToFahrenheit()))


atexit.register(exit_handler)

main()
