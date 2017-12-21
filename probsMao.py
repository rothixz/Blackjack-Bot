
baralho = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'A':11, 'K':10, 'D':10, 'V':10}

dealerHand = ['6','2']

myHand = ['2','7', '5']

def handValue(hand):
	v=0
	for i in hand:
		if i=='A':
			if v+11>21:
				v = v+1
			else:
				v = v+11
		else:
			v = v + baralho[i]
	return v
def probGanharAgora(dealerHand, myHand):
	x=0
	myVal = handValue(myHand)
	if (myVal == 21) or (handValue(dealerHand) > 21):
		print "100%\n"
		exit()
	if myVal > 21:
		print "0%"
		exit()
	for i in baralho:
		dealerVal = handValue(dealerHand + [i])
		if (dealerVal > myVal) and (dealerVal <= 21):
			x = x+1
	p = 100-(float(x)/float(13))*100
	print ("probabilidade de ganhar agora: %2.2f%%"% (p))
	return p

def probGanharProxRonda(myHand, dealerHand):
	x=0 #em que o dealer ganha
	c=0 #casos totais
	for i in baralho:
		myVal = handValue(myHand + [i])
		for k in baralho:
			for j in baralho:
				dealerVal = handValue(dealerHand + [k] + [j])
				if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
					x = x+1
					c = c+1
				else:
					c = c+1
	p = 100-(float(x)/float(c))*100
	print ("probabilidade de ganhar na proxima jogada fazendo os 2 hit: %2.2f%%"% (p))
	return p

def probGanharProxRondaHitStand(myHand, dealerHand): #dealer faz hit e jog faz stand
	x=0
	c=0
	myVal = handValue(myHand)
	for i in baralho:
		for j in baralho:
			dealerVal = handValue(dealerHand + [i] + [j])
			if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
				x = x + 1
				c = c + 1
			else:
				c = c + 1
	p = 100-(float(x)/float(c))*100
	print ("probabilidade de ganhar na proxima jogada fazendo stand e o dealer hit: %2.2f%%"% (p))

def probGanharProxRondaStandHit(myHand, dealerHand): #dealer faz hit e jog faz stand
	x=0 #em que o dealer ganha
	c=0 #casos totais
	for i in baralho:
		myVal = handValue(myHand + [i])
		for k in baralho:
			dealerVal = handValue(dealerHand + [k])
			if ((dealerVal > myVal) and (dealerVal <= 21)) or (myVal > 21):
				x = x+1
				c = c+1
			else:
				c = c+1
	p = 100-(float(x)/float(c))*100
	print ("probabilidade de ganhar na proxima jogada fazendo hit e o dealer stand: %2.2f%%"% (p))
	return p

probGanharAgora(dealerHand, myHand)
probGanharProxRonda(myHand, dealerHand)
probGanharProxRondaHitStand(myHand, dealerHand)
probGanharProxRondaStandHit(myHand, dealerHand)