#BLACKJACK GAME
import random

class Dealer:
    def __init__(self, initial_hand):
        self.dealer_hand = initial_hand
        
    def show_hand(self):
        return self.dealer_hand[0]

    def show_full_hand(self):
        return self.dealer_hand

    def hand_value(self):
        hand_value = 0
        for card_type in self.dealer_hand:
            card_value = card_type.rstrip(card_type[-1])
            if card_value.isnumeric() == True:
                card_value = int(card_value)
            elif card_value.lower() == 'a':
                card_value = 11
            else:
                card_value = 10
            hand_value += card_value
        return hand_value

    def dealer_move(self):
        #if value of dealer_hand < 17, dealer_move == 'hit'
        if self.hand_value() < 17:
            return 'hit'
        elif self.hand_value() > 21:
            return 'bust'
        elif self.hand_value() == 21:
            return '21'
        else:
            return 'stay'
        

class Player:
    def __init__(self, initial_hand):
        self.player_hand = initial_hand    

    def show_hand(self):
        return self.player_hand

    def hand_value(self):
        hand_value = 0
        for card_type in self.player_hand:
            card_value = card_type.rstrip(card_type[-1])
            if card_value.isnumeric() == True:
                card_value = int(card_value)
            elif card_value.lower() == 'a':
                card_value = 11
            else:
                card_value = 10
            hand_value += card_value
        return hand_value

class Board:
    def __init__(self):
        self.deck = self.build_deck()
        self.shuffle()
        self.game_over = False

    def build_deck(self):
        cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        suits = ['h', 'c', 's', 'd']
        deck = []
        for card in cards:
            for suit in suits:
                card_type = str(card) + suit
                deck.append(card_type)
        # print(f"before {deck}") 
        return deck

    def shuffle(self):
        random.shuffle(self.deck)
        # print(f"after {self.deck}")

    def deal_a_card(self):
        return self.deck.pop()

class UI():
    def __init__(self):
        self.board = Board()
        self.player = Player(self.initialize_hand())
        self.dealer = Dealer(self.initialize_hand())

    def initialize_hand(self):
        card1 = self.board.deal_a_card()
        card2 = self.board.deal_a_card()
        return [card1,card2]

    def play_game(self):
        
        if self.player.hand_value() == 21:
            print(f"Blackjack!")
            print(f"Your Hand: {self.player.show_hand()}")
            print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
        print(f"Your Hand: {self.player.show_hand()}")
        print(f"Dealer's hand: {self.dealer.show_hand()}")

        player_move = input('Would you like to hit or stay? ').strip()
        while player_move != 'stay':
            if player_move == 'hit':
                self.player.player_hand.append(self.board.deal_a_card())
                # print(self.board.deck)
            else:
                print(f"Your Hand: {self.player.show_hand()}")
                self.player.hand_value()
            if int(self.player.hand_value()) > 21:
                print(f"Oh shoot! You busted! Better luck next time...")
                print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
                print(f"Your Hand: {self.player.show_hand()}")
                return
            print(f"Your Hand: {self.player.show_hand()}")
            print(f"Dealer's hand: {self.dealer.show_hand()}")
            player_move = input("Would you like to hit or stay? ").strip()


        dealer_move = self.dealer.dealer_move()
        while dealer_move != 'stay':
            if dealer_move == "hit":
                self.dealer.dealer_hand.append(self.board.deal_a_card())
                print('HITTTTTT')
            elif dealer_move == '21':
                print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
                print('WINNER WINNER')
                break
            elif dealer_move == 'bust':
                print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
                print('BUSTED MF')
                return
            else:
                print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
                print('ELSE WTF')
            print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
            dealer_move = self.dealer.dealer_move()


        if int(self.player.hand_value()) > int(self.dealer.hand_value()):
            print(f"Congratulations! You have beat the dealer.")
            print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
        elif self.player.hand_value() == self.dealer.hand_value():
            print (f"It's a tie! Would you like to play again?")
            print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
        else:
            print(f"Tough cookies, toots! The dealer got you beat.")
            print(f"Dealer's Hand: {self.dealer.show_full_hand()}")
        
ui = UI()
ui.play_game()        

player_input = input("Do you want to play again? ").strip()
while player_input.lower() == 'yes':
    new_ui = UI()
    new_ui.play_game()
    player_input = input("Do you want to play again? ").strip()

