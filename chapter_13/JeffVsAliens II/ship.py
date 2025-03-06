import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # Ensure ai_game has a screen attribute
        self.settings = ai_game.settings  # Ensure ai_game has settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/jeff2.bmp')  # Ensure this path is correct
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
