import RPi.GPIO as GPIO
import time
import numpy as np

dec = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dec, GPIO.OUT)

comp = 4
troyka = 17

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def bin2dec(arr):
    res = 0
    counter = 128
    for i1 in range(8):
        res += arr[i1] * counter
        counter /= 2

def adc(value):
    signal = dec2bin(value)
    GPIO.output(dec, signal)
    return signal

try:
    while True:
        time1 = int(time.time() * 1000)
        for value in range(256):
            signal = adc(value)
            time.sleep(0.001)
            voltage = value / 255 * 3.3
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 0:
                print(voltage)
                break
        time2 = int(time.time() * 1000)
        table = numpy.zeros((8, 8))
        for i1 in range(8):
            table[i1][i1] = 1
            if comparatorValue == 1:
                table[:][i1] = 1
            time.sleep(0.001)
        print(3.3 * bin2dec(table[7] / 255))
        time3 = int(time.time() * 1000)
        print("time for alg1= " + str(time2 - time1))
        print("time for alg2= " + str(time3 - time2))

finally:
    GPIO.output(dec, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()