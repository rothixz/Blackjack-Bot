#!/usr/bin/python
from game import Game
from player import Player
from randomplayer import RandomPlayer
from student import StudentPlayer

if __name__ == '__main__':

    players = [RandomPlayer("EU",100)]

    for i in range(100):
        #print players
        g = Game(players,shoe_size=4, min_bet=1, max_bet=5) 
        #g = Game(players, debug=True)
        g.run()

    
    print "OVERALL: ", players
