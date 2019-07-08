#!/usr/bin/env python3
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
thegameStyles = ['rocker', 'random', 'reflect', 'cycle']

"""The Player class is the parent class for all of the Players
in this game"""
# MR PANDA's Game

class My_Soldier_Players:
    # Explaining the players Moves:
    def __init__(self):
        self.my_challenger_move = random.choice(moves)
        self.my_last_move = random.choice(moves)
# the game will start with 0 Score.
        self.score = 0
        
# (1) player that always plays 'rock'

    def move(self):
        return 'rock'
#  what is learn ?

    def learn(self, my_move, theCH_move):
        self.my_challenger_move = theCH_move
        self.my_last_move = my_move

# (2) when the player chooses the moves randomly:


class RandomPlayerSpace(My_Soldier_Players):
    def move(self):
        return random.choice(moves)

# (3) player that cycles through the three moves :


class CyclePlayerIquana(My_Soldier_Players):
    def move(self):
        if self.my_last_move == 'rock':
            return 'paper'
        elif self.my_last_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

# (4) player that remembers and imitates what the human player did in the previous round:


class ReflectPlayerMirror(My_Soldier_Players):
    def move(self):
        return self.my_challenger_move


class HumanPlayerMoon(My_Soldier_Players):
    def move(self):
        while(True):

            userinput = input('its on YOU!:  ').lower()
            if userinput in moves:
                return userinput
            else:
                print('Opps!that was close!')


# Explainig who will get more points in :

def beats(first, second):
    return ((first == 'rock' and second == 'scissors') or
            (first == 'scissors' and second == 'paper') or
            (first == 'paper' and second == 'rock'))

# definning who is going to play with the class:


class Game:
    def __init__(self, ply1, ply2):
        self.ply1 = ply1
        self.ply2 = ply2

    def play_round(self):
        move1 = self.ply1.move()
        move2 = self.ply2.move()
        print(f"Ply 1: {move1}  Ply 2: {move2}")
        self.ply1.learn(move1, move2)
        self.ply2.learn(move2, move1)

        if beats(move1, move2):
            print('WINNER WINNER CHICKEN DINNER!!! PLAYER 1 WINS! ')
            self.ply1.score += 1

        elif beats(move2, move1):
            print('WINNER WINNER CHICKEN DINNER!! PLAYER 1 WINS!')
            self.ply2.score += 1
        else:
            print('ITS A TIE SOLDIER U HAVE TO BREAK IT!')

    def play_game(self):
        print ("choose between;rock,paper or scissors:") 
        print("THE WAR HAS STARTED MOVE IT !!!")
        print("")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
            print(" Try Harder!.")
            print("")
            print("AND THE FINAL SCOREEE ISSSS !:")
            print(
            f"Ply 1: {self.ply1.score}  Ply 2: {self.ply2.score}")
            print("Soldier you should always remember that It’s hard to beat a person who never gives up so CHEER UP!!!")
            print("")
        if self.ply1.score > self.ply2.score:
           print("PLAYER 1 YOU DID IT WOHOOO")
        elif self.ply1.score < self.ply2.score:
           print("AND THE WINNER IS >>>>> PLAYER 2 <<<<<")
        else:
            print("YOU WON !!,OH SORRY ITS APRIL JOKE LOSERS :P")
if __name__ == '__main__':
    
    while(True):

        
        thegameStyle = input(
            "Are you ready to start the war against Mr panda team? Show me what you got  ;)!   ").lower()
        if thegameStyle in thegameStyles:
            break

    if thegameStyle == "rocker":
        game = Game(HumanPlayerMoon(), My_Soldier_Players())
    elif thegameStyle == "random":
        game = Game(HumanPlayerMoon(), RandomPlayerSpace())
    elif thegameStyle == "reflect":
        game = Game(HumanPlayerMoon(), ReflectPlayerMirror())
    else:
        game = Game(HumanPlayerMoon(), CyclePlayerIquana())

    game.play_game()

