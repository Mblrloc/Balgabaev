import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dec = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dec, GPIO.OUT)
t = 20
try:
    while True:
        for a in range(0, 256, 1):
            GPIO.output(dec, dec2bin(a))   
            time.sleep(t / 255)
        for a in range(255, -1, -1):
            GPIO.output(dec, dec2bin(a))   
            time.sleep(t / 255)
            
finally:
    GPIO.output(dec, 0)
    GPIO.cleanup()