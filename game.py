import pygame
import random

#Constantes úteis:
casino_green = (7, 99, 36)
casino_title_font = "Casino3DLinesMarquee.ttf"
red = (209, 45, 54)
poker_chip = pygame.image.load("poker chip.png")
chip_loc_player_selection_list = [(279, 330), (279, 408), (279, 486), (545, 536)]
chip_loc_decks_selection_list = [(70, 305), (70, 368), (70, 431), (70, 494), (325, 305), (325, 368), (325, 431), (325, 494), (545, 536)]

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
                    self.reset_keys()
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
        self.window.blit(poker_chip, (70, 305))
        pygame.display.update()
        chip_loc = 1
        while self.running:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY or self.LEFT_KEY or self.RIGHT_KEY:
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
        elif self.DOWN_KEY and (chip_loc < 9) and (chip_loc != 4):
            chip_loc += 1
        elif self.UP_KEY and (chip_loc > 1) and (chip_loc != 5):
            chip_loc -= 1
        elif self.RIGHT_KEY and (chip_loc < 5):
            chip_loc += 4
        elif self.RIGHT_KEY and (chip_loc > 4) and (chip_loc < 9):
            chip_loc = 9
        elif self.LEFT_KEY and (chip_loc == 9):
            chip_loc = 8
        elif self.LEFT_KEY and (chip_loc > 4) and (chip_loc < 9):
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
                if event.key == pygame.K_r:
                    self.R = True
                if event.key == pygame.K_w:
                    self.W = True
                if event.key == pygame.K_e:
                    self.A = True
                if event.key == pygame.K_s:
                    self.S = True
                if event.key == pygame.K_d:
                    self.D = True
    #Função que reseta as keys -------------------------#
    def reset_keys(self):
        self.ENTER_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY, self.ESC, self.R, self.A, self.W, self.S, self.D = False, False, False, False, False, False, False, False, False, False, False, False
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
                    self.reset_keys()
                    self.player_selection()
                if chip_loc == "down":
                    self.reset_keys()
                    self.about_page()
                    chip_loc = "up"
            pygame.display.update()
            self.reset_keys()

    #O JOGO EM SI -----------------------------------------------------------------------------#
    #Função que embaralha as cartas: ----------------------------------------------#
    # def shuffle(self, decks):
    #     deck = [("a", "s"), (2, "s"), (3, "s"), (4, "s"), (5, "s"), (6, "s"), (7, "s"), (8, "s"), (9, "s"), (10, "s"), (11, "s"), (12, "s"), (13, "s"), 
    #     ("a", "c"), (2, "c"), (3, "c"), (4, "c"), (5, "c"), (6, "c"), (7, "c"), (8, "c"), (9, "c"), (10, "c"), (11, "c"), (12, "c"), (13, "c"), 
    #     ("a", "d"), (2, "d"), (3, "d"), (4, "d"), (5, "d"), (6, "d"), (7, "d"), (8, "d"), (9, "d"), (10, "d"), (11, "d"), (12, "d"), (13, "d"),
    #     ("a", "h"), (2, "h"), (3, "h"), (4, "h"), (5, "h"), (6, "h"), (7, "h"), (8, "h"), (9, "h"), (10, "h"), (11, "h"), (12, "h"), (13, "h")]
    #     full_deck = []
    #     for i in range(decks):
    #         for j in range(52):
    #             full_deck.append(deck[j])
    #     random.shuffle(full_deck)
    
    # def check_for_game_over(self):
    #     if (player_balance <= 0) or (len(schuffled_deck) <= 20) or (self.ESC) or not self.running:
    #         self.game_over = True

    # def turn(self, deck, player_balance):
    #     self.reset_keys()
    #     #Função ask_for_player_bet() pede aposta para o jogador, checa se é possível e devolve aposta
    #     player_bet = self.ask_for_player_bet(player_balance)
    #     player_hand = []
    #     dealer_hand = []
    #     #Função deal_a_card() retorna um tuplo (carta, baralho após tirar a carta) ao mesmo tempo desenhando na tela a carta em questão
    #     card1, new_deck = self.deal_a_card("player", deck)
    #     card2, new_deck  = self.deal_a_card("player", new_deck)
    #     player_hand.append(card1)
    #     player_hand.append(card2)
    #     card1, new_deck = self.deal_a_card("dealer down", new_deck)
    #     card2, new_deck  = self.deal_a_card("dealer", new_deck)
    #     dealer_hand.append(card1)
    #     dealer_hand.append(card2)
    #     while not self.S_KEY:
    #         #Função check_events_gameloop() checa o input e executa a função correspondente devolvendo a mão do jogador e o novo baralho
    #         player_hand, new_deck = self.check_events_gameloop(player_hand, new_deck)
    #         self.reset_keys()
    #     self.reset_keys()
    #     #Função dealer_turn() executa a vez do dealer
    #     dealer_hand, new_deck = self.dealer_turn(dealer_hand, new_deck)
    #     #Função compare_hands() compara as mãos dizendo quanto deve ser pago/tirado do jogador no tuplo (valor, sinal)
    #     player_bet_add, sign = self.compare_hands(dealer_hand, player_hand, player_bet)
    #     if sign == "+":
    #         player_bet += player_bet_add
    #     elif sign == "-":
    #         player_bet -= player_bet_add
    #     #Função reset_screen() volta a tela para o estado inicial com o contador igual ao novo balanço do jogador
    #     self.reset_screen(player_balance)
    #     return(new_deck, player_balance)

    # def rules(self):
    #     self.reset_keys()
    #     screenshot = 
    #     rules1 = pygame.image.load("Rules 1.png")
    #     rules2 = pygame.image.load("Rules 1.png")
    #     self.window.blit(rules1, (126, 100))
    #     pygame.display.update()
    #     rule_menu = 1
    #     while self.running and not self.R and not self.ESC:
    #         self.check_events()
    #         if self.ENTER_KEY:
    #             if rule_menu == 1:
    #                 self.window.blit(screenshot, (0, 0))
    #                 self.window.blit(rules2, (126, 100))
    #                 pygame.display.update()
    #                 rule_menu += 1
    #             elif rule_menu == 2:
    #                 self.window.blit(screenshot, (0, 0))
    #                 pygame.display.update()
    #                 break
    #         self.reset_keys()
    #     self.reset_keys()

    #Função central do jogo: -------------------------------------------------------#
    def begin_game(self, players, decks):
        self.reset_keys()
        player_balance = 100
        background_game_photo = pygame.image.load("Game Screen.jpg").convert()
        self.window.blit(background_game_photo, (0, 0))
        pygame.display.update()
        #self.rules()
        #self.reset_keys()  
        # shuffled_deck = self.shuffle(decks)
        # while self.running:
        #     while not self.game_over:
        #         shuffled_deck, player_balance = self.turn(shuffled_deck, player_balance)
        #     #if self.ESC:
        #         #Função abre tela perguntando se jogador tem certeza que quer sair
        #         #self.are_you_sure()
        #     if self.running:
        #         #Função abre tela do game over
        #         self.game_over_screen(player_balance)












#CREDITS:
#Casino Font Family:
#Vladimir Nikolic @https://www.coroflot.com/vladimirnikolic/profile
#Icon Image:
#Eucalyp @https://www.flaticon.com/authors/eucalyp
#Cards:
#Byron Knoll @http://code.google.com/p/vector-playing-cards/