from pico2d import *
import game_world, game_framework
import random

# Boy Run Speed
PIXEL_PER_METER = (50.0 / 0.1) # 10 pixel 30 cm
RUN_SPEED_KMPH  = 45.0 # Km / Hour
RUN_SPEED_MPM   = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS   = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS   = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(350, 550)
        self.frame = 0
        self.dir = 1
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        
        if self.x <= 25:
            self.dir = 1
        elif self.x >= 1600 - 25:
            self.dir -= 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*184, 338, 184, 168, 0, 'h', self.x, self.y, 50, 50)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame)*184, 338, 184, 168, 0, 'n', self.x, self.y, 50, 50)

