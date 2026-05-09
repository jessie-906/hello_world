import sys
import pygame
import random
from pygame.sprite import Sprite

class Settings():
    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 1000
        self.screen_color = (0,0,0)
        self.stars_path = ['A_I_practice/star_001.png',
            'A_I_practice/star_002.png']

        self.number_star = 50
        self.x_min = 0
        self.x_max = 1500
        self.y_min = 0
        self.y_max = 1000


class Star(Sprite):
    def __init__(self,RS,image_path):
        super().__init__()
        self.screen = RS.screen
        self.screen_rect = self.screen.get_rect()

        self.image = RS.assets[image_path]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class RandomStars():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.stars_path = self.settings.stars_path

        self.assets = {}
        for path in self.stars_path:
            image = pygame.image.load(path)
            self.assets[path] = image

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Random Stars')

        self.stars = pygame.sprite.Group()
        self.create_random_stars()

    def run_game(self):
        while True:
            self.screen.fill(self.settings.screen_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.stars.draw(self.screen)
            self.clock.tick(60)
            pygame.display.flip()
    
    def create_random_stars(self):
        while len(self.stars) < self.settings.number_star:
            image_path = random.choice(self.stars_path)
            new_star = Star(self,image_path)

            new_star.x = random.randint(
                self.settings.x_min,
                self.settings.x_max - new_star.rect.width
            )
            new_star.y = random.randint(
                self.settings.y_min,
                self.settings.y_max - new_star.rect.height
            )

            new_star.rect.x = new_star.x
            new_star.rect.y = new_star.y
            
            self.stars.add(new_star)

if __name__ == '__main__':
    random_star = RandomStars()
    random_star.run_game()