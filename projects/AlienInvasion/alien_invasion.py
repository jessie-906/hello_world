import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))   #创建窗口：set_mode()
        
        pygame.display.set_caption("Alien Invasion")                    #设置窗口标题：set_caption()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
                                                            
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events() 
            self.ship.update() 
            self._update_bullets()
            self._update_alien()
            self._update_screen()
            self.clock.tick(60)
    
    def check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():                            #pygame.event.get()从 Pygame 的事件队列（event queue），
            if event.type == pygame.QUIT:                           #中取出所有未处理的事件，返回一个列表，
                sys.exit()                                          #每次调用后，队列会被清空（避免重复处理）
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)                         
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)          

    def check_keydown_events(self,event):
        """Respond to KRYDOWN events"""
        if event.key == pygame.K_RIGHT:                        
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_keyup_events(self,event):
        """Respond to KEYUP events"""
        if event.key == pygame.K_RIGHT:    
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #remove corresponding bullets and aliens.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
                
        if not self.aliens:
            #Clear existing bullets and recreate a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Create a row of aliens, filling the screen until no more space remains
        #Set the spacing between aliens to equal one alien's width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        current_x, current_y = alien_width, alien_height
        while current_y <= (self.settings.screen_height - 3 * alien_height):
            while current_x <= (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #after adding a row of aliens, reset x and increment y.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self,x_position,y_position):
        """Create an alien and add it to the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        """Take appropriate action if any alien reaches the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down and change its direction."""
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y
        self.settings.fleet_direction *= -1

    def _update_alien(self):
        """Update the positions of all  aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()   



if __name__ == '__main__':
    #create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()