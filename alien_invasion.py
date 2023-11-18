import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet



class AlienInvasion:
    #constructor
    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        #Group that holds the bullets
        self.bullets = pygame.sprite.Group()
        #Refreshing rate
        self.clock = pygame.time.Clock()
        #Imported settings 
        self.settings = Settings()
        #Screen display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth)) 
        pygame.display.set_caption("Alien Invasion")
        #Ship
        self.ship = Ship(self)
    
    
    #* FUNCTIONS
    
    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()  # check player input    
            self.ship.update()  # update position of screen and any bullet that have been
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)
            self._update_bullets()
            
    def _check_events(self):
        #Helper function that respond to keyboard/mouse events
        for event in pygame.event.get(): 
            #movement w/ keyevents
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
    
    def _update_screen(self):
        #Updates the images of the screen at 60FPS
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 
        pygame.display.flip()
    
    def _update_bullets(self):
        # Update position of bullet and get rid of outscreen bullets
        # Get rid of bullets that goes beyond the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        
    def _fire_bullet(self):
        # Create a new bullet and add it to the group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            print(len(self.bullets))
    
    
if __name__ == "__main__":
    #make a game instance and run it
    ai = AlienInvasion()
    ai.run_game()
            
            
            #! PAGINA 290 DEL CONTADOR DEL PDF, NO LA HOJA