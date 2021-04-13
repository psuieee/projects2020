from machine import Pin
import utime

code_string='101' #can change the string, or use this as an input value
led1=Pin(21,Pin.OUT) #display input bit
led2=Pin(20,Pin.OUT) #display lock open/close
button1=Pin(2,Pin.IN,Pin.PULL_DOWN) #set input bit
button2=Pin(5,Pin.IN,Pin.PULL_DOWN) #confirm input bit
button3=Pin(8,Pin.IN,Pin.PULL_DOWN) #confirm input

bit=0
input_string=''
led1.off()
led2.off()
while True:
    if(button3.value()==1):
        break
    elif(button2.value()==1):
        input_string=input_string+str(bit)
        led1.off()
        bit=0
        utime.sleep(0.4)
    elif(button1.value()==1):
        led1.toggle()
        bit=1-bit
        utime.sleep(0.4)
if(input_string==code_string):
    led2.on()