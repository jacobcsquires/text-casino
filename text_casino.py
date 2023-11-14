import random
import time

# Starting balance
total = 100

running = True
while running:

    game = input("Here are the games:\n\t1. Higher or Lower\n\t2. Steps\n\t3. Multipier\n\t4. Russian Roulette\nWhich game would you like to play? ")

    if game == "quit":
        running = False
    else:
        # Higher
        if game == "1" or game == "higher or lower":
            game_running = True

            edge = 0.01

            # Rules
            print("\nHere are the rules:\n\t1. Pick a number 1-100\n\t2. If the number spun is higher than the number you choose, then you win\n\t3. The higher your guess, the bigger the winnings")

            while game_running:

                state = input("\nSpin or Leave? ").lower()

                if state == "spin":

                    # User input
                    bet = float(input("What is your bet? $")).__round__(2)

                    if bet > total:
                        print("You don't have enough money.")
                        time.sleep(1)
                        game_running = False
                        break

                    total -= bet

                    guess = float(input("Pick a number: "))

                    # Spinning
                    print("\nSpinning...\n")
                    time.sleep(3)
                    number = random.randrange(0, 100)
                    print(number)
                    time.sleep(1)

                    # Payout Calculator
                    percentage = (100 - guess) / 100
                    payout = (1 - edge) / percentage

                    if guess < number:
                        game_winnings = (bet * payout).__round__(2)
                        total += game_winnings
                        print("You win!")
                        time.sleep(1)
                        print("Balance: ${:.2f}".format(total))
                        time.sleep(1)
                    else:
                        print("Maybe next time!")
                        time.sleep(1)
                        print("Balance: ${:.2f}".format(total))
                        time.sleep(1)

                elif state == "leave":

                    print("")
                    game_running = False

        # Steps
        if game == "2" or game == "steps":
            game_running = True

            edge = 0.01

            # Rules
            print("\nHere are the rules:\n\t1. For each round, pick a number 1-4\n\t2. If the number you choose is not the unlucky number, you move on to the next round\n\t3. The more rounds you play, the bigger the winnings")

            while game_running:

                state = input("\nPlay or Leave? ").lower()

                if state == "play":

                    # User input
                    bet = float(input("What is your bet? $")).__round__(2)

                    if bet > total:
                        print("You don't have enough money.")
                        time.sleep(1)
                        game_running = False
                        break

                    total -= bet

                    # Initializers
                    payout = 0
                    round = 1

                    playing = True

                    while playing:

                        multiplier = ((1 - edge) / ((3 / 4) ** round)).__round__(2)

                        # Choosing number
                        number = random.randint(1, 4)

                        print(f"\nRound {round}")
                        guess = float(input("Pick a number 1-4: "))

                        if guess != number:
                            print(f"\nYour current multiplier is {multiplier}x")
                            keep_playing = input(f"Would you like to continue to Round {round + 1} (Yes or No)? ").lower()

                            if keep_playing == "yes":
                                round += 1
                            elif keep_playing == "no":
                                payout = bet * multiplier
                                playing = False

                        else:
                            print("Maybe next time!")
                            time.sleep(1)
                            playing = False

                    total += payout
                    print("Balance: ${:.2f}".format(total))
                    time.sleep(1)

                elif state == "leave":

                    print("")
                    game_running = False

        # Multiplier
        if game == "3" or game == "multiplier":
            game_running = True

            edge = 0.01

            multiplier_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.7, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 3.00, 4.00]

            # Rules
            print("\nHere are the rules:\n\t1. For each round, place a bet\n\t2. Each spin will produce a different multiplier which will affect your bet")

            while game_running:

                state = input("\nSpin or Leave? ").lower()

                if state == "spin":

                    # User input
                    bet = float(input("What is your bet? $")).__round__(2)

                    if bet > total:
                        print("You don't have enough money.")
                        time.sleep(1)
                        game_running = False
                        break

                    total -= bet

                    playing = True

                    while playing:

                        # Choosing number
                        number = random.randint(1, 30)

                        multiplier = multiplier_list[number]

                        print("\nSpinning...\n")
                        time.sleep(3)

                        print("{:.2f}x".format(multiplier))
                        time.sleep(1)
                        total += multiplier * bet
                        print("Balance: ${:.2f}".format(total))
                        time.sleep(1)

                        playing = False

                elif state == "leave":

                    print("")
                    game_running = False

        #  Russian Roulette
        if game == "4" or game == "russian roulette":
            game_running = True

            edge = 0.01

            multiplier_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.7, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 3.00, 4.00]

            # Rules
            print("\nHere are the rules:\n\t1. Choose how many bullets go into the chamber (1-6)\n\t2. Spin the barrel and hope it fires a blank\n\t3. The more bullets, the higher your winnings")

            while game_running:

                state = input("\nSpin or Leave? ").lower()

                if state == "spin":

                    # User input
                    bullets = int(input("How many bullets (1-6)? "))
                    bet = float(input("What is your bet? $")).__round__(2)

                    if bet > total:
                        print("You don't have enough money.")
                        time.sleep(1)
                        game_running = False
                        break

                    total -= bet

                    playing = True

                    while playing:

                        # Choosing number
                        number = random.randint(1, 6)

                        print("\nSpinning the barrel...\n")
                        time.sleep(3)

                        if (number / 6) > (bullets / 6):

                            multiplier = (1 - edge) / ((6 - bullets) / 6)

                            payout = (bet * multiplier).__round__(2)

                            print("You survived.")
                            time.sleep(1.5)
                            total += payout
                            print("Balance: ${:.2f}".format(total))
                            time.sleep(1)

                        else:
                            print("You shot yourself.")
                            time.sleep(1.5)
                            print("Balance: ${:.2f}".format(total))
                            time.sleep(1)

                        playing = False

                elif state == "leave":

                    print("")
                    game_running = False
