import sys
import pygame

from s_s_ship12_6 import Settings,Ship,Bullet
from s_s_alien13_5 import Alien

class ShootSideways():
    def __init__(self):
        """初始化游戏并创建资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption('ShootSideways')

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """游戏主循环"""
        while True:
            self.keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()

            self._update_alien()
            self._update_bullets()
            self.ship.update(self.keys)
            self.update_screen()
            self.clock.tick(60)
    
    def _create_fleet(self):
        """Create a fleet"""
        row_number = self.settings.row_number
        column_number = self.settings.column_number

        draw_width = self.settings.draw_width
        draw_height = self.settings.draw_height

        step_width = draw_width / row_number
        step_height = draw_height / column_number

        for r in range(row_number):
            for c in range(column_number):
                new_alien = Alien(self)
                new_alien.x = r * step_width
                new_alien.y = c * step_height

                new_alien.rect.x = new_alien.x
                new_alien.rect.y = new_alien.y
                self.aliens.add(new_alien)

    def check_fleet_edges(self):
        """Take approriate action if any alien reches the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Advance the aliens towards the shp."""
        for alien in self.aliens.sprites():
            alien.x += self.settings.fleet_advance_speed
            alien.rect.x = alien.x        
        #change fleet direction
        self.settings.fleet_direction *= -1

    def _update_alien(self):
        """Update the positions of all aliens in the fleet."""
        self.aliens.update()
        self.check_fleet_edges()

    def fire_bullet(self):
        """创建子弹"""
        new_bullet = Bullet(self)
        
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹位置并删除已消失的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if not self.aliens:
            #Clear existing bullets and recreate a new fleet
            self.bullets.empty()
            self._create_fleet()

    def update_screen(self):
        """创建并刷新屏幕,飞船和子弹"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    first_ss = ShootSideways()
    first_ss.run_game()