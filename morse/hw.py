from random import randint

class Player:
    def __init__(self,player1,player2):
        self.score1=0
        self.score2=0
        self.player1=player1
        self.player2=player2
        self.turn=0

    def roll(self):
        a=randint(1,6)
        if a==1:
            self.score1+=1;self.score2+=1;
        elif self.turn%2==0:
            self.score1+=a
        else:
            self.score2+=a

    def has_won(self):
        if(self.score1>=20):
            print("%s has won"%(self.player1))
            print("="*10)
            print("game over")
            return 1;
        elif(self.score2>=20):
            print("%s has won"%(self.player2))
            print("=" * 10)
            print("game over")
            return 1;

    def printscore(self):
        if(self.turn%2==0):
            print("%s : %d"%(self.player1, self.score1))
            print("%s : %d"%(self.player2, self.score2))
        else:
            print("%s : %d" % (self.player2, self.score2))
            print("%s : %d" % (self.player1, self.score1))
        print("="*10)

    def turnchange(self):
        self.turn+=1

game=Player("p1","p2")

while(game.has_won()!=1):
    game.roll()
    game.printscore()
    game.turnchange()