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
        Initialise Card object
        :param suit: str
            The suit of the card
        :param rank: str
            The rank of the card
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Deck class used to create deck of 52 cards
    """

    def __init__(self):
        """
        Initialise Deck object and create 52 card objects inside
        """
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __len__(self):
        """
        The length of the Deck of cards
        :return: int
            Number of cards in the Deck
        """
        return len(self.all_cards)

    def __str__(self):
        for card in self.all_cards:
            print(card)



new_card = Card(suits[1], ranks[1])
print(new_card, new_card.value)

new_deck = Deck()
print(new_deck.all_cards[0])
print(len(new_deck))
print(new_deck)
