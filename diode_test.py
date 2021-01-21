import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

blink_count = 3
count = 0
led_pin = 18

GPIO.setup(led_pin, GPIO.OUT)

while count < blink_count:
    GPIO.output(led_pin, True)
    print("LED ON")
    sleep(3)
    GPIO.output(led_pin, False)
    print("LED OFF")
    sleep(1)
    count += 1