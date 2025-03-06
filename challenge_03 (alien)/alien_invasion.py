# import sys
# from time import sleep
# import pygame
# from settings import Settings
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien
# from boss import Boss

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Settings()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Jeff Saves The World")

#         self.stats = GameStats(self)
#         self.sb = Scoreboard(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()
        
#         self.boss = None  # Boss reference
#         self.boss_group = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play button.
#         self.play_button = Button(self, "Play")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)

#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game settings.
#             self.settings.initialize_dynamic_settings()

#             # Reset the game statistics.
#             self.stats.reset_stats()
#             self.sb.prep_score()
#             self.sb.prep_level()
#             self.sb.prep_ships()
#             self.game_active = True

#             # Get rid of any remaining bullets and aliens.
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship.
#             self._create_fleet()
#             self.ship.center_ship()

#             # Hide the mouse cursor.
#             pygame.mouse.set_visible(False)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
    
    
#         collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

#         if collisions:
#             for aliens in collisions.values():
#                 self.stats.score += self.settings.alien_points * len(aliens)
#             self.sb.prep_score()
#             self.sb.check_high_score()

#         # Check if all aliens are defeated and no boss is active
#         if not self.aliens and not self.boss:
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()
#             self.stats.level += 1
#             self.sb.prep_level()
#             self.spawn_boss()

#         # **New: Check for bullet-boss collisions**
#         if self.boss:
#             boss_hits = pygame.sprite.spritecollide(self.boss, self.bullets, True)
#             if boss_hits:
#                 self.boss.hp -= len(boss_hits) * 10  # Reduce boss HP by 10 per hit

#             if self.boss.hp <= 0:
#                     self.boss.kill()
#                     self.boss = None  # Remove the boss reference
#                     self.stats.score += 500  # Bonus points for defeating the boss
#                     self.sb.prep_score()
#                     self.sb.check_high_score()

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left, and update scoreboard.
#             self.stats.ships_left -= 1
#             self.sb.prep_ships()

#             # Get rid of any remaining bullets and aliens.
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship.
#             self._create_fleet()
#             self.ship.center_ship()

#             # Pause.
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen.
#         self._check_aliens_bottom()

#         # Update the boss if it exists.
#         if self.boss:
#             self.boss_group.update()

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _check_fleet_edges(self):
#         """Respond appropriately if any aliens have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break

#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def spawn_boss(self):
#         """Spawn the boss when all aliens are defeated."""
#         self.boss = Boss(self)
#         self.boss.speed = self.settings.ship_speed * 1.5
#         self.boss.hp = 100
#         self.boss_group.add(self.boss)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the boss if it exists.
#         if self.boss:
#             self.boss_group.draw(self.screen)
#             self._draw_boss_hp()

#         # Draw the score information.
#         self.sb.show_score()

#         # Draw the play button if the game is inactive.
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()

#     def _draw_boss_hp(self):
#         """Draw the boss health bar."""
#         if self.boss:
#             bar_width = 300
#             bar_height = 20
#             bar_x = (self.settings.screen_width - bar_width) // 2
#             bar_y = 10
#             hp_percentage = self.boss.hp / 100
#             hp_width = int(bar_width * hp_percentage)
#             pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
#             pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, hp_width, bar_height))


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game() 


# My code

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _start_game(self):         
        """Start a new game by resetting statistics and initializing game objects."""
        self.stats.reset_stats()
        self.game_active = True 
        self.ship.center_ship()
        self.aliens.empty() 
        self.bullets.empty()  
        self._create_fleet()  # Make a new fleet of aliens
        self.settings.initialize_dynamic_settings()

        # Reset the game statistics.
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Hide the mouse cursor once the game starts.
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game if the player clicks the Play button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_p and not self.game_active:
            self._start_game()  # Start the game when "P" is pressed

        if self.game_active:  # Only handle ship movement if the game is active
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()




# 'RONNY CODE'S 
# import pygame
# import random
# import math
# import os  # To check if sound files exist

# # Initialize pygame
# pygame.init()
# pygame.mixer.init()  # Initialize sound mixer

# # Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# YELLOW = (255, 255, 0)

# # Create screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Challenging Target Practice")

# # Load font
# font = pygame.font.Font(None, 36)

# # Load sounds (with error handling)
# def load_sound(filename):
#     if os.path.exists(filename):  # Check if file exists
#         return pygame.mixer.Sound(filename)
#     else:
#         print(f"Warning: {filename} not found. Sound will be disabled.")
#         return None

# shoot_sound = load_sound("shoot.wav")
# explosion_sound = load_sound("explosion.wav")

# # Load background
# bg = pygame.image.load("background.jpg") if os.path.exists("background.jpg") else None
# if bg:
#     bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# # Play button
# button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)

# # Ship
# ship = pygame.Rect(50, HEIGHT // 2 - 25, 50, 50)

# # Moving Target
# target = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 25, 50, 50)
# target_base_y = HEIGHT // 2 - 25  # Base position for wave movement
# target_speed = 3  # Initial speed (will increase)
# target_amplitude = 100  # Wave movement amplitude
# target_frequency = 0.05  # Speed of oscillation
# speed_increment = 0.2  # How much the target speeds up over time

# # Bullets
# bullets = []
# bullet_speed = 7

# # Game Variables
# lives = 3
# game_active = False
# frame_count = 0  # To control wave motion
# explosion_frames = 0  # Controls target flashing on hit
# time_survived = 0  # Counts time played to increase difficulty

# # Main game loop
# running = True
# while running:
#     # Draw background (if available)
#     if bg:
#         screen.blit(bg, (0, 0))
#     else:
#         screen.fill(WHITE)  # Use white background if no image

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and game_active:
#                 bullets.append(pygame.Rect(ship.x + 50, ship.y + 20, 10, 5))  # Fire bullet
#                 if shoot_sound:
#                     shoot_sound.play()
        
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button_rect.collidepoint(event.pos) and not game_active:
#                 # Restart game
#                 game_active = True
#                 lives = 3  # Reset lives
#                 bullets.clear()
#                 explosion_frames = 0
#                 target_speed = 3  # Reset target speed
#                 time_survived = 0  # Reset time

#     # Game logic (if active)
#     if game_active:
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP] and ship.y > 0:
#             ship.y -= 5
#         if keys[pygame.K_DOWN] and ship.y < HEIGHT - 50:
#             ship.y += 5

#         # Move target in a wave pattern
#         frame_count += 1
#         target.y = target_base_y + int(math.sin(frame_count * target_frequency) * target_amplitude)

#         # Increase difficulty over time
#         time_survived += 1
#         if time_survived % 300 == 0:  # Every 300 frames (~10 sec), increase speed
#             target_speed += speed_increment

#         # Move bullets
#         for bullet in bullets[:]:  # Iterate over copy of bullets list
#             bullet.x += bullet_speed
#             if bullet.x > WIDTH:  # Bullet missed
#                 bullets.remove(bullet)
#                 lives -= 1

#             if bullet.colliderect(target):  # Bullet hit target
#                 bullets.remove(bullet)
#                 explosion_frames = 10  # Trigger explosion effect
#                 if explosion_sound:
#                     explosion_sound.play()

#         # End game if out of lives
#         if lives <= 0:
#             game_active = False

#     # Draw everything
#     pygame.draw.rect(screen, BLUE, ship)  # Ship
#     if explosion_frames > 0:  # Target flashes yellow when hit
#         pygame.draw.rect(screen, YELLOW, target)
#         explosion_frames -= 1
#     else:
#         pygame.draw.rect(screen, RED, target)

#     for bullet in bullets:
#         pygame.draw.rect(screen, GREEN, bullet)  # Bullets

#     # Display lives
#     lives_text = font.render(f"Lives: {lives}", True, BLACK)
#     screen.blit(lives_text, (20, 20))

#     # Display Target Speed
#     speed_text = font.render(f"Speed: {round(target_speed, 1)}", True, BLACK)
#     screen.blit(speed_text, (20, 50))

#     # Display Play button if game is not active
#     if not game_active:
#         pygame.draw.rect(screen, BLACK, button_rect)
#         text = font.render("Play", True, WHITE)
#         screen.blit(text, (button_rect.x + 25, button_rect.y + 12))

#     # Update display
#     pygame.display.flip()

#     # Control frame rate
#     pygame.time.delay(30)

# pygame.quit()
