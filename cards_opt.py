class Card(object):

    card_values = {
        'A': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]


class CardAscii(object):
    def __init__(self):
        pass

    def ascii_version_of_card(cards, return_string=True):
        # we will use this to prints the appropriate icons for each card
        suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        suits_symbols = ['♠', '♦', '♥', '♣']

        # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]

        for card in cards:
            # "King" should be "K" and "10" should still be "10"
            if card.rank == '10':
                rank = card.rank
                space = ''
            else:
                rank = card.rank[0]
                space = ' '

            # get the cards suit in two steps
            suit = suits_name.index(card.suit)
            suit = suits_symbols[suit]

            # add the individual card on a line by line basis
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))

        # hidden cards do not use string
        if return_string:
            return '\n'.join(result)
        else:
            return result



class CardPrinter():
    def __init__(self):
        pass

    def PrintCards(self, cards):
        print(CardAscii.ascii_version_of_card(cards))




CardPrinter = CardPrinter()




"""
card = Card("Diamonds","5")
card2 = Card("Diamonds", "King")
card3 = Card("Hearts", "7")
cards = [card, card2, card3]

CardPrinter.PrintCards(cards)"""
