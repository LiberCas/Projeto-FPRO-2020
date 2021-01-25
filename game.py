import pygame
import random
pygame.mixer.init()

#Constantes úteis:
casino_green = (7, 99, 36)
casino_font = "CasinoFlat.ttf"
red = (209, 45, 54)
poker_chip = pygame.image.load("poker chip.png")
poker_chip_game_red = pygame.image.load("Med Red.png")
poker_chip_blue = pygame.image.load("poker chip blue.png")

card_toss_sound = pygame.mixer.Sound("card toss.wav")
card_shuffle_sound = pygame.mixer.Sound("card shuffle.wav")
card_deck_sound = pygame.mixer.Sound("card from deck.wav")
chip_sound = pygame.mixer.Sound("chip sound.wav")
music = pygame.mixer.music.load("music.wav")

chip_loc_player_selection_list = [(279, 330), (279, 408), (279, 486), (545, 536)]
chip_loc_decks_selection_list = [(70, 305), (70, 368), (70, 431), (70, 494), (325, 305), (325, 368), (325, 431), (325, 494), (545, 536)]
balance_image = pygame.image.load("Player Balance.png")


pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

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
        while self.running:
            self.playing = True
            background_photo = pygame.image.load("Main Menu.jpg").convert()
            self.window.blit(background_photo, (0, 0))
            self.window.blit(poker_chip, (279, 330))
            pygame.display.update()
            self.game_loop()
    #Função página about -------------------------------#
    def about_page(self):
        about_photo = pygame.image.load("About.jpg").convert()
        self.window.blit(about_photo, (0, 0))
        pygame.display.update()
        while self.running:
            self.check_events()
            if self.ENTER_KEY or self.ESC:
                pygame.mixer.Sound.play(chip_sound)
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
        while self.running and self.playing:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY:
                chip_loc = self.move_chip_player_selection(chip_loc)
            elif self.ENTER_KEY:
                pygame.mixer.Sound.play(chip_sound)
                if chip_loc == 1:
                    self.reset_keys()
                    players = 1
                    self.decks_selection(players)
                elif chip_loc == 2:
                    self.reset_keys()
                    self.multiplayer()
                    self.window.blit(player_selection_photo, (0, 0))
                    self.window.blit(poker_chip, (279, 330))
                    pygame.display.update()
                    chip_loc = 1
                elif chip_loc == 3:
                    self.reset_keys()
                    self.multiplayer()
                    self.window.blit(player_selection_photo, (0, 0))
                    self.window.blit(poker_chip, (279, 330))
                    pygame.display.update()
                    chip_loc = 1
                elif chip_loc == 4:
                    self.reset_keys()
                    chip_loc = "up"
                    self.main_menu()
                    break
            elif self.ESC:
                pygame.mixer.Sound.play(chip_sound)
                self.reset_keys()
                chip_loc = "up"
                self.main_menu()
                break
            pygame.display.update()
            self.reset_keys()
    #Função que define as telas de multijogador ---------------------#
    def multiplayer(self):
        multiplayer_photo = pygame.image.load("Multiplayer.jpg").convert()
        self.window.blit(multiplayer_photo, (0, 0))
        pygame.display.update()
        while self.running:
            self.check_events()
            if self.ESC or self.ENTER_KEY:
                self.reset_keys()
                pygame.mixer.Sound.play(chip_sound)
                break
    #Função que define a tela de seleção do número de baralhos ------#
    def decks_selection(self, players):
        decks_selection_photo = pygame.image.load("Deck Number.jpg").convert()
        self.window.blit(decks_selection_photo, (0, 0))
        self.window.blit(poker_chip, (70, 305))
        pygame.display.update()
        chip_loc = 1
        while self.running and self.playing:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY or self.LEFT_KEY or self.RIGHT_KEY:
                chip_loc = self.move_chip_decks_selection(chip_loc)
            elif self.ESC:
                pygame.mixer.Sound.play(chip_sound)
                chip_loc = 1
                player_selection_photo = pygame.image.load("Player Number.jpg").convert()
                self.window.blit(player_selection_photo, (0, 0))
                self.window.blit(poker_chip, (279, 330))
                break
            elif self.ENTER_KEY:
                pygame.mixer.Sound.play(chip_sound)
                if chip_loc == 9:
                    chip_loc = 1
                    player_selection_photo = pygame.image.load("Player Number.jpg").convert()
                    self.window.blit(player_selection_photo, (0, 0))
                    self.window.blit(poker_chip, (279, 330))
                    break
                else:
                    self.reset_keys()
                    self.begin_game(players, chip_loc)
            if self.ESC or self.R:
                decks_selection_photo = pygame.image.load("Deck Number.jpg").convert()
                self.window.blit(decks_selection_photo, (0, 0))
                self.window.blit(poker_chip, (70, 305))
                chip_loc = 1
            pygame.display.update()
            self.reset_keys()
    #Função que move o chip para o menu principal ------#
    def move_chip_main(self):
        background_photo = pygame.image.load("Main Menu.jpg").convert()
        self.window.blit(background_photo, (0, 0))
        if self.DOWN_KEY:
            self.window.blit(poker_chip, (279, 408))
            pygame.mixer.Sound.play(chip_sound)
            return "down"
        if self.UP_KEY:
            self.window.blit(poker_chip, (279, 330))
            pygame.mixer.Sound.play(chip_sound)
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
        pygame.mixer.Sound.play(chip_sound)
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
        pygame.mixer.Sound.play(chip_sound)
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
        pygame.mixer.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY, self.ESC = False, False, False, False, False
        self.display = pygame.Surface((800, 600))
        self.window = pygame.display.set_mode((800, 600)) 
        self.main_menu()
    #Função que checa o input do jogador ----------------#
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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
                if event.key == pygame.K_a:
                    self.A = True
                if event.key == pygame.K_s:
                    self.S = True
                if event.key == pygame.K_d:
                    self.D = True
                if event.key == pygame.K_i:
                    self.I = True
    #Função que reseta as keys -------------------------#
    def reset_keys(self):
        self.ENTER_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY, self.ESC, self.R, self.A, self.W, self.S, self.D, self.I = False, False, False, False, False, False, False, False, False, False, False, False, False
    #Função game_loop para o menu principal ------------#
    def game_loop(self):
        chip_loc = "up"
        while self.running and self.playing:
            self.check_events()
            #Aqui direi o que acontece em cada evento
            if self.UP_KEY or self.DOWN_KEY:
                chip_loc = self.move_chip_main()
            if self.ENTER_KEY:
                pygame.mixer.Sound.play(chip_sound)
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
    #Função central do jogo: -------------------------------------------------------#
    def begin_game(self, players, decks):
        self.playing = True
        self.reset_keys()
        player_balance = 100
        background_game_photo = pygame.image.load("Game Screen.jpg").convert()
        self.window.blit(background_game_photo, (0, 0))
        self.update_pb(player_balance)
        pygame.display.update()
        self.rules()
        shuffled_deck = self.shuffle(decks)
        while self.running and self.playing:
            if self.ESC or self.R:
                break
            shuffled_deck, player_balance, game_over = self.turn(shuffled_deck, player_balance)
            self.window.blit(background_game_photo, (0, 0))
            pygame.display.update()
            self.reset_keys()
            if not self.playing:
                break
            if game_over != False:
                self.game_over_screen(game_over)
                break   
            self.check_events()
            if self.ESC:
                self.playing = False
                self.reset_keys()
                break
            elif self.R:
                self.rules()
    #Função que cria a tela de regras: --------------------------------------------#
    def rules(self, midgame=False):
        self.reset_keys()
        screenshot = pygame.Surface(self.window.get_size(), 0, self.window)
        screenshot.blit(self.window, (0, 0))
        rules1 = pygame.image.load("Rules 1.png")
        rules2 = pygame.image.load("Rules 2.png")
        self.window.blit(rules1, (126, 100))
        pygame.display.update()
        rule_menu = 1
        while self.running:
            self.check_events()
            if self.ENTER_KEY:
                if rule_menu == 1:
                    self.window.blit(screenshot, (0, 0))
                    self.window.blit(rules2, (126, 100))
                    pygame.display.update()
                    rule_menu += 1
                    pygame.mixer.Sound.play(chip_sound)
                elif rule_menu == 2:
                    self.window.blit(screenshot, (0, 0))
                    pygame.display.update()
                    pygame.mixer.Sound.play(chip_sound)
                    break
            elif self.ESC or self.R:
                if midgame != False:
                    self.window.blit(screenshot, (0, 0))
                    pygame.display.update()
                    break
                else:
                    break
            self.reset_keys()
    #Função que executa as funções relativas à vez do indivíduo/maquina: ---------------#
    def turn(self, deck, player_balance, game_over=False):
        pygame.mixer.Sound.play(card_shuffle_sound)
        pygame.time.delay(1000)
        while self.running and self.playing:
            self.reset_keys()
            player_bet = self.ask_for_player_bet(player_balance)
            self.draw_chip(player_bet)
            if self.playing == False:
                return 0, 0, False
            player_balance -= player_bet
            self.update_pb(player_balance)
            pygame.display.update()
            player_hand = [[], 0, 0, "ns"]
            dealer_hand = [[], 0]
            # #Função deal_a_card() retorna um tuplo (carta, baralho após tirar a carta) ao mesmo tempo desenhando na tela a carta em questão
            player_hand, new_deck = self.deal_a_card("player", deck, player_hand)
            player_hand, new_deck  = self.deal_a_card("player", new_deck, player_hand)
            dealer_hand, new_deck = self.deal_a_card("dealer_down", new_deck, dealer_hand)
            dealer_hand, new_deck  = self.deal_a_card("dealer", new_deck, dealer_hand)
            self.reset_keys()
            player_hand = self.check_hand_value(player_hand)
            player_hand, player_balance, player_bet, new_deck = self.player_turn(player_hand, player_balance, player_bet, new_deck, dealer_hand)
            if new_deck == 0:
                return 0, 0, False
            self.reset_keys()
            if self.running and self.playing and game_over != True:
                #Função dealer_turn() executa a vez do dealer
                dealer_hand, new_deck, game_over = self.dealer_turn(dealer_hand, new_deck)
            if self.running and game_over != True:
                #Função compare_hands() compara as mãos dizendo quanto deve ser pago/tirado do jogador no tuplo (valor, sinal)
                player_balance = self.compare_hands(dealer_hand, player_hand, player_bet, player_balance)
                self.update_pb(player_balance)
                pygame.display.update()
                game_over = self.check_for_game_over(new_deck, player_balance) 
            return new_deck, player_balance, game_over
    #Função da vez do jogador: -----------------------#
    def player_turn(self, player_hand, player_balance, player_bet, new_deck, dealer_hand, split=False):
        while self.running:
            self.check_events()
            #Acções: -----------------------------------------#
            if self.ESC:
                self.reset_keys()
                self.playing = False
                return 0, 0, 0, 0
            if self.R:
                self.rules(True)
                self.reset_keys()
            if self.I and dealer_hand[0][1][0] == "a":
                player_hand[2] = self.ask_for_player_bet(player_balance, player_bet)
                if player_hand[2] != 0:
                    self.draw_chip(player_hand[2], True, split)
                player_balance -= player_hand[2]
                self.update_pb(player_balance)
                pygame.display.update()
                #Insurance graphic function
            elif self.A and player_hand[1] != "blackjack":
                player_hand, new_deck = self.deal_a_card("player", new_deck, player_hand, split)
                player_hand = self.check_hand_value(player_hand)
                if player_hand[1] == "bust":
                    break
            elif self.D and len(player_hand[0]) == 2 and player_bet <= player_balance  and player_hand[1] != "blackjack":
                player_balance -= player_bet
                player_bet *= 2
                self.draw_chip(player_bet, False, split)
                self.update_pb(player_balance)
                pygame.display.update()
                card5, new_deck = self.deal_a_card("player", new_deck, player_hand, split)
                player_hand[0].append(card5)
                player_hand = self.check_hand_value(player_hand)
                break
            elif self.W and split == False and player_hand[2] == 0 and len(player_hand[0]) == 2 and player_hand[0][0][0] == player_hand[0][1][0] and player_hand[1] != "blackjack":
                # Split Function ------------------#
                player_hand, player_balance, player_bet, new_deck = self.split(player_hand, player_balance, player_bet, new_deck, dealer_hand)
                break
            elif self.S:
                break
            elif self.running == False:
                break
            if player_hand[1] == "blackjack":
                break
            self.reset_keys()
        return player_hand, player_balance, player_bet, new_deck
    #Função da vez do dealer: ------------------------#
    def dealer_turn(self, dealer_hand, new_deck, game_over=False):
        dealer_hand[0][0] = new_deck.pop(0)
        dealer_hand = self.check_hand_value(dealer_hand)
        graphic1 = "{a}{b}.png".format(a=str(dealer_hand[0][0][0]), b=dealer_hand[0][0][1])
        graphic1 = pygame.image.load(graphic1)
        graphic2 = "{a}{b}.png".format(a=str(dealer_hand[0][1][0]), b=dealer_hand[0][1][1])
        graphic2 = pygame.image.load(graphic2)
        self.window.blit(graphic1, (300, 27))
        self.window.blit(graphic2, (330, 27))
        pygame.display.update()
        while self.running and type(dealer_hand[1]) == int and dealer_hand[1] < 17:
            dealer_hand, new_deck = self.deal_a_card("dealer", new_deck, dealer_hand)
            dealer_hand = self.check_hand_value(dealer_hand)
            self.check_events()
            if self.ESC:
                game_over = True
                break 
            self.reset_keys()
        pygame.time.delay(2000)
        return dealer_hand, new_deck, game_over
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
        random.shuffle(full_deck)
        return full_deck
    #Função que checa se alguma das condições de fim de jogo se verificam: --------------------#
    def check_for_game_over(self, new_deck, player_balance):
        if (player_balance <= 0):
            return "Lost"
        elif len(new_deck) <= 20:
            return player_balance
        else:
            return False
    #Função que capta a aposta do jogador: --------------------------------------------------#
    def ask_for_player_bet(self, player_balance, insurance=False, split=False):
        if insurance == False:
            background_game_photo = pygame.image.load("Game Screen.jpg").convert()
        else:
            background_game_photo = pygame.Surface(self.window.get_size(), 0, self.window)
        background_game_photo.blit(self.window, (0, 0))
        player_bet = 0
        self.num = False
        money_box = pygame.image.load("Money box.png")
        self.window.blit(money_box, (305, 256))
        self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
        self.update_pb(player_balance)
        pygame.display.update()
        while self.running:
            self.check_written()
            if type(self.num) == int:
                player_bet = int(str(player_bet) + str(self.num))
                if player_bet <= player_balance and (insurance == False or player_bet <= (insurance/2)):
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    self.reset_keys()
                    self.num = False
                elif player_balance <= player_bet:
                    player_bet = 0
                    self.window.blit(background_game_photo, (0,0))
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    if insurance == 0:
                        self.write("Please write in a value smaller than your balance", 20, "CasinoFlat.ttf", (255, 255, 255), 400, 363)
                    else:
                        self.write("Please write in a value smaller than half your initial bet", 20, "CasinoFlat.ttf", (255, 255, 255), 400, 363)
                    self.reset_keys()
                    self.update_pb(player_balance)
                    self.num = False
            elif self.ENTER_KEY == True:
                if player_bet == 0:
                    self.window.blit(background_game_photo, (0,0))
                    self.window.blit(money_box, (305, 256))
                    self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                    self.write("Please write in a value", 20, "CasinoFlat.ttf", (255, 255, 255), 400, 363)
                    self.update_pb(player_balance)
                    self.reset_keys()
                else:
                    self.window.blit(background_game_photo, (0, 0))
                    self.num = False
                    self.reset_keys()
                    pygame.display.update()
                    return player_bet
            elif self.ESC == True:
                #Are_you_sure() function --------------------#
                self.reset_keys()
                if insurance == False:
                    self.playing = False
                    return player_bet
                else:
                    return 0
            elif self.BACK_KEY == True:
                self.window.blit(background_game_photo, (0,0))
                self.window.blit(money_box, (305, 256))
                player_bet = player_bet//10
                self.write(str(player_bet), 40, "CasinoFlat.ttf", (255, 255, 255), 345, 316, "midleft")
                self.reset_keys()
                self.update_pb(player_balance)
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
                    self.num = 5
                if event.key == pygame.K_5:
                    self.num = 4
                if event.key == pygame.K_6:
                    self.num = 6
                if event.key == pygame.K_7:
                    self.num = 7
                if event.key == pygame.K_8:
                    self.num = 8
                if event.key == pygame.K_9:
                    self.num = 9
    #Função que move o gráfico da carta do bolo para a localização final:-------------#
    def move_card(self, graphic, person, hand, split=False):
        final_loc_h = 0
        final_loc_w = 300
        if person == "player":
            final_loc_h = 406
        else:
            final_loc_h = 27
        if split == 1:
            final_loc_w = 170
        elif split == 2:
            final_loc_w = 500
        for card in range(len(hand[0])):
            final_loc_w += 30
        start_loc = [12, 10]
        h_factor = (final_loc_h - start_loc[1])/400
        w_factor = (final_loc_w - start_loc[0])/400
        current_loc = start_loc.copy()
        screenshot = pygame.Surface(self.window.get_size(), 0, self.window)
        screenshot.blit(self.window, (0, 0))
        pygame.mixer.Sound.play(card_deck_sound)
        while current_loc[0] < final_loc_w:
            self.window.blit(screenshot, (0, 0))
            self.window.blit(graphic, current_loc)
            current_loc[0] += w_factor
            current_loc[1] += h_factor
            pygame.time.delay(1)
            pygame.display.update()
        self.reset_keys()
        pygame.mixer.Sound.play(card_toss_sound)
    # Função que dá uma carta para o jogador/dealer: -----------------#
    def deal_a_card(self, person, deck, hand, split=False):
        if person == "dealer_down":
            card = "down"
            graphic = pygame.image.load("card.png")
        else:
            card = deck.pop(0)
            cardname = "{a}{b}.png".format(a=str(card[0]), b=card[1])
            graphic = pygame.image.load(cardname)
        self.move_card(graphic, person, hand, split)
        hand[0].append(card)
        self.check_events()
        return hand, deck
    # Função para checar o valor da mão de um indivíduo: ---------------------------------#
    def check_hand_value(self, hand):
        hand[1] = 0
        for card in hand[0]:
            if type(card[0]) == int:
                hand[1] += card[0]
            elif card[0] in ["j", "q", "k"]:
                hand[1] += 10
            elif card[0] == "a":
                hand[1] += 11
        for card in hand[0]:
            if hand[1] > 21:
                if card[0] == "a":
                    hand[1] -= 10
                else: 
                    pass
            else: 
                break
        if hand[1] > 21:
            hand[1] = "bust"
        elif hand[1] == 21 and len(hand[0]) == 2:
            hand[1] = "blackjack"
        elif hand[1] < 21:
            pass
        return hand
    #Função que compara as mãos do jogador e do dealer: ----------------------------------#
    def compare_hands(self, dealer_hand, player_hand, player_bet, player_balance):
        bet = player_bet
        if type(player_hand[3]) == list:
            bet = player_bet[0]
        if dealer_hand[1] == "blackjack":
            if player_hand[1] == "blackjack":
                    modifier = (player_hand[2] * 2) + bet
            else:
                modifier = player_hand[2] * 2
        elif player_hand[1] == "blackjack":
            modifier = (2 * bet) + (bet//2)
        elif player_hand[1] == "bust":
            modifier = 0
        elif dealer_hand[1] == "bust":
            modifier = 2 * bet
        elif dealer_hand[1] == player_hand[1]:
            modifier = bet
        elif dealer_hand[1] > player_hand[1]:
            modifier = 0
        elif dealer_hand[1] < player_hand[1]:
            modifier = 2 * bet
        player_balance += modifier
        if type(player_hand[3]) == list:
            bet = player_bet[1]
            if dealer_hand[1] == "blackjack":
                if player_hand[1] == "blackjack":
                        modifier = (player_hand[2] * 2) + bet
                else:
                    modifier = player_hand[2] * 2
            elif player_hand[1] == "blackjack":
                modifier = (2 * bet) + (bet//2)
            elif player_hand[1] == "bust":
                modifier = 0
            elif dealer_hand[1] == "bust":
                modifier = 2 * bet
            elif dealer_hand[1] == player_hand[1]:
                modifier = bet
            elif dealer_hand[1] > player_hand[1]:
                modifier = 0
            elif dealer_hand[1] < player_hand[1]:
                modifier = 2 * bet
            player_balance += modifier
        return player_balance
    #Função que determina a tela de game over: ---------------------------------------------#
    def game_over_screen(self, game_over):
        if game_over == "Lost":
            image = pygame.image.load("Lost screen.png")
            self.window.blit(image, (255, 202))
            pygame.display.update()
        elif game_over == 100:
            image = pygame.image.load("Equal screen.png")
            self.window.blit(image, (255, 202))
            pygame.display.update()
        elif game_over < 100:
            image = pygame.image.load("Lost money screen.png")
            self.window.blit(image, (255, 202))
            self.write(str(100 - game_over), 60, casino_font, (255, 255, 255), 335, 351, "midleft")
            pygame.display.update()
        elif game_over > 100:
            image = pygame.image.load("Won screen.png")
            self.window.blit(image, (255, 202))
            self.write(str(game_over - 100), 60, casino_font, (255, 255, 255), 335, 351, "midleft")
            pygame.display.update()
        pygame.time.delay(60)
    #Função que escreve o balanço do jogador: -----------------------------------------#
    def update_pb(self, player_balance):
        self.window.blit(balance_image, (0, 0))
        self.write(str(player_balance), 40, casino_font, (255, 255, 255), 650, 50, "midleft")
        pygame.display.update()
    #Função que desenha o chip: --------------------------------------------------------#
    def draw_chip(self, player_bet, insurance=False, split=False):
        pygame.mixer.Sound.play(chip_sound)
        if split == "first":
            graphic = poker_chip_game_red
            init_loc = (200, 300)
            self.window.blit(graphic, init_loc)
            self.write(str(player_bet), 30, casino_font, (255, 255, 255), init_loc[0] + 35, init_loc[1] + 36)
            init_loc = (530, 300)
            self.window.blit(graphic, init_loc)
            self.write(str(player_bet), 30, casino_font, (255, 255, 255), init_loc[0] + 35, init_loc[1] + 36)
        else:
            if split == 1:
                if insurance != 0:
                    init_loc = (260, 250)
                    graphic = poker_chip_blue
                else:
                    init_loc = (200, 300)
                    graphic = poker_chip_game_red
            elif split == 2:
                if insurance != 0:
                    init_loc = (470, 250)
                    graphic = graphic = poker_chip_blue
                else:
                    init_loc = (530, 300)
                    graphic = poker_chip_game_red
            else:
                if insurance != 0:
                    init_loc = (350, 270)
                    graphic = graphic = poker_chip_blue
                else:
                    init_loc = (480, 330)
                    graphic = graphic = poker_chip_game_red
            self.window.blit(graphic, init_loc)
            self.write(str(player_bet), 30, casino_font, (255, 255, 255), init_loc[0] + 34, init_loc[1] + 36)
        pygame.display.update()
    #Função da ação "split": -----------------------------------------#
    def split(self, player_hand, player_balance, player_bet, new_deck, dealer_hand):
        #Setup inicial para dividir as cartas:
        self.reset_keys()
        player_balance -= player_bet
        self.update_pb(player_balance)
        player_hand[3] = [[player_hand[0][1]], 0, 0, "s"]
        player_hand[3] = self.check_hand_value(player_hand[3])
        player_hand[0] = [player_hand[0][0]]
        player_hand = self.check_hand_value(player_hand)
        right = pygame.image.load("right.png")
        left = pygame.image.load("left.png")
        temp = pygame.image.load("temp.png")
        image = pygame.image.load("Game Screen Split.png")
        self.window.blit(image, (0, 0))
        pygame.display.update()
        cardname = "{a}{b}.png".format(a=str(player_hand[0][0][0]), b=player_hand[0][0][1])
        card1 = pygame.image.load(cardname)
        cardname = "{a}{b}.png".format(a=str(player_hand[3][0][0][0]), b=player_hand[3][0][0][1])
        card2 = pygame.image.load(cardname)
        #Dividir cartas:
        final_loc_card1 = 170
        final_loc_card2 = 500
        card1_fac = (final_loc_card1 - 300)/50
        card2_fac = (final_loc_card2 - 330)/50
        current_loc_card1 = 300
        current_loc_card2 = 330
        while current_loc_card1 > final_loc_card1:
            self.window.blit(image, (0, 0))
            self.window.blit(card1, (current_loc_card1, 406))
            self.window.blit(card2, (current_loc_card2, 406))
            current_loc_card1 += card1_fac
            current_loc_card2 += card2_fac
            pygame.time.delay(1)
            pygame.display.update()
        self.draw_chip(player_bet, False, "first")
        player_bet = [player_bet, player_bet]
        pygame.display.update()
        #Dar mais duas cartas:
        player_hand, new_deck = self.deal_a_card("player", new_deck, player_hand, 1)
        player_hand[3], new_deck = self.deal_a_card("player", new_deck, player_hand[3], 2)
        player_hand = self.check_hand_value(player_hand)
        player_hand[3] = self.check_hand_value(player_hand[3])
        self.window.blit(left, (0, 0))
        pygame.display.update()
        #Turno para o primeiro par:
        player_hand, player_balance, player_bet[0], new_deck = self.player_turn(player_hand, player_balance, player_bet[0], new_deck, dealer_hand, 1)
        self.reset_keys()
        if not self.playing:
            self.ESC = True
            return 0, 0, 0, 0
        player_hand = self.check_hand_value(player_hand)
        self.window.blit(temp, (0, 0))
        self.window.blit(right, (0, 0))
        pygame.display.update()
        #Turno para o segundo par:
        player_hand[3], player_balance, player_bet[1], new_deck = self.player_turn(player_hand[3], player_balance, player_bet[1], new_deck, dealer_hand, 2)
        if not self.playing:
            self.ESC = True
            return 0, 0, 0, 0
        self.window.blit(temp, (0, 0))
        pygame.display.update()
        self.reset_keys()
        player_hand[3] = self.check_hand_value(player_hand[3])
        return player_hand, player_balance, player_bet, new_deck





#CREDITS:
#Casino Font Family:
#Vladimir Nikolic @https://www.coroflot.com/vladimirnikolic/profile
#Icon Image:
#Eucalyp @https://www.flaticon.com/authors/eucalyp
#Cards:
#Byron Knoll @http://code.google.com/p/vector-playing-cards/
