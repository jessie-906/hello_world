import sys
import pygame
from pygame.sprite import Sprite

class Settings():
    """A class to store all settings for the game."""
    def __init__(self):
        """Initialise the settings of the game."""
        self.screen_width = 1500
        self.screen_height = 1000
        self.screen_color = (0,0,0)

        self.row_number = 10
        self.column_number = 6

        self.margin_x = 100
        self.margin_y = 80

        self.raindrop_drop_speed = 5

class Raindrop(Sprite):
    def __init__(self,R_Game):
        """Initialise the raindrop and set the initial resources."""
        super().__init__()
        self.screen = R_Game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = R_Game.settings

        self.image = pygame.image.load('A_I_practice/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop to the bottom."""
        self.y += self.settings.raindrop_drop_speed 
        self.rect.y = self.y

class RaindropsGame():
    def __init__(self):
        """Initialise the game and create resources."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Raindrops')

        self.raindrops = pygame.sprite.Group()
        self.create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.screen.fill(self.settings.screen_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_raindrops()
            self.raindrops.draw(self.screen)
            self.clock.tick(60)
            pygame.display.flip()    

    def create_rain(self):
        """create a certain number of raindrops to fill the screen."""
        row_number =  self.settings.row_number
        column_number = self.settings.column_number

        margin_x = self.settings.margin_x
        margin_y = self.settings.margin_y

        draw_width = self.screen_rect.width - 2 * margin_x
        draw_height = self.screen_rect.height - 2 * margin_y

        step_width = draw_width / (row_number - 1)
        step_height = draw_height / (column_number - 1)

        for c in range(column_number):
            for r in range(row_number):
                new_raindrop = Raindrop(self)

                new_raindrop.x = margin_x + r * step_width  
                new_raindrop.x -= new_raindrop.rect.width / 2
                new_raindrop.y = margin_y + c * step_height
                new_raindrop.y -= new_raindrop.rect.height / 2

                new_raindrop.rect.x = new_raindrop.x
                new_raindrop.rect.y = new_raindrop.y

                self.raindrops.add(new_raindrop)

        
    def continuous_raindrops(self):
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.top >= self.screen_rect.bottom:
                raindrop.y = self.settings.margin_y
                raindrop.y -= raindrop.rect.height 
                raindrop.rect.y = raindrop.y
        
    def _update_raindrops(self):
        self.raindrops.update()
        self.continuous_raindrops()
        
if __name__ == '__main__':
    """Creare a game instance and run the game."""
    raindrop = RaindropsGame()
    raindrop.run_game()