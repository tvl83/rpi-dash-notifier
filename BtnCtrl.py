from scapy.all import *
import RPi.GPIO as GPIO

YellowLedPin = 7
YellowBtnPin = 12

RedLedPin = 11
RedBtnPin = 13

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(YellowLedPin, GPIO.OUT)
    GPIO.setup(YellowBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RedLedPin, GPIO.OUT)
    GPIO.setup(RedBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(YellowLedPin, GPIO.HIGH)
    GPIO.output(RedLedPin, GPIO.HIGH)

def loop():
    while True:
        if GPIO.input(YellowBtnPin) == GPIO.LOW:
            print "Yellow Led OFF!"
            GPIO.output(YellowLedPin, GPIO.HIGH)
        elif GPIO.input(RedBtnPin) == GPIO.LOW:
            print "Red Led OFF!"
            GPIO.output(RedLedPin, GPIO.HIGH)
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
