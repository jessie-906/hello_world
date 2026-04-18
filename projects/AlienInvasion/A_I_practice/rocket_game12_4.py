import sys
import pygame

from rocket12_4 import Settings,Rocket

class RocketGame():
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.rocket = Rocket(self)
        
    def run_game(self):
        """运行游戏主循环,加载游戏资源"""
        while True:                                     #方法的顺序一定要正确，
            self.screen.fill(self.settings.bg_color)             #先填充屏幕fill，
            self.check_events()                         
            self.rocket.update()                        
            self.rocket.blitme()                        #后绘制飞船blitne，
            pygame.display.flip()                       #最后刷新屏幕flip
            self.clock.tick(60)
    def check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True    
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()  

    def check_keyup_events(self,event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False    
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

if __name__ == '__main__':
    """创建实例"""
    rg = RocketGame()
    rg.run_game()

    