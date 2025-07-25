import atexit
from sense_hat import SenseHat



sense = SenseHat()
humidity = sense.get_humidity()
humidity = round(humidity, 1)

sense.set_rotation(180)


def exit_handler():
    print("exiting program...")
    sense.clear()


def main():
    print("starting humidity reader...")
    
    while True:
        sense.show_message(str(humidity))


atexit.register(exit_handler)

main()
