import atexit
from sense_hat import SenseHat



sense = SenseHat()

sense.low_light = True
sense.set_rotation(180)


def exit_handler():
    print("exiting program...")
    sense.clear()


def main():
    print("starting humidity reader...")
    
    while True:
        reading = sense.get_humidity()
        reading = round(reading, 1)
        sense.show_message(str(reading))


atexit.register(exit_handler)

main()
