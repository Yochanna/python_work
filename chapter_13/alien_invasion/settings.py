class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 1.5

        # Bullets
        self.bullet_speed = 1.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction: 1 = right, -1 = left
        self.fleet_direction = 1
