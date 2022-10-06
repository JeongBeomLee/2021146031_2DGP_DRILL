from pico2d import *

def events():
    global running
    global LR, UD
    global direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # 종료
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                LR += 1
                direction = RIGHT
            elif event.key == SDLK_LEFT:
                LR -= 1
                direction = LEFT
            elif event.key == SDLK_UP:
                UD += 1
            elif event.key == SDLK_DOWN:
                UD -= 1
            elif event.key == SDLK_ESCAPE: # ESC키
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                LR -= 1
            elif event.key == SDLK_LEFT:
                LR += 1
            elif event.key == SDLK_UP:
                UD -= 1
            elif event.key == SDLK_DOWN:
                UD += 1

    pass

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
TUK_GROUND = load_image('TUK_GROUND.png')

running = True
x = 400
y = 300
frame = 0
#
LR = 0
UD = 0

#
RIGHT = 0
LEFT = 1
direction = RIGHT

while running:
    clear_canvas()
    #grass.draw(400, 30)
    TUK_GROUND.clip_draw(0, 0, TUK_GROUND.w, TUK_GROUND.h, 400, 300 , get_canvas_width(), get_canvas_height())

    if(LR == 1): # 오른쪽 이동
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif(LR == -1): # 왼쪽 이동
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif(UD == 1): # 위로 이동
        if(direction == LEFT):
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
        if(direction == RIGHT):
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif(UD == -1): # 아래로 이동
        if (direction == LEFT):
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
        if (direction == RIGHT):
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif(LR == 0 and UD == 0): # 가만히
        if (direction == LEFT):
            character.clip_draw(0, 200, 100, 100, x, y)
        if (direction == RIGHT):
            character.clip_draw(0, 300, 100, 100, x, y)

    update_canvas() # 버퍼변경

    events()
    frame = (frame + 1) % 8
    x += LR * 5
    y += UD * 5
    delay(0.01)

close_canvas()