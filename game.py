import pygame

#Constantes úteis:
casino_green = (7, 99, 36)
casino_title_font = "Casino3DLinesMarquee.ttf"
red = (209, 45, 54)
poker_chip = pygame.image.load("poker chip.png")
chip_loc_player_selection_list = [(279, 330), (279, 408), (279, 486), (545, 536)]
chip_loc_decks_selection_list = [(70, 300), (70, 363), (70, 426), (70, 489), (330, 300), (330, 363), (330, 426), (330, 489), (545, 536)]

#Variáveis globais:
players = 1

#Personalização da tela:
pygame.display.set_caption("The Wonderful World of Blackjack")
icon = pygame.image.load("image.png")
pygame.display.set_icon(icon)

#Classe de Jogo -------------------------------------------------------------------------------#
class Game():

    #O MENU -----------------------------------------------------------------------------------#

    #Função do menu principal --------------------------#
    def main_menu(self):
        background_photo = pygame.image.load("Main Menu.jpg").convert()
        self.window.blit(background_photo, (0, 0))
        self.window.blit(poker_chip, (279, 330))
        pygame.display.update() 
    #Função página about -------------------------------#
    def about_page(self):
        about_photo = pygame.image.load("About.jpg").convert()
        self.window.blit(about_photo, (0, 0))
        pygame.display.update()
        while self.running:
            self.check_events()
            if self.ENTER_KEY or self.ESC:
                self.reset_keys()
                self.main_menu()
                break  
    #Função que define a tela de seleção do jogador ----#
    def player_selection(self):
        player_selection_photo = pygame.image.load("Player Number.jpg").convert()
        self.window.blit(player_selection_photo, (0, 0))
        self.window.blit(poker_chip, (279, 330))
        pygame.display.update()
        chip_loc = 1
        while self.running:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY:
                chip_loc = self.move_chip_player_selection(chip_loc)
            if self.ENTER_KEY:
                if chip_loc == 1:
                    self.reset_keys
                    players = 1
                    self.decks_selection(players)
                elif chip_loc == 2:
                    self.reset_keys()
                    players = 2
                    chip_loc = 1
                    self.decks_selection(players)
                elif chip_loc == 3:
                    self.reset_keys()
                    players = 3
                    chip_loc = 1
                    self.decks_selection(players)
                elif chip_loc == 4:
                    self.main_menu()
                    self.reset_keys()
                    chip_loc = "up"
                    break
            if self.ESC:
                self.main_menu()
                self.reset_keys()
                chip_loc = "up"
                break
            pygame.display.update()
            self.reset_keys()
    ##Função que define a tela de seleção do número de baralhos ------#
    def decks_selection(self, players):
        decks_selection_photo = pygame.image.load("Deck Number.jpg").convert()
        self.window.blit(decks_selection_photo, (0, 0))
        self.window.blit(poker_chip, (70, 300))
        pygame.display.update()
        chip_loc = 1
        while self.running:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY or self.:
                chip_loc = self.move_chip_decks_selection(chip_loc)
            elif self.ESC:
                chip_loc = 1
                player_selection_photo = pygame.image.load("Player Number.jpg").convert()
                self.window.blit(player_selection_photo, (0, 0))
                self.window.blit(poker_chip, (279, 330))
                break
            elif self.ENTER_KEY:
                if chip_loc == 9:
                    chip_loc = 1
                    player_selection_photo = pygame.image.load("Player Number.jpg").convert()
                    self.window.blit(player_selection_photo, (0, 0))
                    self.window.blit(poker_chip, (279, 330))
                    break
                else:
                    self.reset_keys()
                    self.begin_game(players, chip_loc)
            pygame.display.update()
            self.reset_keys()
    #Função que move o chip para o menu principal ------#
    def move_chip_main(self):
        background_photo = pygame.image.load("Main Menu.jpg").convert()
        self.window.blit(background_photo, (0, 0))
        if self.DOWN_KEY:
            self.window.blit(poker_chip, (279, 408))
            return "down"
        if self.UP_KEY:
            self.window.blit(poker_chip, (279, 330))
            return "up"
    #Função que move o chip para a seleção de jogador --#
    def move_chip_player_selection(self, chip_loc):
        background_photo = pygame.image.load("Player Number.jpg").convert()
        if self.DOWN_KEY and (chip_loc < 4):
            chip_loc += 1
        if self.UP_KEY and (chip_loc > 1):
            chip_loc -= 1
        self.window.blit(background_photo, (0, 0))
        self.window.blit(poker_chip, chip_loc_player_selection_list[chip_loc-1])
        return chip_loc
    #Função que move o chip para a seleção dos baralhos -#
    def move_chip_decks_selection(self, chip_loc):
        background_photo = pygame.image.load("Deck Number.jpg").convert()
        if self.DOWN_KEY and (chip_loc == 4):
            chip_loc = 9
        if self.DOWN_KEY and (chip_loc < 9) and (chip_loc != 4):
            chip_loc += 1
        if self.UP_KEY and (chip_loc > 1) and (chip_loc != 5):
            chip_loc -= 1
        if self.RIGHT_KEY and (chip_loc < 5):
            chip_loc += 4
        if self.RIGHT_KEY and (chip_loc > 4) and (chip_loc < 9):
            chip_loc = 9
        if self.LEFT_KEY and (chip_loc == 9):
            chip_loc = 8
        if self.LEFT_KEY and (chip_loc > 4) and (chip_loc < 9):
            chip_loc -= 4
        self.window.blit(background_photo, (0, 0))
        self.window.blit(poker_chip, chip_loc_decks_selection_list[chip_loc-1])
        return chip_loc
    #Função para escrever coisas -----------------------#
    def write(self, text, size, font, colour, x, y):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)
    #Função que inicia o jogo --------------------------#
    def initialise(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY, self.ESC = False, False, False, False, False
        self.display = pygame.Surface((800, 600))
        self.window = pygame.display.set_mode((800, 600)) 
        self.main_menu()
    #Função que checa o input do jogador ----------------#
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC = True
    #Função que reseta as keys -------------------------#
    def reset_keys(self):
        self.ENTER_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY, self.ESC = False, False, False, False, False, False, False
    #Função game_loop para o menu principal ------------#
    def game_loop(self):
        chip_loc = "up"
        while self.running:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY:
                chip_loc = self.move_chip_main()
            if self.ENTER_KEY:
                if chip_loc == "up":
                    self.reset_keys
                    self.player_selection()
                if chip_loc == "down":
                    self.reset_keys()
                    self.about_page()
                    chip_loc = "up"
            pygame.display.update()
            self.reset_keys()

    #O JOGO EM SI -----------------------------------------------------------------------------#
    def begin_game(self, players, decks):
        self.reset_keys()
        background_game_photo = pygame.image.load("Game Screen.jpg").convert
        self.window.blit(background_game_photo, (0, 0))
        pygame.display.update()






#CREDITS:
#Casino Font Family:
#Vladimir Nikolic @https://www.coroflot.com/vladimirnikolic/profile
#Icon Image:
#Eucalyp @https://www.flaticon.com/authors/eucalyp
#Cards:
#Byron Knoll @http://code.google.com/p/vector-playing-cards/