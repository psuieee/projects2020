from machine import Pin
import utime

code_string='101' #can change the string, or use this as an input value
led1=Pin(21,Pin.OUT) #display input bit
led2=Pin(20,Pin.OUT) #display lock open/close
button1=Pin(2,Pin.IN,Pin.PULL_DOWN) #set input bit
button2=Pin(5,Pin.IN,Pin.PULL_DOWN) #confirm input bit
button3=Pin(8,Pin.IN,Pin.PULL_DOWN) #confirm input

led1.off()
led2.off()

#FILL HERE:
#Define your own variables/setup, make sure to setup a way yo gather input

while True:
    if(button3.value()==1):
        break
    elif(button2.value()==1):
        #FILL HERE:
        #store the current state of the input bit in conjunction with all of the previous input bits

        utime.sleep(0.4)
    elif(button1.value()==1):
        #FILL HERE:
        #toggle led and state of current input bit

        utime.sleep(0.4)

#FILL HERE:
#Turn on the led if the input bits entered matches the code bits, to signify that the lock has been 'opened'
