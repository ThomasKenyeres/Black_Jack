import time
from random import randint

class Animations():
    def __init__(self):
        self.thinking_pics = [
            "_      *",
            " _    * ",
            "  _  *  ",
            "   _*   ",
            "   *_   ",
            "  *  _  ",
            " *    _ ",
            "*      _",
            " *    _ ",
            "  *  _  ",
            "   *_   ",
            "   _*   ",
            "  _  *  ",
            " _    * "
        ]


    def Loading(self, string):
        for j in range(0, 8):
            for i in range(0, len(self.thinking_pics)):
                t = str(string) + str(self.thinking_pics[i-1])
                print(t, end="\r\r")
                time.sleep(0.03)




Animations = Animations()


class MultipleChars():
    def __init__(self):
        pass

    def PrintSpace(n):
        return str((" ")*n)

#Animations.Loading("Thinking")


class Deck():
    def __init__(self):
        self.cards = []

        self.colors = ["Spades", "Diamonds", "Hearts", "Clubs"]
        self.values = ["2", "3", "4", "5", "6", "7", "8","9", "10", "A", "J", "Q", "K"]

        #creating deck cards
        for color in self.colors:
            for value in self.values:
                self.cards.append({"value": value, "color": color, "used": False})

    def pick_card(self, color, value):
        for i in range(len(self.cards)):
            if self.cards[i]["used"] == False and self.cards[i]["value"] == value and self.cards[i]["color"] == color:
                self.cards[i]["used"] = True

    def print_cards(self):
        for card in self.cards:
            print (card)

    def pick_random_card(self):
        unused = []
        for card in self.cards:
            if card["used"] == False:
                unused.append({"color": card["color"], "value": card["value"]})
        random_pick = randint(0,len(unused)-1)
        self.pick_card(unused[random_pick]["color"], unused[random_pick]["value"])





"""
Deck = Deck()
Deck.pick_card("Spades", "6")
Deck.pick_random_card()
Deck.print_cards()
"""
