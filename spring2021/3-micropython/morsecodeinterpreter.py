from machine import Pin
import utime
morse_code={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
            '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

dotLength=6000
dashLength=3*dotLength
wordChangeLength=7*dotLength

string=[[]]
button1=Pin(2,Pin.IN,Pin.PULL_DOWN)
button2=Pin(5,Pin.IN,Pin.PULL_DOWN)
previous=0
count=[0,0]
while True:
    if(button2.value()==1):
        x=""
        for i in string:
            for j in i:
                if j in morse_code:
                    x+=morse_code[j]
            x+=" "
            
        print("Decoded string: ",x)
        previous=0
        count=[0,0]
        string=[[]]
        utime.sleep(0.4)
    x=button1.value()
    if (x!=previous):
        if(count[previous]>dotLength and count[previous]<dashLength):
            if previous==1:
                string[-1][-1]+='.'
        elif(count[previous]>dashLength and count[previous]<wordChangeLength):
            if previous==0:
                string[-1].append('')
            elif previous==1:
                string[-1][-1]+='-'
        elif(count[previous]>wordChangeLength):
            string.append([''])
        print(string)
        count[x]+=1
        count[previous]=0
        previous=x
    else:
        count[x]+=1
    