import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
    def __init__(self):
        """初始化游戏并创键游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))   #创建窗口：set_mode()
        
        pygame.display.set_caption("Alien Invasion")                    #设置窗口标题：set_caption()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
                                                            
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self.check_events() 
            self.ship.update() 
            self._update_bullets()
            self.update_screen()
            self.clock.tick(60)
    
    def check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():                            #pygame.event.get()从 Pygame 的事件队列（event queue），
            if event.type == pygame.QUIT:                           #中取出所有未处理的事件，返回一个列表，
                sys.exit()                                          #每次调用后，队列会被清空（避免重复处理）
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)                         
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)          

    def check_keydown_events(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:                        
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_keyup_events(self,event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:    
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        #更新子弹位置
        self.bullets.update()

        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
           
        pygame.display.flip()   



if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()