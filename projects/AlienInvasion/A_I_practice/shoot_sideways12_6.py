import sys
import pygame

from s_s_ship12_6 import Settings,Ship,Bullet
 
class ShootSideways():
    def __init__(self):
        """初始化游戏并创建资源"""
        pygame.init
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption('ShootSideways')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
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

            self._update_bullets()
            self.ship.update(self.keys)
            self.update_screen()
            self.clock.tick(60)
    
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

    def update_screen(self):
        """创建并刷新屏幕,飞船和子弹"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
 
        pygame.display.flip()

if __name__ == '__main__':
    first_ss = ShootSideways()
    first_ss.run_game()