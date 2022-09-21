from pico2d import *  # import * : 모든 기능을 가져옴 C++ using 같은 기능 
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
move = 'rect'
rect_move = 0
degree = 0

x=400
y=90

while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    
    if  move == 'rect' and rect_move == 0:
        x+=2
        if(x == 700):
            rect_move = 1
            rect_prev_move = 0
            continue
    elif move == 'rect' and rect_move == 1:
        y+=2
        if(y == 500):
            rect_move = 2
            rect_prev_move = 1
            continue
    elif move == 'rect' and rect_move == 2:
        x-=2
        if(x == 100):
            rect_move = 3
            rect_prev_move = 2
            continue
    elif move == 'rect' and rect_move == 3:
        y-=2
        if(y == 90):
            rect_move = 0
            rect_prev_move = 3
            continue
    delay(0.01)

close_canvas()
