import sys

import pygame

from settings import Settings

class AlienInvasion():
    def __init__(self):
        """初始化游戏并创键游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))   #创建窗口：set_mode()
        pygame.display.set_caption("Alien Invasion")                    #设置窗口标题：set_caption()

        #设置背景色
        self.bg_color = (230,230,230)
                                                            
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #侦听键盘和鼠标事件
            for event in pygame.event.get():                            #pygame.event.get()从 Pygame 的事件队列（event queue），
                if event.type == pygame.QUIT:                           #中取出所有未处理的事件，返回一个列表，
                    sys.exit()                                          #每次调用后，队列会被清空（避免重复处理）

            #每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)

            #让最近绘制的屏幕可见
            pygame.display.flip()                                        #刷新屏幕：flip() 或 update()
            self.clock.tick(60)

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()