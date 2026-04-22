import pygame
from pygame.sprite import Sprite

class Settings:
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (3,0,39)
        #飞船设置
        self.speed = 2.0
        #子弹设置
        self.bullet_color = (255,0,0)
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_speed = 3.0


class Ship:
    def __init__(self,s_s):
        """初始化飞船设置"""
        self.screen = s_s.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = s_s.settings

        self.image = pygame.image.load('images/ship_002.png')
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)
        
    def update(self,keys):
        """移动并刷新飞船位置"""
        if self.rect.top > 0:
            if keys[pygame.K_UP]:
                self.y -= self.settings.speed
        if self.rect.bottom < self.screen_rect.bottom:
            if keys[pygame.K_DOWN]:
                self.y += self.settings.speed  
        self.rect.y = self.y  

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    
class Bullet(Sprite):
    def __init__(self,s_s):
        """初始化子弹并创建其资源"""
        super().__init__()

        self.settings = s_s.settings
        self.ship = s_s.ship
        self.screen = s_s.screen
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midleft = self.ship.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        """向右移动子弹位置"""
       
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)