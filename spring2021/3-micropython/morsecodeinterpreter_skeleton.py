from machine import Pin
import utime
morse_code={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
            '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

dotLength=6000
dashLength=3*dotLength
wordChangeLength=7*dotLength
button1=Pin(2,Pin.IN,Pin.PULL_DOWN)
button2=Pin(5,Pin.IN,Pin.PULL_DOWN)

#FILL HERE:
#Define your own variables/setup, make sure to setup a way to gather input
while True:
    if(button2.value()==1):
        #FILL HERE:
        #Process and translate the input, (HINT: Use the dictionary above)

    x=button1.value()
    if (): #FILL HERE: Condition, Check the input (Hint: detect change in input rather than just the input itself)
        #FILL HERE:
        #Add a '.' a '-', change letters or change word

    else:
        #Any supporting code can go here
