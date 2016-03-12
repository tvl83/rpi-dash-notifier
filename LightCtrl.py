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


def arp_display(pkt):
    print "ARP Packet Found"
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == '74:75:48:dc:30:79':
            print "Yellow Led ON!"
            GPIO.output(YellowLedPin, GPIO.LOW)
        elif pkt[ARP].hwsrc == 'f0:27:2d:bc:61:b3':
            print "Red Led ON!"
            GPIO.output(RedLedPin, GPIO.LOW)
        elif pkt[ARP].psrc == '0.0.0.0':
            print "ARP Probe from: " + pkt[ARP].hwsrc

setup()
print sniff(prn=arp_display, filter="arp", store=0)
