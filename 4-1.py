import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dec = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dec, GPIO.OUT)
try:
    while True:
        a = input()

        if (a == 'q'):
            print("Завершение работы")
            exit(0)
        else:
            try:
                num = float(a)
            except ValueError:
                print("Введите десятичное число")
                continue
        if (abs(float(a) % 1) >= 1e-10):
            print("Нужно целое число")
            continue
        num = int(a)
        if (num > 255):
            print("Значение превышает диапазон 8-разрядного ЦАП")
            continue  
        elif (num < 0):
            print("Отрицательные значения недопустимы")
            continue
        voltage = num * 3.3/ 255
        print("V = " + "{:.2f}".format(voltage))
        GPIO.output(dec, dec2bin(num))    
finally:
    GPIO.output(dec, 0)
    GPIO.cleanup()