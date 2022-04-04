import RPi.GPIO as GPIO
import time
import numpy as np

dec = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dec, GPIO.OUT)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT)
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
    return res


def adc(value):
    signal = dec2bin(value)
    GPIO.output(dec, signal)
    return signal


try:
    while True:
        value = 0
        for value in range(256):
            signal = adc(value)
            time.sleep(0.001)
            voltage = value / 255 * 3.3
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 0:
                print("alg1 = ", end='')
                print(voltage)
                break


        table = np.zeros((8, 8), dtype=int)
        for i1 in range(8):
            table[i1][i1] = 1
            GPIO.output(dec, table[i1].tolist())
            time.sleep(0.001)
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 1:
                table[:, i1] = 1
        print("alg2 = ", end='')
        print(3.3 * bin2dec(table[7]) / 255)
        GPIO.output(leds, dec2bin(value))
finally:
    GPIO.output(dec, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
