import random

def create_deck():
    """Creates a deck of 52 cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Returns the value of a given card."""
    value, _ = card
    if value in ['Jack', 'Queen', 'King']:
        return 10
    elif value == 'Ace':
        return 11
    else:
        return int(value)

def hand_value(hand):
    """Calculates the total value of a hand of cards."""
    value = sum(card_value(card) for card in hand)
    # Adjust for Aces if value is over 21
    num_aces = sum(card[0] == 'Ace' for card in hand)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def play_blackjack():
    """Simulates a game of Blackjack between two players."""
    deck = create_deck()
    player1_hand = [deck.pop(), deck.pop()]
    player2_hand = [deck.pop(), deck.pop()]

    for player_hand in [player1_hand, player2_hand]:
        while hand_value(player_hand) < 17:
            player_hand.append(deck.pop())

    player1_value = hand_value(player1_hand)
    player2_value = hand_value(player2_hand)


    return player1_hand, player1_value, player2_hand, player2_value

# Simulate a game of Blackjack
player1_hand, player1_value, player2_hand, player2_value = play_blackjack()
print(player1_hand, player1_value, player2_hand, player2_value)