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
p1 : 2
p2 : 0
p2 : 1
p1 : 3
==========
p1 : 9
p2 : 1
p2 : 2
p1 : 10
==========
p1 : 14
p2 : 2
p2 : 5
p1 : 14
==========
p1 : 18
p2 : 5
p2 : 7
p1 : 18
==========
p1 : 24
p2 : 7
p2 : 11
p1 : 24
==========
p1 has won
==========
game over
'''

