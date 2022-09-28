from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation.png')

frame = 0

# 여기를 채우세요.
y = 113
# 첫 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*0, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 13
    delay(0.1)
    get_events()



# 두 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 13
    delay(0.1)
    get_events()

# 세 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*2, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 9
    delay(0.1)
    get_events()

# 네 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*3, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 16
    delay(0.1)
    get_events()

# 다섯 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*4, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 14
    delay(0.1)
    get_events()

# 여섯 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*5, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 6
    delay(0.1)
    get_events()

# 일곱 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*6, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 15
    delay(0.1)
    get_events()

# 여덟 번째 애니메이션
for a in range(0, 200+1, 5):
    clear_canvas()
    character.clip_draw(frame * 103, y*7, 103, 113, 400, 300, 103, 113)
    update_canvas()
    frame = (frame + 1) % 16
    delay(0.1)
    get_events()

close_canvas()

