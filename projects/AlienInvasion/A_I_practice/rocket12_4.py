import pygame

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 1000
        self.bg_color = (255,255,255)
        self.rocket_speed = 2.0

class Rocket():
    def __init__(self,r_g):
        """初始化火箭并设置其位置"""
        
        self.screen = r_g.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = r_g.settings

        self.image = pygame.image.load('A_I_practice/cohete_off.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        """响应键盘和鼠标事件移动飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= 2.0
        if self.moving_up and self.rect.top > 0:
            self.y -= 2.0
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 2.0
        self.rect.x = self.x
        self.rect.y = self.y

    
    