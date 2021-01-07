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
    def write(self, text, size, font, colour, x, y, align="center"):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = (x, y)
        else:
            text_rect.midleft = (x, y)
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
    #Função que cria a tela de regras: --------------------------------------------#
    def rules(self):
        self.reset_keys()
        screenshot = pygame.Surface(self.window.get_size(), 0, self.window)
        screenshot.blit(self.window, (0, 0))
        rules1 = pygame.image.load("Rules 1.png")
        rules2 = pygame.image.load("Rules 2.png")
        self.window.blit(rules1, (126, 100))
        pygame.display.update()
        rule_menu = 1
        while self.running and not self.R and not self.ESC:
            self.check_events()
            if self.ENTER_KEY:
                if rule_menu == 1:
                    self.window.blit(screenshot, (0, 0))
                    self.window.blit(rules2, (126, 100))
                    pygame.display.update()
                    rule_menu += 1
                elif rule_menu == 2:
                    self.window.blit(screenshot, (0, 0))
                    pygame.display.update()
                    break
            self.reset_keys()
        self.reset_keys()
    #Função que embaralha as cartas: ----------------------------------------------#
    def shuffle(self, decks):
        deck = [("a", "s"), (2, "s"), (3, "s"), (4, "s"), (5, "s"), (6, "s"), (7, "s"), (8, "s"), (9, "s"), (10, "s"), ("j", "s"), ("q", "s"), ("k", "s"), 
        ("a", "c"), (2, "c"), (3, "c"), (4, "c"), (5, "c"), (6, "c"), (7, "c"), (8, "c"), (9, "c"), (10, "c"), ("j", "c"), ("q", "c"), ("k", "c"), 
        ("a", "d"), (2, "d"), (3, "d"), (4, "d"), (5, "d"), (6, "d"), (7, "d"), (8, "d"), (9, "d"), (10, "d"), ("j", "d"), ("q", "d"), ("k", "d"),
        ("a", "h"), (2, "h"), (3, "h"), (4, "h"), (5, "h"), (6, "h"), (7, "h"), (8, "h"), (9, "h"), (10, "h"), ("j", "h"), ("q", "h"), ("k", "h")]
        full_deck = []
        for i in range(decks):
            for j in range(52):
                full_deck.append(deck[j])
        full_deck = random.shuffle(full_deck)
        return full_deck
    #Função que checa se alguma das condições de fim de jogo se verificam: --------------------#
    def check_for_game_over(self):
        if (player_balance <= 0) or (len(schuffled_deck) <= 20) or (self.ESC) or not self.running:
            self.game_over = True
    #Função que capta a aposta do jogador: --------------------------------------------------#
    def ask_for_player_bet(self, player_balance):
        background_game_photo = pygame.image.load("Game Screen.jpg").convert()
        self.num = False
        player_bet = 0
        money_box = pygame.image.load("Money box.png")
        self.window.blit(money_box, (305, 256))
        self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
        pygame.display.update()
        while self.running:
            self.check_written()
            if type(self.num) == int:
                player_bet = int(str(player_bet) + str(self.num))
                if player_bet <= player_balance:
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    self.reset_keys()
                    self.num = False
                elif player_balance <= player_bet:
                    player_bet = 0
                    self.window.blit(background_game_photo, (0,0))
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    self.write("Please write in a value smaller than your balance", 20, "CasinoFlat.ttf", (255, 255, 255), 400, 363)
                    self.reset_keys()
                    self.num = False
            elif self.ENTER_KEY == True:
                if player_bet == 0:
                    self.window.blit(background_game_photo, (0,0))
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    self.write("Please write in a value", 20, "CasinoFlat.ttf", (255, 255, 255), 400, 363)
                    self.reset_keys()
                else:
                    self.window.blit(background_game_photo, (0, 0))
                    self.num = False
                    self.reset_keys()
                    pygame.display.update()
                    return(player_bet)
            elif self.ESC == True:
                #Are_you_sure() function --------------------#
                self.running = False
            elif self.BACK_KEY == True:
                self.window.blit(background_game_photo, (0,0))
                self.window.blit(money_box, (305, 256))
                player_bet = player_bet//10
                self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                self.reset_keys()
                self.num = False
            pygame.display.update()     
    #Função que checa o valor de número escrito: -------------------#
    def check_written(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.ESC = True
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_0:
                    self.num = 0
                if event.key == pygame.K_1:
                    self.num = 1
                if event.key == pygame.K_2:
                    self.num = 2
                if event.key == pygame.K_3:
                    self.num = 3
                if event.key == pygame.K_4:
                    self.num = 4
                if event.key == pygame.K_5:
                    self.num = 5
                if event.key == pygame.K_6:
                    self.num = 6
                if event.key == pygame.K_7:
                    self.num = 7
                if event.key == pygame.K_8:
                    self.num = 8
                if event.key == pygame.K_9:
                    self.num = 9
    #Função que move o gráfico da carta do bolo para a localização final:-------------#
    def move_card(self, graphic, person, hand):
        final_loc_h = 0
        final_loc_w = 300
        if person == "player":
            final_loc_h = 600
        else:
            final_loc_h = 200
        for card in range(len(hand)):
            final_loc_w += 30
        start_loc = [12, 10]
        h_factor = (final_loc_h - start_loc[1])/100
        w_factor = (final_loc_w - start_loc[0])/100
        current_loc = start_loc
        screenshot = pygame.Surface(self.window.get_size(), 0, self.window)
        screenshot.blit(self.window, (0, 0))
        while current_loc[0] < final_loc_w:
            self.window.blit(screenshot, (0, 0))
            self.window.blit(graphic, current_loc)
            current_loc[0] += w_factor
            current_loc[1] += h_factor
            pygame.time.delay(30)
            pygame.display.update()
        self.reset_keys()
    # Função que dá uma carta para o jogador/dealer: -----------------#
    def deal_a_card(self, person, deck, hand):
        if person == "dealer_down":
            card = "down"
            graphic = pygame.image.load("card.png")
        else:
            card = deck.pop(0)
            cardname = "{a}{b}.png".format(a=str(card[0]), b=card[1])
            graphic = pygame.image.load(cardname)
        self.move_card(graphic, person, hand)
        return card, deck
    #Função que executa as funções relativas à vez do indivíduo/maquina: ---------------#
    def turn(self, deck, player_balance):
        while self.running:
            self.reset_keys()
            player_bet = self.ask_for_player_bet(player_balance)
            player_hand = []
            dealer_hand = []
            # #Função deal_a_card() retorna um tuplo (carta, baralho após tirar a carta) ao mesmo tempo desenhando na tela a carta em questão
            card1, new_deck = self.deal_a_card("player", deck, player_hand)
            player_hand.append(card1)
            # card2, new_deck  = self.deal_a_card("player", new_deck, player_hand)
            # player_hand.append(card2)
            # card1, new_deck = self.deal_a_card("dealer_down", new_deck, dealer_hand)
            # dealer_hand.append(card1)
            # card2, new_deck  = self.deal_a_card("dealer_down", new_deck, dealer_hand)
            # dealer_hand.append(card2)
            # while not self.S_KEY:
            #     #Função check_events_gameloop() checa o input e executa a função correspondente devolvendo a mão do jogador e o novo baralho
            #     player_hand, new_deck = self.check_events_gameloop(player_hand, new_deck)
            #     self.reset_keys()
            # self.reset_keys()
            # #Função dealer_turn() executa a vez do dealer
            # dealer_hand, new_deck = self.dealer_turn(dealer_hand, new_deck)
            # #Função compare_hands() compara as mãos dizendo quanto deve ser pago/tirado do jogador no tuplo (valor, sinal)
            # player_bet_add, sign = self.compare_hands(dealer_hand, player_hand, player_bet)
            # if sign == "+":
            #     player_bet += player_bet_add
            # elif sign == "-":
            #     player_bet -= player_bet_add
            # #Função reset_screen() volta a tela para o estado inicial com o contador igual ao novo balanço do jogador
            # self.reset_screen(player_balance)
            # return(new_deck, player_balance)
            
    #Função central do jogo: -------------------------------------------------------#
    def begin_game(self, players, decks):
        self.reset_keys()
        player_balance = 100
        background_game_photo = pygame.image.load("Game Screen.jpg").convert()
        self.window.blit(background_game_photo, (0, 0))
        pygame.display.update()
        self.rules() 
        shuffled_deck = self.shuffle(decks)
        while self.running: #and not self.game_over:
            shuffled_deck, player_balance = self.turn(shuffled_deck, player_balance)
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