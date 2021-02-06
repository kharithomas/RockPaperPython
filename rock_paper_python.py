# create a rock, paper, scissors game in python
# added best 2 out of 3
# added basic error handling

import random


class Game:

    def __init__(self):
        self.res = [0, 0]

    def print_score(self):
        print(f"\nYou: {self.res[0]}\nComputer: {self.res[1]}\n")

    def play_game(self):
        # start
        while self.res[0] < 3 and self.res[1] < 3:
            # player, computer pick
            computer = random.choice(['r', 'p', 's'])
            user = input('Pick your choice: ')

            # print score
            if user.lower() == 'score':
                self.print_score()
                continue
            
            # error handling
            if user.lower() != 'r' and user.lower() != 's' and user.lower() != 'p':
                print('Please enter a valid option!\n')
                continue

            # rules: r>s, s>p, p>r
            if user.lower() == 'r' and computer == 's' \
                    or user.lower() == 's' and computer == 'p' \
                    or user.lower() == 'p' and computer == 'r':
                print(f"Computer picked: {computer}\n")
                print('You win!')
                self.res[0] += 1
            elif user.lower() == computer:
                print('Draw. Try again!\n')
                continue
            else:
                print(f"Computer picked: {computer}\n")
                print('You lose!')
                self.res[1] += 1

        # print final score
        self.print_score()

game = Game()
game.play_game()
