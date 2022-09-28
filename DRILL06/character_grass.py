from pico2d import *  # import * : 모든 기능을 가져옴 C++ using 같은 기능 
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    pass

def bottom_line():
    for x in range(50,750+1,10):
        render_all(x,90)
    pass

def right_line():
    for y in range(90,550+1,10):
        render_all(750,y)
    pass

def top_line():
    for x in range(750,50-1,-10):
        render_all(x,550)
    pass

def left_line():
    for y in range(550,90-1,-10):
        render_all(50,y)
    pass

def run_rectangle():
    bottom_line()
    right_line()
    top_line()
    left_line()
    pass

def run_ellipse():
    cx,cy,r=400,300,200
    for deg in range(0,360,5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        render_all(x,y)
    pass

while(1):
    run_rectangle()
    run_ellipse()

close_canvas()
