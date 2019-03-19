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