
f = open('ex.txt', 'r')
'''
line = f.read()
print(line)
'''
line_by_sentence = f.readline()
# print(line_by_sentence)




filepath = 'ex.txt'
with open(filepath) as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

# write
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()