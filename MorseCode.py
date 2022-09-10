from ws2812 import WS2812
import utime
import machine
power = machine.Pin(11,machine.Pin.OUT)
power.value(1)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (200, 150, 0)
YELLOWGREEN = (100, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
VIOLET = (255, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (200, 0, 150)
WHITE = (255, 255, 255)
COLORS = (RED, YELLOW, ORANGE, YELLOWGREEN, GREEN, CYAN, BLUE, PURPLE, MAGENTA, WHITE)
led = WS2812(12,1)#WS2812(pin_num,led_count)
morsecode = "-."
letter = "a"
color = WHITE
def dah():
    led.pixels_fill(BLACK)
    led.pixels_show()
    utime.sleep(0.2)
    led.pixels_fill(color)
    led.pixels_show()
    utime.sleep(0.5)   
    led.pixels_fill(BLACK)
    led.pixels_show()
    utime.sleep(0.2)
    
def dih():
    led.pixels_fill(BLACK)
    led.pixels_show()
    utime.sleep(0.2)
    led.pixels_fill(color)
    led.pixels_show()
    utime.sleep(0.2)   
    led.pixels_fill(BLACK)
    led.pixels_show()
    utime.sleep(0.2)
    
def morseCode():
    if (morsecode == ".-"):
        letter = 'a'
    elif (morsecode == "-..."):
        letter = 'b'
    elif (morsecode == "-.-."):
        letter = 'c'
    elif (morsecode == "-.."):
        letter = 'd'
    elif (morsecode == "."):
        letter = 'e'
    elif (morsecode == "..-."):
        letter = 'f'
    elif (morsecode == "--."):
        letter = 'g'
    elif (morsecode == "...."):
        letter = 'h'
    elif (morsecode == ".."):
        letter = 'i'
    elif (morsecode == ".---"):
        letter = 'j'
    elif (morsecode == "-.-"):
        letter = 'k'
    elif (morsecode == ".-.."):
        letter = 'l'
    elif (morsecode == "--"):
        letter = 'm'
    elif (morsecode == "-."):
        letter = 'n'
    elif (morsecode == "---"):
        letter = 'o'
    elif (morsecode == ".--."):
        letter = 'p'
    elif (morsecode == "--.-"):
        letter = 'q'
    elif (morsecode == ".-."):
        letter = 'r'
    elif (morsecode == "..."):
        letter = 's'
    elif (morsecode == "-"):
        letter = 't'
    elif (morsecode == "..-"):
        letter = 'u'
    elif (morsecode == "...-"):
        letter = 'v'
    elif (morsecode == ".--"):
        letter = 'w'
    elif (morsecode == "-..-"):
        letter = 'x'
    elif (morsecode == "-.--"):
        letter = 'y'
    elif (morsecode == "--.."):
        letter = 'z'
    elif (morsecode == ".----"):
        letter = '1'
    elif (morsecode == "..---"):
        letter = '2'
    elif (morsecode == "...--"):
        letter = '3'
    elif (morsecode == "....-"):
        letter = '4'
    elif (morsecode == "....."):
        letter = '5'
    elif (morsecode == "-...."):
        letter = '6'
    elif (morsecode == "--..."):
        letter = '7'
    elif (morsecode == "---.."):
        letter = '8'
    elif (morsecode == "----."):
        letter = '9'
    elif (morsecode == "-----"):
        letter = '10'
    else ():
        letter = " "
        
    def morseAlphabet():
    if (letter == 'a'):
        morsecode = ".-"
    elif (letter == 'b'):
        morsecode = "-..."
    elif (letter == 'c'):
        morsecode = "-.-."
    elif (letter == 'd'):
        morsecode = "-.."
    elif (letter == 'e'):
        morsecode = "."
    elif (letter == 'f'):
        morsecode = "..-."
    elif (letter == 'g'):
        morsecode = "--."
    elif (letter == 'h'):
        morsecode = "...."
    elif (letter == 'i'):
        morsecode = ".."
    elif (letter == 'j'):
        morsecode = ".---"
    elif (letter == 'k'):
        morsecode = "-.-"
    elif (letter == 'l'):
        morsecode = ".-.."
    elif (letter == 'm'):
        morsecode = "--"
    elif (letter == 'n'):
        morsecode = "-."
    elif (letter == 'o'):
        morsecode = "---"
    elif (letter == 'p'):
        morsecode = ".--."
    elif (letter == 'q'):
        morsecode = "--.-"
    elif (letter == 'r'):
        morsecode = ".-."
    elif (letter == 's'):
        morsecode = "..."
    elif (letter == 't'):
        morsecode = "-"
    elif (letter == 'u'):
        morsecode = "..-"
    elif (letter == 'v'):
        morsecode = "...-"
    elif (letter == 'w'):
        morsecode = ".--"
    elif (letter == 'x'):
        morsecode = "-..-"
    elif (letter == 'y'):
        morsecode = "-.--"
    elif (letter == 'z')
    morsecode = "--.."

while True:
    
     userinput = input()
     
    
    
    
     


   
    
  

