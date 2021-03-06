'''
class Player 을 사용하여 두 명의 플레이어가 게임하는 프로그램을 작성하시오.

게임 룰:

    roll()함수:
    주사위를 던져서 나온 숫자(1 ~ 6 중 랜덤한 하나의 값)를 출력하고, 해당 숫자만큼 게이머의 score이 증가한다.
    단, 플레이어가 던진 주사위 숫자가 1인 경우, 상대의 score이 1 증가한다.

    has_won()함수: 둘 중 한명의 score이 20점 이상이 된 경우, 게임이 종료되고, 우승자의 이름을 출력한다.

힌트:
    roll() 함수에서 랜덤한 값 생성하기 :
        from random import randint
        x = randint(1, 6)
        를 이용한다.


sample output:
p1 : 6
p2 : 0
==========
p2 : 5
p1 : 6
==========
p1 : 9
p2 : 5
==========
p2 : 10
p1 : 9
==========
p1 : 15
p2 : 10
==========
p2 : 15
p1 : 15
==========
p1 : 19
p2 : 15
==========
p2 : 17
p1 : 19
==========
p1 : 25
p2 : 17
==========
p1 has won
==========
game over


sample output2:

p1 : 2
p2 : 0
==========
p2 : 5
p1 : 2
==========
p1 : 3
p2 : 6
==========
p2 : 12
p1 : 3
==========
p1 : 4
p2 : 13
==========
p2 : 15
p1 : 4
==========
p1 : 7
p2 : 15
==========
p2 : 16
p1 : 8
==========
p1 : 9
p2 : 17
==========
p2 : 19
p1 : 9
==========
p1 : 15
p2 : 19
==========
p2 : 24
p1 : 15
==========
p2 has won
==========
game over

'''





from random import randint

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def roll(self, opp):
        dice = randint(1, 6)
        self.score += dice
        if dice == 1:
            opp.score += 1
        print(self.name,':', self.score)
        print(opp.name,':', opp.score)
        print("=" * 10)

    def has_won(self):
        if self.score >= 20:
            print(self.name, 'has won')
            return True
        else:
            return False


p1 = Player('p1')
p2 = Player('p2')
currently_playing = True
def gameover():
        currently_playing = False
        print("="*10)
        print("game over")

while True:

    if p1.has_won() or p2.has_won():
        gameover()
        break

    else:
        p1.roll(p2)
        if p1.has_won() or p2.has_won():
            gameover()
            break
        p2.roll(p1)

