from pico2d import *
import os

# 이벤트 정의
# RD = 0, LD = 1, RU = 2, LU = 3
RD, LD, RU, LU, aD, aU, TIMER = range(7)

# 키 입력 확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP,   SDLK_RIGHT): RU,
    (SDL_KEYUP,   SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a)    : aD,
    (SDL_KEYUP,   SDLK_a)    : aU,
}

class IDLE:
    @staticmethod
    def enter(player, event): # 상태에 들어갈 때 행하는 액션
        # print('ENTER IDLE')
        player.dir = 0
        player.timer = 100
    
    @staticmethod
    def exit(player): # 상태에서 나갈 때 행하는 액션
        # print('EXIT IDLE')
        pass
    
    @staticmethod
    def do(player): # 상태에 있을 때 지속적으로 행하는 행위
        player.frame = (player.frame + 1) % 8
        player.timer -= 1

        if player.timer == 0:
            player.add_event(TIMER) # 객체지항젹인 방법
    
    @staticmethod
    def draw(player):
        if player.face_dir == 5:
            player.image.clip_draw(player.frame * 100, 300, 100, 100, player.x, player.y)
        else:
            player.image.clip_draw(player.frame * 100, 200, 100, 100, player.x, player.y)
            
class RUN:
    @staticmethod
    def enter(player, event): # 상태에 들어갈 때 행하는 액션, 뭘 근거로? 어떤 키가 눌렸기 때문에
        # 키 이벤트 정보가 필요하다.
        # print('ENTER RUN')
        if event == RD:
            player.dir += 5
        elif event == LD:
            player.dir -= 5
        elif event == RU:
            player.dir -= 5
        elif event == LU:
            player.dir += 5
    
    @staticmethod
    def exit(player): # 상태에서 나갈 때 행하는 액션
        # print('EXIT RUN')
        player.face_dir = player.dir
    
    @staticmethod
    def do(player): # 상태에 있을 때 지속적으로 행하는 행위
        player.frame = (player.frame + 1) % 8

        # 벽 밖으로 나가지 못 하도록
        player.x += player.dir
        player.x = clamp(0, player.x, 800)

    
    @staticmethod
    def draw(player):
        if player.dir == -5:
            player.image.clip_draw(player.frame * 100, 0, 100, 100, player.x, player.y)
        else:
            player.image.clip_draw(player.frame * 100, 100, 100, 100, player.x, player.y)


class SLEEP:
    @staticmethod
    def enter(player, event):  # 상태에 들어갈 때 행하는 액션
        # print('ENTER SLEEP')
        player.dir = 0

    @staticmethod
    def exit(player):  # 상태에서 나갈 때 행하는 액션
        # print('EXIT IDLE')
        pass

    @staticmethod
    def do(player):  # 상태에 있을 때 지속적으로 행하는 행위
        pass

    @staticmethod
    def draw(player):
        # print('DRAW SLEEP')
        if player.face_dir == -5:
            # player.image.clip_draw(player.frame * 100, 300, 100, 100, player.x, player.y)
            player.image.clip_composite_draw(100, 200, 100, 100, -3.141592 / 2, '', player.x + 25, player.y - 25, 100, 100)
        else:
            # player.image.clip_draw(player.frame * 100, 200, 100, 100, player.x, player.y)
            player.image.clip_composite_draw(100, 300, 100, 100, 3.141592 / 2, '', player.x - 25, player.y - 25, 100, 100)


class AUTO_RUN:
    @staticmethod
    def enter(player, event):  # 상태에 들어갈 때 행하는 액션, 뭘 근거로? 어떤 키가 눌렸기 때문에
        # 키 이벤트 정보가 필요하다.
        # print('ENTER RUN')
        player.dir = player.face_dir
        pass

    @staticmethod
    def exit(player):  # 상태에서 나갈 때 행하는 액션
        # print('EXIT RUN')
        player.face_dir = player.dir
        player.dir = 0

    @staticmethod
    def do(player):  # 상태에 있을 때 지속적으로 행하는 행위
        player.frame = (player.frame + 1) % 8

        # 벽 밖으로 나가지 못 하도록
        player.x += player.dir
        if player.x <= 0:
            player.dir = 5
        elif player.x >= 800:
            player.dir = -5
        # player.x = clamp(0, player.x, 800)

    @staticmethod
    def draw(player):
        if player.dir == -5:
            player.image.clip_draw(player.frame * 100, 0, 100, 100, player.x, player.y + 25, 200, 200)
        else:
            player.image.clip_draw(player.frame * 100, 100, 100, 100, player.x, player.y + 25, 200, 200)


next_state = {
    SLEEP:    {RU: RUN,      LU: RUN,      RD: RUN,  LD: RUN,  aD: SLEEP,    aU: SLEEP, TIMER: SLEEP},
    IDLE:     {RU: RUN,      LU: RUN,      RD: RUN,  LD: RUN,  aD: AUTO_RUN, aU: IDLE, TIMER: SLEEP},
    RUN:      {RU: IDLE,     LU: IDLE,     RD: IDLE, LD: IDLE, aD: AUTO_RUN, aU: RUN},
    AUTO_RUN: {RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN,  LD: RUN,  aD: IDLE,     aU: AUTO_RUN}
}

class Boy:
    def __init__(self):
        self.x, self.y = 1, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 5
        self.image = load_image('animation_sheet.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        
    def update(self):
        os.system('cls')
        print('dir : %d' %self.dir)
        print('face_dir : %d' %self.face_dir)
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
    
    def add_event(self, event):
        self.event_que.insert(0, event)
        
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    
