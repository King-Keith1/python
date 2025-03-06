class Settings:

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        # ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 100
        
        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1