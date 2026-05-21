import sys
import pygame
from pygame.sprite import Sprite
from time import sleep

class Settings:
    """A class to store all settings for Shooting game."""
    def __init__(self):
        """Initialize settings of the game."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.screen_color = (23,45,67)

        #Ship setttings
        self.ship_speed = 3.0
        self.ship_direction = 1

        #Bullets settings
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (255,0,0)
        self.bullet_speed = 2.5
        self.bullet_limit = 3

        #Alien settings
        self.alien_speed = 2.0
        self.alien_direction = 1


class Ship:
    """A class to manage the ship."""
    def __init__(self,shooting_game):
        self.screen = shooting_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = shooting_game.settings

        self.image = pygame.image.load('images/ship_002.png')
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def update(self):
        """Update ship's position.""" 
        self.y += self.settings.ship_speed * self.settings.ship_direction

        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_rect.bottom - self.rect.height:
            self.y = self.screen_rect.bottom - self.rect.height

        self.rect.y = self.y
    
    def center_ship(self):
        """Center the ship at the screen's midright."""
        self.rect.midright = self.screen_rect.midleft
        self.x = self.rect.x

    def blit(self):
        """Draw the ship at its specified position."""
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """A class to manage bullets fired by the ship."""
    def __init__(self,shooting_game):
        super().__init__()
        self.screen = shooting_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = shooting_game.settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                self.settings.bullet_height)
        self.rect.midleft = shooting_game.ship.rect.midleft

        self.x = float(self.rect.x)
    
    def update(self):
        """Move bullets to left."""
        self.x -= self.settings.bullet_speed
    
    def draw_bullet(self):
        """Draw bullets on the screen."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)


class Alien:
    """A class to manage alien."""
    def __init__(self,shoot_game):
        self.screen = shoot_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = shoot_game.settings

        self.image = pygame.image.load('images/ufo_001.png')
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)
    
    def update(self):
        """Update alien's position."""
        self.y += self.settings.alien_speed * self.settings.alien_directio
    
    def blit(self):
        self.screen.blit(self.image, self.rect)


class Shooting_game():
    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Shooting Game')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = Alien(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.keys = pygame.key.get_pressed()
            self._check_events()

            self._update_ship()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_ship(self):
        """Update the ship's position based on keyboard input."""
        if self.keys[pygame.K_UP]:
            self.settings.ship_direction = -1
            self.ship.update() 
        if self.keys[pygame.K_DOWN]:
            self.settings.ship_direction = 1
            self.ship.update()
    
    def _fire_bullet(self):
        """Create a new bullet, and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def Reset_resources(self):
        """Rset respurces: bullet, ship, alien."""
        #Derement bullet_limit by 1
        self.settings.bullet_limit -= 1

        #Center the ship and create a new alien
        self.ship.center_ship()
        self._create_alien()

        

    def _update_screen(self):
        """Updare images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.screen_color)
        self.ship.blit()
        self.alien.blit()

        pygame.display.flip()

if __name__ == '__main__':
    shooting_game = Shooting_game()
    shooting_game.run_game()