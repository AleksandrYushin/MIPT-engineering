import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abs():
    a_1=0
    for i in range(7, -1, -1):
        a=1
        for j in range(i):
            a = a*2
        a_1=a_1+a
        number = decimal2binary(a_1)
        GPIO.output(dac, number)
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            a_1=a_1-a
    return a_1

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]
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
