import sys
import pygame
from pygame.sprite import Sprite

class Settings():
    def __init__(self):
        """Initialise the settings of the game"""
        self.screen_width = 1500
        self.screen_height = 1000
        self.screen_color = (0,0,0)
        self.clock_tick = 60

        #Settings of the stars
        self.row_number = 10
        self.column_number = 8

        self.margin_x = 100
        self.margin_y = 80



class Star(Sprite):
    def __init__(self,Star):
        """Initialise the star and create resource"""
        super().__init__()
        self.screen = Star.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('A_I_practice/star_001.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class NeatlyArrangedStars():
    def __init__(self):
        """Initialise the game and creat resource"""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
       
        pygame.display.set_caption('Neatly Arranged Stars')
        
        self.stars = pygame.sprite.Group()
        self.create_stars()
        

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.screen.fill(self.settings.screen_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.stars.draw(self.screen)
            self.clock.tick(self.settings.clock_tick)
            pygame.display.flip()

    def create_stars(self):
        """Create a row of neatly arranged stars with even spacing"""
        #Set the number of stars per row and per column
        row_number = self.settings.row_number
        column_number = self.settings.column_number

        #Set horizontal and vertical margins to prevent stars from touching the edges
        margin_x = self.settings.margin_x
        margin_y = self.settings.margin_y

        #Calculate the effective drawing area
        draw_width = self.screen_rect.width - margin_x * 2
        draw_height = self.screen_rect.height - margin_y * 2

        #Calculate the width and height of each gaps
        #With N stars ,there are N-1 gaps
        step_width = draw_width / (row_number - 1)
        step_height = draw_height / (column_number - 1)

        for c in range(column_number):
            for r in range(row_number):    
                new_star = Star(self)
                #Coordinatte = starting margin + (index * step_size)
                new_star.x = margin_x + r * step_width
                new_star.y = margin_y + c * step_height
                #Center the star: subtract half of the star's own width
                new_star.rect.x = new_star.x - new_star.rect.width / 2
                new_star.rect.y = new_star.y - new_star.rect.width / 2
                self.stars.add(new_star)


if __name__ == '__main__':
    stars = NeatlyArrangedStars()
    stars.run_game()
