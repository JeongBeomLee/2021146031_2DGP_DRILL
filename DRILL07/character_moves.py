from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('CupheadIdle.png')

frame = 0

# 여기를 채우세요.
# 첫 번째 애니메이션
for a in range(0, 200+1, 1):
    clear_canvas()
    character.clip_draw(frame * 134, 0, 134, 209, 400, 300, 134, 209)
    update_canvas()
    frame = (frame + 1) % 10
    delay(0.01)
    get_events()

close_canvas()
