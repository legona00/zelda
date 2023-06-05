import pygame, sys
from settings import *
from level import Level



class Game:
    def __init__(self):
        #general setup
        self.title_font = pygame.font.SysFont(UI_FONT, 200)
        self.text_font = pygame.font.SysFont(UI_FONT, 40)

        #initiate pygame, surface, and a clock, ALWAYS NEED FOR PYGAME
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda in Python') #Change name for game window
        self.clock = pygame.time.Clock()

        self.level = Level()
        #sound
        

    def draw_start_menu(self):
        self.screen.fill((0,0,0))
        title = self.title_font.render('ZELDA', True, (255,255,255))
        start_button = self.text_font.render('PRESS SPACE START', True, 'gold')
        self.screen.blit(title, (1300/2 - title.get_width()/2, 450/2 - title.get_height()/2))
        self.screen.blit(start_button, (1300/2 - start_button.get_width()/2, 600/2 + start_button.get_height()/2))
        pygame.display.update()

    def draw_game_over(self):
        self.screen.fill('maroon')
        title = self.title_font.render('GAME OVER', True, 'gold')
        restart = self.text_font.render('R - Restart', True, 'white')
        quit_button = self.text_font.render('Q - Quit', False, 'white')
        self.screen.blit(title, (1300/2 - title.get_width()/2, 450/2 - title.get_height()/2))
        self.screen.blit(restart, (1300/2 - restart.get_width()/2, 600/2 + restart.get_height()/2))
        self.screen.blit(quit_button, (1300/2 - restart.get_width()/2, 600/2 + restart.get_height()/2))
        pygame.display.update()

    def run(self):
        #EVENT LOOP
        game_state = 'start'
        if game_state == 'start' or game_state == 'game':
                #sound setup
                game_audio = pygame.mixer.Sound('../audio/main.ogg')
                game_audio.set_volume(0.6)
                game_audio.play()
        game_over = False
        while(game_over == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            

            if game_state == 'start':
                self.draw_start_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_state = 'game'
                                     

#           FILL SCREEN WITH BLACK COLOR, UPDATING, and setting FPS
            if game_state == 'game':
                self.screen.fill(WATER_COLOR)
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)
                if self.level.check_player_death():
                    game_state = 'death'

            if game_state == 'death':
                #Change sound
                game_audio.fadeout(700)
                death_sound = pygame.mixer.Sound('../audio/darksoulsdeadsound.ogg')
                death_sound.set_volume(0.3)
                death_sound.play()

                self.draw_game_over()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
                if keys[pygame.K_r]:
                    game_over = True

        death_sound.stop()
        self.level = Level()
        self.run()

#Check if in main file, create instance of the class and call run method from Game class
if __name__ == '__main__':
    game = Game()
    game.run()