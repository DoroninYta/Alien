class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed = 0.8
        self.fleet_drop_speed = 50 #down speed
        self.fleet_direction = 1 #1 or -1 right or left

