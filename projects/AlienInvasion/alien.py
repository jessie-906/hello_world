import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人并设置其初始资源"""
        super().__init__()
        self.screen = ai_game.screen
        #加载外星人并设置其rect属性
        self.image = pygame.image.load('images/ufo_1.png')
        self.rect = self.image.get_rect()
        #每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #储存外星人的精准水平位置
        self.x = float(self.rect.x)