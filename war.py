from cards import *
import math
import itertools
games=10000
cards= [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52]
wins=  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(games):
    adeck1=deck()
    adeck2=deck()
    adeck1.shuffle()
    adeck2.shuffle()
    deck2=0
    deck3=0
    while adeck1.cardsleft()>0:
        acard1=adeck1.dealcard()
        acard2=adeck2.dealcard()
        if acard1.value()> acard2.value():
            deck2 +=2
        if acard2.value()> acard1.value():
            deck3 +=2
        else:
            deck2 +=1
            deck3 +=1
    difference = int(abs(deck2-deck3))
    wins[int(difference/2)] = wins[int(difference/2)] + 1
winsratio= [i/ games for i in wins]
c= "\n".join("{} {}".format(x, y) for x,y in zip(cards,winsratio))       
print(c)
