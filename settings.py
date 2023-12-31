class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_heigth = 600
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 8.0
        
        # Bullet settings
        self.bullet_speed = 16.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 2