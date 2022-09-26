from pico2d import *  # import * : 모든 기능을 가져옴 C++ using 같은 기능 
from math import *


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
move = 'rect'
rect_move = 0
degree = 0

x=400
y=90
ceta = 0;

while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=300*cos(ceta) + 400
    y=300*sin(ceta) + 90
    ceta=ceta+1
    delay(0.01)

close_canvas()
