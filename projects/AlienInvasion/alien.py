import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人并设置其初始资源"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #加载外星人并设置其rect属性
        self.image = pygame.image.load('images/ufo_001.png')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的精准位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def check_edges(self):
        """Return True, if an alien reches the screen edge."""
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right or the left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x