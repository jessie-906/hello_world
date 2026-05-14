import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,shoot_game):
        """Initialize ufo and create resources."""
        super().__init__()
        self.screen = shoot_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = shoot_game.settings

        self.image = pygame.image.load('images/ufo_001.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if an alien reches screen edge."""
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

    def update(self):
        """Move the aliens to the top or the bottom."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y