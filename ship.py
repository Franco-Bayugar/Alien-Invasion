import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship img and get its Rect
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        
        #start new ship and the bottom-center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store a float for the x position of the ship
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #update the ship pos based on Flag
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #update rect object
        self.rect.x = self.x 
    
    def blitme(self):
        #draw the ship and the current location
        self.screen.blit(self.image, self.rect)
    
            