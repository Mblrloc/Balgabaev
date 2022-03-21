import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)
try:
    while True:
        a = int(input())
        p.start(a)
        voltage = (3.3 * a/ 200)
        print("V = " + "{:.2f}".format(voltage))
finally:
    p.stop(0)
    GPIO.output(22, 0)
    GPIO.cleanup()