#encoding: utf8
import card
import random
from player import Player
from probsMaoFinal import *
import pickle


class StudentPlayer(Player):
    ###GLOBALS TO START

    def __init__(self, name="EU", money=0):
        super(StudentPlayer, self).__init__(name, money)
        self.last_actions = []
        ###
        #Ler ficheiro matrix de persistencia
        ###
        self.fi = open("matrix.data", "rb")
        self.fi.seek(0)
        self.m = pickle.load(self.fi)
        self.fi.close()
        self.turn = 1


    def play(self, dealer, players):
        action = self.choose_from_matrix(dealer, players)

        #nao pode ser asssim
        #tem de ser mais complexo e guardar todas as acooes 
        #q o nosso jogador efectuou numa jogada
        #inves do turno total
        #desta maneira, agora, 
        #apenas guarda a accao final do jogador
        #evidenciado pelos prints na choose_from_matrix
        for p in players:
            if p.player.name == self.name:
                r = p.hand
                # if self.turn == 1:
                #     if card.value(r) == 15:
                #        print "teste"
                #        self.turn =0
              #         return "d"
                if card.value(r) > 19:
                    self.turn =0
                    action = 's'
                    return 's'
                elif card.value(r) < 6:
                    self.turn =0
                    action = 'h'
                    return 'h'
        self.last_actions.append([card.value(dealer.hand), card.value(r), action])
        #print self.last_actions
        
        self.turn =0
        return action


    def bet(self, dealer, players):
        # for p in players:
        #     if p.player.name == self.name:
        #         r = p.hand
        #         ss = probGanharAgora(dealer.hand, r)
        #         sh = probGanharProxRondaStandHit(r, dealer.hand)
        #         hs = probGanharProxRondaHitStand(r, dealer.hand)
        #         hh = probGanharProxRonda(r, dealer.hand)
        #         prob = float(ss+sh+hs+hh)/4
        #         print "teste: "
        #         print p.hand
        #         if prob > 80:
        #             return 5
        #         elif prob > 50:
        #             return 2
        return 1

    def choose_from_matrix(self, dealer, players):
        
        for p in players:
            if p.player.name == self.name:
                r = card.value(p.hand)
        c = card.value(dealer.hand)

        
        l = self.m[r][c]


        nl = [ ]
        for i in l:
            nl.append([i[0], self.success_rate(i[1], i[2])])
        return self.weighted_choice(nl)

    

    def payback(self, prize):
        self.table = 0
        self.pocket += prize
        self.turn = 1
        for i in self.last_actions:
            self.endGame(i, (prize>0))
    
    def endGame(self, turn, won):
        x = turn[0]
        y = turn[1]
        action = turn[2]

        l = list(self.m[x][y])
        for i in l:
            if i[0] == action:
                if won:
                    i[1] += 1
                else:
                    i[2] += 1
        self.m[x][y] = l
        return 1

    # #tem de ser mod para guardar todas as accoes
    # #com o winsn e lose
    # def increase_weight(self):
    #     for i in self.last_actions:


    #     if self.last_actions != None:
    #         dealer = self.last_action[0]
    #         players = self.last_action[1]
    #         action = self.last_action[2]
    #     else:
    #         return
        
    #     try:
    #         l = self.m[r][c]
    #     except:
    #         r = 0
    #         c = 0

    #     l = self.m[r][c]

    #     for a in l:

    #         if a[0]==action:
    #             weight = a[1]
    #             #weight *= 1.05
    #             #new_weight = (weight*105)/100
    #             if weight < 0: 
    #                 weight = 0
    #             new_weight = weight + 10
    #             a[1] = new_weight

    #     self.m[r][c] = l

    #     return 

    #tem de ser mod para guardar todas as accoes
    #com o winsn e lose
    # def decrease_weight(self):

    #     if self.last_action != None:
    #         dealer = self.last_action[0]
    #         players = self.last_action[1]
    #         action = self.last_action[2]
    #     else:
    #         return

    #     for p in players:
    #             if p.player.name == self.name:
    #                r = card.value(p.hand)
    #     c = card.value(dealer.hand)
        
    #     try:
    #         l = self.m[r][c]
    #     except:
    #         r = 0
    #         c = 0

    #     l = self.m[r][c]

    #     for a in l:

    #         if a[0]==action:
    #             weight = a[1]
    #             #weight *= 99.95
    #             #new_weight = (weight*95)/100
                
    #             if weight < 0: 
    #                 weight = 0
    #             if weight == 0:
    #                 new_weight = 0
    #             else:
    #                 new_weight = weight-10
    #             a[1] = new_weight

    #     self.m[r][c] = l

    #     return 


    def close_matrix(self):
        ###
        #Escrever matrix de persistencia
        ###
        fo = open("matrix.data", "wb")
        fo.seek(0)
        fo.truncate()
        fo.seek(0)
        pickle.dump(self.m, fo)
        fo.close()

    def weighted_choice(self, choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w >= r:
                return c
            upto += w

    #returns the percentage of wins
    def success_rate(self, wins, losses):

        t = wins + losses
        if t == 0:
            return 0
        return (wins*100) / t
        
