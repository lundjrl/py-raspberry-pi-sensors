import atexit
from sense_hat import SenseHat



sense = SenseHat()

sense.low_light = True
sense.set_rotation(180)


def exit_handler():
    print("exiting program...")
    sense.clear()


def main():
    print("starting temp reader...")
    
    while True:
        reading = sense.get_pressure()
        sense.show_message(str(round(reading, 2)))


atexit.register(exit_handler)

main()
