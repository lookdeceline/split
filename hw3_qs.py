'''
Write a Python function to find the Max of numbers of a list given in parameter.
'''
def Max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

print(Max([5,7,2,3]))

'''
5. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Sample Output :
fizzbuzz
1
2
fizz
4
buzz
'''
for i in range(1, 51):
    if i % (3 * 5) == 0:   # * 이외에 and 같은 것을 쓸 수 있을까요?
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0 :
        print("buzz")
    else:
        print(i)


'''
8. List타입의 파라미터를 받아서 리스트의 각 요일로부터 10일 후의 요일을 계산하여 결과를 list 타입으로 반환하는 함수를 작성하라.
days = [‘월’, ‘목’, ‘일’]
'''

week=['월','화','수','목','금','토','일']

def aftertendays(days):
    newdays=[]
    for i in range(len(days)):
        newdays.append(week[(week.index(days[i]) + 10) % 7])
    return newdays
print(aftertendays(['월','목','일']))