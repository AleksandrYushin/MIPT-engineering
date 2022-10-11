import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abs():
    number = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(256):
        number = decimal2binary(i)
        GPIO.output(dac, number)
        time.sleep(0.005)
        y = GPIO.input(comp)
        if y==0:
            return i

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
try:
    while True:
        n = abs()
        if n!=0:
            print (n, "{:.3f}".format(3.3*n/256))        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
