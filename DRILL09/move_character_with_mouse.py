from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
start_x, start_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = start_x, start_y
arrow_x, arrow_y = x, y
frame = 0
hide_cursor()

t = 0
left = 0
right = 1
direction = right
def reset_world():
    global arrow_x, arrow_y
    global start_x, start_y
    global t
    arrow_x, arrow_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    t = 0
    start_x, start_y = x, y
    pass

def update_world():
    global x, y
    global t
    t += 0.001
    x = (1 - t) * start_x + t * arrow_x
    y = (1 - t) * start_y + t * arrow_y

    if t >= 1.0:
        reset_world()

def decide_direction():
    global direction
    if arrow_x < x:
        direction = left
    elif arrow_x > x:
        direction = right

reset_world()
while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(arrow_x, arrow_y)
    decide_direction()
    character.clip_draw(frame * 100, 100 * direction, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




