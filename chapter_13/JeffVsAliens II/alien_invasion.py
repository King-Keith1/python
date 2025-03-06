import sys
from time import sleep

import pygame

from boss import Boss
from bullet import Bullet
from alien import Alien
from ship import Ship
from settings import Settings
from game_stats import GameStats

class AlienInvasion:
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
        self.boss = None  # Boss reference
        self.boss_group = pygame.sprite.Group()
        
        self._create_fleet()
        
        self.game_active = True

    def run_game(self):
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if self.boss:
            boss_hits = pygame.sprite.spritecollide(self.boss, self.bullets, True)
            if boss_hits:
                self.boss.hp -= 10
                if self.boss.hp <= 0:
                    self.boss_group.remove(self.boss)
                    self.boss = None

        if not self.aliens and not self.boss:
            self.bullets.empty()
            self.spawn_boss()

    def _ship_hit(self):
        """Respond to the ship being hit."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()
    
        if self.boss:
            self.boss_group.update()

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def spawn_boss(self):
        """Spawn the boss when all aliens are defeated."""
        self.boss = Boss(self)
        self.boss.speed = self.settings.ship_speed * 1.5
        self.boss.hp = 100
        self.boss_group.add(self.boss)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        if self.boss:
            self.boss_group.draw(self.screen)
            self._draw_boss_hp()

        pygame.display.flip()

    def _draw_boss_hp(self):
        """Draw the boss health bar."""
        if self.boss:
            bar_width = 300
            bar_height = 20
            bar_x = (self.settings.screen_width - bar_width) // 2
            bar_y = 10
            hp_percentage = self.boss.hp / 100
            hp_width = int(bar_width * hp_percentage)
            pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, hp_width, bar_height))

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()