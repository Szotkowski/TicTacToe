__author__ = "Author: Michael Szotkowski"
__copyright__ = "Copyright (c) 2024 Michael Szotkowski"
__email__ = "Email: xszotko1@mendelu.cz"
__link__ = "Link: https://github.com/Szotkowski/TicTacToe"
__license__ = "License: GPL-3.0 license "

print("\nTicTacToe")
print(__author__)
print(__copyright__)
print(__email__)
print(__link__)
print(__license__)

import sys, random

class Game:
    def __init__(self, size, play_with_robot = False, number_of_victory_in_line = 3):
        self.size = size
        self.matrix = [[" " for i in range(size)] for j in range (size)]
        self.number_of_victory_in_line = number_of_victory_in_line
        self.play_with_robot = play_with_robot
    
    def __str__(self):
        return '+---' * self.size + '+\n' + ''.join(['| ' + ' | '.join(row) + ' |\n' + '+---' * self.size + '+\n' for row in self.matrix])

    def check_victory(self, player):
        #radek
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0]) - self.number_of_victory_in_line + 1):
                if all(self.matrix[i][j+k] == player for k in range(self.number_of_victory_in_line)):
                    print(self)
                    print("Vyhrál " + player + ".")
                    sys.exit(0)

        #sloupec
        for j in range(len(self.matrix[0])):
            for i in range(len(self.matrix) - self.number_of_victory_in_line + 1):
                if all(self.matrix[i+k][j] == player for k in range(self.number_of_victory_in_line)):
                    print(self)
                    print("Vyhrál " + player + ".")
                    sys.exit(0)
        
        #diagonaly
        for i in range(len(self.matrix) - self.number_of_victory_in_line + 1):
            for j in range(len(self.matrix[0]) - self.number_of_victory_in_line + 1):
                if all(self.matrix[i+k][j+k] == player for k in range(self.number_of_victory_in_line)):
                    print(self)
                    print("Vyhrál " + player + ".")
                    sys.exit(0)
        
        #diagonal reverse
        for i in range(len(self.matrix) - self.number_of_victory_in_line + 1):
            for j in range(self.number_of_victory_in_line-1, len(self.matrix[0])):
                if all(self.matrix[i+k][j-k] == player for k in range(self.number_of_victory_in_line)):
                    print("Vyhrál " + player + ".")
                    sys.exit(0)
    
    #does matrix contain O
    def has_O(self):
        return any(cell == "O" for row in self.matrix for cell in row)
    
    #return indexes of O
    def find_O(self):
        return next(((i, j) for i, row in enumerate(self.matrix) for j, cell in enumerate(row) if cell == "O"), None)
    
    #play with robot
    def play_robot(self):
        if self.has_O():
            position = self.find_O()
            row, column = position
            row += random.choice([-1, 1])
            column += random.choice([-1, 1])
            if 0 <= row < self.size and 0 <= column < self.size and self.matrix[row][column] == ' ':
                self.matrix[row][column] = "O"
        else:
            empty_fields = [(i, j) for i in range(self.size) for j in range(self.size) if self.matrix[i][j] == ' ']
            if empty_fields:
                row, column = random.choice(empty_fields)
                self.matrix[row][column] = "O"
        self.check_victory()

    #start
    def start_game(self):
        player = 'X'
        while True:
            print(self)
            try:
                print("Hráč " + player + ".", end = "\n")
                row = int(input("Zadejte řádek: ")) - 1
                column = int(input("Zadejte sloupec: ")) - 1
                if (0 <= row < self.size and 0 <= column < self.size):
                    if self.matrix[row][column] == ' ':
                        self.matrix[row][column] = player
                        self.check_victory(player)
                    else:
                        print("Chyba. Pole je již obsazeno.")
                else:
                    print("Chyba. Zadejte číselné hodnoty(1-" + str(self.size) + ")")
                if (self.play_with_robot):
                    self.play_robot()
                    self.check_victory(player)
                else:
                    player = 'O' if player == 'X' else 'X'
            except ValueError:
                print("Chyba. Zadejte číselné hodnoty(1-" + str(self.size) + ")")
            except KeyboardInterrupt:
                print("\nKonec hry.")
                sys.exit()

game = Game(5, True)
game.start_game()