'''
Connor Kissack
Tic Tac Toe
October 6, 2020
'''
# Welcome to my Tic Tac Toe Board
# draw board
# choose number of players 0, 2
# choose x or o
# random Pick who goes first
# Place first entry on the board
# Gameplay
# Check for winning or tie condition
# Outcome message
# ASCII art
# Would you like to play again message if y refresh if n exit

print("Welcome to my Tic-Tac-Toe Board")
num_of_players = input("Choose the number of players. Valid inputs are: 0, 1, or 2 ")
print("You have chosen", num_of_players, "players" )
choose_x_or_o = input("Choose X or O")
uppercase_xo = choose_x_or_o.upper()
print("You have chosen", uppercase_xo)
# print(type(uppercase_xo))
# This code is stating what the player is choosing and what is chosen for the 2nd player
if uppercase_xo == 'X':
    print("You have chosen", uppercase_xo, "Player 2 is O")
else:
    print("You have chosen", uppercase_xo, "Player 2 is X")

vertical = [' | | ']
horizontal = ['- - -']




