from random import shuffle

# Global variables
suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:
    """
    Card class used to create different types of cards.
    """

    def __init__(self, suit, rank):
        """
        Initialise Card object.
        :param suit: str
            The suit of the card.
        :param rank: str
            The rank of the card.
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Deck class used to create deck of 52 cards.
    """

    def __init__(self):
        """
        Initialise Deck object and create 52 card objects inside.
        """
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __len__(self):
        """
        The length of the Deck of cards (number of cards in the Deck).
        :return: int
        """
        return len(self.all_cards)

    def __str__(self):
        """
        Print the names of all cards.
        :return: list
        """
        cards_names = []
        for card in self.all_cards:
            cards_names.append(str(card))
        return f'List of all cards: {cards_names}'

    def shuffle(self):
        """
        In-place method to shuffle the deck of cards.
        :return: None
        """
        shuffle(self.all_cards)

    def deal_card(self):
        """
        Method for dealing a single card from the deck.
        Use pop(0) to take the top card (top card being most left or first in the list).
        :return: Card object
        """
        return self.all_cards.pop(0)


class Player:
    """
    Class used to create the Players.
    """

    def __init__(self, id_num):
        """
        Initialise the Player by giving it ID.
        :param id_num: str
        """
        self.id_num = id_num
        self.all_cards = []

    def __str__(self):
        """
        Special method to print out the player name and the cards he is holding.
        :return: str
        """
        cards_names = []
        for card in self.all_cards:
            cards_names.append(str(card))
        return f'Hello, I am Player number {self.id_num} and here are all my cards {cards_names}'

    def take_card(self, card):
        """
        In-place method to collect a card and put to the bottom of the deck.
        Bottom of the deck is referring to most right or last in the list.
        :param card: Card object
        :return: None
        """
        self.all_cards.append(card)

    def deal_card(self):
        """
        Method for dealing a single card from the deck.
        Use pop(0) to take the top card (top card being most left or first in the list).
        :return: Card object
        """
        return self.all_cards.pop(0)


def select_players():
    """
    Method to ask the user and select the number of virtual players for the game of War.
    :return: int
    """
    val = "INVALID"
    while val not in ["2", "3", "4", "5", "6"]:
        val = input("Select the number of virtual players for the game of War (any number between 2 and 6):")
        if val not in ["2", "3", "4", "5", "6"]:
            print("Invalid user input, try again...")
    return int(val)


# Create a new deck of cards
deck_of_cards = Deck()
# Shuffle the cards in the deck
deck_of_cards.shuffle()
print(deck_of_cards)

# Create the players
players_list = []
for i in range(select_players()):
    players_list.append(Player(str(i + 1)))
# Deal the cards between the players, until there are no more left
while True:
    try:
        for p in players_list:
            p.take_card(deck_of_cards.deal_card())
    except IndexError:
        # When there are no more cards left, Index error will be raised for the pop() method from empty list
        break

# Start the game
# All players deal a card
table_cards = []    # list of cards on the table
for p in players_list:
    table_cards.append(p.deal_card())

# Is there a winner?

'''
for i in range(len(deck_of_cards)%len(players_list)):
    for p in players_list:
        p.take_card(deck_of_cards.deal_card())
for p in players_list:
    print(p.all_cards)

for p in players_list:
    print(p)

new_card = Card(suits[1], ranks[1])
print(new_card, new_card.value)

new_deck = Deck()
print(new_deck.all_cards[0])
print(len(new_deck))
print(new_deck)

new_deck.shuffle()
print(new_deck)
print(new_deck.deal_card())
print(new_deck)
'''
