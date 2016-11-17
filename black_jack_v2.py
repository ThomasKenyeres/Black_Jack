import random
import sys
import time

#####
from cards_opt import *
from special_functions import *
#####


cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
coins = 500
new_round = 1
user_win = 0
host_win = 0
host_coins = 0


def PrintCardsAndSum(person, cards, sum):
    if person == "user":
        print("YOUR CARDS: " + MultipleChars.PrintSpace(50))
    if person == "host":
        print("MY CARDS: " + MultipleChars.PrintSpace(50))

    card_objs = []

    for card in cards:
        colors = ["Diamonds", "Clubs", "Hearts", "Spades"]
        clr = randint(0, len(colors)-1)
        card_objs.append(Card(colors[clr], card))



    CardPrinter.PrintCards(card_objs)

    print("VALUE OF CARDS: " + str(sum))

def open_high_scores():
    file_ = []
    try:
        file_ = open("Scores.csv", "r+")
    except IOError:
        fp = open("Scores.csv", "w+")

    scores = []
    final_scores = []

    for line in file_:
        scores.append(line.strip().split(","))

    scores = sorted(scores, key=lambda player: (int(player[1]), 1000-(int(player[2]))))

    final_scores = scores[::-1]


    print("┌─────────────────────────High Scores────────────────────────┐")
    print("│Username ----- Wins ----- Losts ----- Coins ----- Lost coins│")

    for players in final_scores:
        usern = players[0] + " "*(16-int(len(str(players[0]))))
        wins = players[1] + " "*(12-int(len(str(players[1]))))
        losts = players[2] + " "*(11-int(len(str(players[2]))))
        coins = players[3] + " "*(13-int(len(str(players[3]))))
        lost_coins = players[4] + " "*(8-int(len(str(players[4]))))
        print("│" + usern + str(wins) + str(losts) + str(coins) + str(lost_coins) + "│")

    print("└────────────────────────────────────────────────────────────┘")






game = True

while game:

    while new_round == 1: #running until the user quit the program
        while coins > 49:
            user_cards = []
            host_cards = []
            insert_coin = 0
            play = 0
            host_start = 0
            print("Your remaining coins: ", coins)

            while play == 0: #running until the correct coin input
                insert_coin = int(input("How many coins do you want to play: "))

                if int(insert_coin) > 49:
                    if int(insert_coin) > int(coins):
                        print("You do not have enough coins!")
                    if (int(insert_coin) > 49) and (int(insert_coin) <= int(coins)):
                        play = 1

                if int(insert_coin) <= 49:
                    print("The minimum limit is 50.")

            Animations.Loading("Deck mixing")


            i = 1
            while i <= 2: #random cards for the user and host
                u = random.randint(0, len(cards) - 1)
                h = random.randint(0, len(cards) - 1)
                user_cards.append(cards[u])
                host_cards.append(cards[h])
                i += 1

            e = 1
            while e == 1: #user - run until one of the 'if' is not completed

                q = ""
                sum_user = 0

                for card in user_cards: #sum the value of the user hand
                    try:
                        if float(card).is_integer:
                            sum_user += int(card)
                    except ValueError:
                        if card == "A":
                            if sum_user > 10:
                                sum_user += 1
                            else:
                                sum_user += 11
                        else:
                            sum_user += 10

                #print("Your cards: ", user_cards, "\nThe value is: ", sum_user)
                PrintCardsAndSum("user", user_cards, sum_user)

                if sum_user <= 20: #check the value of the user hand
                    q = input("Do you want to take another card? Y/N: ")

                    if (q == "y") or (q == "Y"):
                        u = random.randint(0, len(cards) - 1)
                        user_cards.append(cards[u])
                    if (q == "n") or (q == "N"):
                        host_start = 0
                        e = 0
                        break

                elif sum_user == 21:
                    print("BLACK JACK! YOU WON!")
                    user_win += 1
                    coins += insert_coin * 2
                    r = input("Do you want a new turn? Y/N: ")
                    if (r == "y") or (r == "Y"):
                        new_round = 1
                        host_start = 1
                        break
                    if (r == "n") or (r == "N"):
                        new_round = 0
                        host_start = 2
                        break

                elif sum_user > 21:
                    print("YOU LOST!")
                    host_win += 1
                    e = 0
                    coins -= insert_coin
                    host_coins += insert_coin
                    r = input("Do you want a new turn? Y/N: ")
                    if (r == "y") or (r == "Y"):
                        new_round = 1
                        host_start = 1
                        break
                    if (r == "n") or (r == "N"):
                        new_round = 0
                        host_start = 2

            if host_start == 0:
                print("")

                e = 1
                while e == 1: #host - run until one of the 'if' is not completed

                    sum_host = 0

                    for card in host_cards: #sum the value of the user hand
                        try:
                            if float(card).is_integer:
                                sum_host += int(card)
                        except ValueError:
                            if card == "A":
                                if sum_host > 10:
                                    sum_host += 1
                                else:
                                    sum_host += 11
                            else:
                                sum_host += 10

                    #print("My cards: ", host_cards, "\nThe value is: ", sum_host)
                    PrintCardsAndSum("host", host_cards, sum_host)


                    if sum_host == 21: #check the value of the host hand
                        print("BLACK JACK! I WON!")
                        host_win += 1
                        coins -= insert_coin
                        host_coins += insert_coin
                        r = input("Do you want a new turn? Y/N: ")
                        if (r == "y") or (r == "Y"):
                            new_round = 1
                            break
                        if (r == "n") or (r == "N"):
                            new_round = 0
                            host_start = 2
                            break

                    elif sum_host <= 20:
                        if sum_host < sum_user:
                            u = random.randint(0, len(cards) - 1)
                            host_cards.append(cards[u])

                        elif sum_host >= sum_user:
                            e = 0
                            print("SORRY! I WON!")
                            host_win += 1
                            coins -= insert_coin
                            host_coins += insert_coin
                            r = input("Do you want a new turn? Y/N: ")
                            if (r == "y") or (r == "Y"):
                                new_round = 1
                                break
                            if (r == "n") or (r == "N"):
                                new_round = 0
                                host_start = 2
                                break

                    elif sum_host > 21:
                        print("I LOST!")
                        user_win += 1
                        coins += insert_coin #* 2
                        e = 0
                        r = input("Do you want a new turn? Y/N: ")
                        if (r == "y") or (r == "Y"):
                            new_round = 1
                        if (r == "n") or (r == "N"):
                            new_round = 0
                            host_start = 2
                            break

                    Animations.Loading("Thinking")


            if coins <= 49:
                print("You do not have enough coins! Game Over!")
                print("Your wins: ", user_win)
                print("My wins: ", host_win)
                print("Your remained coins: ", coins)
                print("Your lost coins: ", host_coins)
                #quit()

            elif host_start == 2:
                print("Your wins: ", user_win)
                print("My wins: ", host_win)
                print("Your remained coins: ", coins)
                print("Your lost coins: ", host_coins)
                #quit()

            name = input("Give your name: ")
            file_ = open("Scores.csv", "a+")
            file_.write(str(name) + "," + str(user_win) + "," + str(1) + "," + str(coins) + "," + str(host_coins))
            file_.close()


            open_high_scores()
        game = False
