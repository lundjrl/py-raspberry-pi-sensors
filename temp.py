import atexit
from sense_hat import SenseHat



sense = SenseHat()

sense.low_light = True
sense.set_rotation(180)


def exit_handler():
    print("exiting program...")
    sense.clear()


def convertCelsiusToFahrenheit(val):
    return round(val * 1.8 + 32, 1)


def main():
    print("starting temp reader...")
    
    while True:
        reading = sense.get_temperature()
        sense.show_message(str(convertCelsiusToFahrenheit(reading)))


atexit.register(exit_handler)

main()
