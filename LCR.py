# Import the random library for dice use
import random

# Creates the dice class
class Dice:
    def __init__(self):
        self.side = 0
# Create a function to roll the dice for each side of the dice
    def toss(self):
        self.side = random.randint(1, 6)
        return self.side


def main():
    # Variable to hold the value of chips in the center/pot
    pot = 0
    # Initialize the dice object
    dice = Dice()
    # Initialize the round variable to track which round the game is on
    round = 0
    # Initialize the variable that determines when the game is over
    game = False
    # Initialize a list that holds th           e players
    playerList = []
    # Loop will catch ValueError if a non-integer is entered and prompt the user to try again
    while True:
        try:
            # Variable that contains the amount of players input from the users
            numOfPlayers = int(input('How many players? '))
        except ValueError:
            print('\nError! Must be an integer. Try again.\n')
        else: break
    # Adds each player to the list input from the users
    for x in range(0, numOfPlayers):
        playerList.append(input("\nEnter Player " + str(x + 1) + "\'s name: \n"))
    # Initializes a list that contains the scores for each player
    scores = [3] * numOfPlayers
    # User presses Enter to start the game
    input("\nPress Enter to start the game!")
    # Loop that controls the game
    while (game == False):
        # Displays which round the game is on
        round = round + 1
        print("\n------------------------------------------\n" + "Round " + str(round))
        # Displays how many chips are in the pot
        if pot == 1:
            print('\nThere is ' + str(pot) + ' chip in the pot\n')
        else: print('\nThere are ' + str(pot) + ' chips in the pot\n')
        # Initialize variable that will be used for playerlist and score indexing
        x = -1
        # This loop controls rolling the dice and calculating the score
        while (x < numOfPlayers - 1) and (game == False):
            x = x + 1
            print("")
            print("It's " + playerList[x] + "'s turn. " + playerList[x] + " has " + str(scores[x]) + " chips.")
            # Determine how many dice the player has to roll based on the amount of chips the player has
            if scores[x] < 1:
                print(playerList[x] + ', no chips, no dice.')
                numOfDice = 0
            elif scores[x] >= 3:
                numOfDice = 3
            else:
                numOfDice = scores[x]

            if numOfDice > 0:
                input("\nPress Enter to roll your dice")
                # This loop will roll the dice for the user, and distribute the chips to the players and the pot
                for diceCount in range(0, numOfDice):
                    roll = dice.toss()
                    # 1 = L
                    # 2 = C
                    # 3 = R
                    # 4, 5, 6 = dot
                    if roll == 1:
                        print("     You rolled an L!")
                        scores[x] = scores[x] - 1
                        if x == 0:
                            scores[numOfPlayers - 1] = scores[numOfPlayers - 1] + 1
                        else:
                            scores[x - 1] = scores[x - 1] + 1
                    elif roll == 2:
                        print("     You rolled a C!")
                        scores[x] = scores[x] - 1
                        pot = pot + 1
                    elif roll == 3:
                        print("     You rolled a R!")
                        scores[x] = scores[x] - 1
                        if x == numOfPlayers - 1:
                            scores[0] = scores[0] + 1
                        else:
                            scores[x + 1] = scores[x + 1] + 1
                    else:
                        print("     You rolled a dot!")


            # Initialize variable that determines the amount of players remaining
            playersRemaining = 0
            for y in range(0, numOfPlayers):
                if scores[y] > 0:
                    playersRemaining = playersRemaining + 1
            # If there is only one player left, the game is over and the winner is displayed
            if playersRemaining == 1:
                game = True
                print('\nGame!\n')
                for y in range(0, numOfPlayers):
                    if scores[y] > 0:
                        print('This game\'s winner is...*drumroll*... ' + playerList[y] + " with " + str(scores[y]) + " chips!")






# Calls the main function
main()
