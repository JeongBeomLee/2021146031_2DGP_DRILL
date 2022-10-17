import pico2d
import play_state
import logo_state

# game main loop code
pico2d.open_canvas()
states = [logo_state, play_state]

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.01)
    state.exit()
pico2d.close_canvas()

# start_state = logo_state
# start_state.enter()
#
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()
#
# start_state = play_state
# start_state.enter()
#
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()
