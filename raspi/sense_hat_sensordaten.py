from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

sense.clear()

sense.set_rotation(r=180)

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

letterColor = v

rainbow = [
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,r,r,o,o,r,r,e,
r,o,o,y,y,o,o,r,
o,y,y,g,g,y,y,o,
y,g,g,b,b,g,g,y,
b,b,b,i,i,b,b,b,
b,i,i,v,v,i,i,b
]

while True:

    sense.set_pixels(rainbow)

    sleep(4)

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    msg = '{:.1f}'.format(t)

    letterColor = (randint(0,255), randint(0,255), randint(0,255))

    for letter in msg:
        sense.show_letter(letter, letterColor)
        sleep(1.5)