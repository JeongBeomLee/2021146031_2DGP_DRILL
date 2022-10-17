from pico2d import *
import game_framework
import play_state
import title_state

# fill here
#running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():
    # fill here
    global logo_time
    #global running
    delay(0.01)
    logo_time += 0.01
    if logo_time > 1.1:
        logo_time = 0
        #running = False
        game_framework.change_state(title_state)
    pass

def draw():
    # fill here
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()





