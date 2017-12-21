import card
from card import Card

baralho = [1,2,3,4,5,6,7,8,9,10,11,12,13]


def probGanharAgora(dealerHand, myHand):
	x=0
	myVal = card.value(myHand)
	if (myVal == 21) or (card.value(dealerHand) > 21):
		print "100%\n"
		return float(100)
	if myVal > 21:
		print "0%"
		return float(0)
	for i in baralho:
		carta = Card(suit=0, rank=i)
		dealerVal = card.value(dealerHand + [carta])
		if (dealerVal > myVal) and (dealerVal <= 21):
			x = x+1
	p = 100-(float(x)/float(13))*100
	#print ("probabilidade de ganhar agora: %2.2f%%"% (p))
	return p

def probGanharProxRonda(myHand, dealerHand): #os dois fazem hit
	x=0 #em que o dealer ganha
	c=0 #casos totais
	for i in baralho:
		carta = Card(suit=0, rank=i)
		myVal = card.value(myHand + [carta])
		for k in baralho:
			cartak = Card(suit=0, rank=k)
			for j in baralho:
				cartaj = Card(suit=0, rank=j)
				dealerVal = card.value(dealerHand + [cartak] + [cartaj])
				if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
					x = x+1
					c = c+1
				else:
					c = c+1
	p = 100-(float(x)/float(c))*100
	#print ("probabilidade de ganhar na proxima jogada fazendo os 2 hit: %2.2f%%"% (p))
	return p

def probGanharProxRondaHitStand(myHand, dealerHand): #dealer faz hit e jog faz stand
	x=0
	c=0
	myVal = card.value(myHand)
	for i in baralho:
		carta = Card(suit=0, rank=i)
		for j in baralho:
			cartaj = Card(suit=0, rank=j)
			dealerVal = card.value(dealerHand + [carta] + [cartaj])
			if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
				x = x + 1
				c = c + 1
			else:
				c = c + 1
	p = 100-(float(x)/float(c))*100
	#print ("probabilidade de ganhar na proxima jogada fazendo stand e o dealer hit: %2.2f%%"% (p))
	return p

def probGanharProxRondaStandHit(myHand, dealerHand): #dealer faz stand e jog faz hit
	x=0 #em que o dealer ganha
	c=0 #casos totais
	for i in baralho:
		carta = Card(suit=0, rank=i)
		myVal = card.value(myHand + [carta])
		for k in baralho:
			cartak = Card(suit=0, rank=k)
			dealerVal = card.value(dealerHand + [cartak])
			if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
				x = x+1
				c = c+1
			else:
				c = c+1
	p = 100-(float(x)/float(c))*100
	#print ("probabilidade de ganhar na proxima jogada fazendo hit e o dealer stand: %2.2f%%"% (p))
	return p
