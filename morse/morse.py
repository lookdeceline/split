# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }
'''
dic2 = {y:x for x,y in dic.items()}
dic2[' '] = '/'
#print(dic2)
'''
class Spy:
    dic = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }

    dic2 = {y: x for x, y in dic.items()}

    def __init__(self, name):
        self.name = name

    def my_name(self):  # send_morse
        return self.name+": "   # "cobb: "

    def alpha_to_morse(self, line):
        result = []
        for word in line.split(" "):
            for char in word:
                # print(char)
                # print(dic2[char])
                result.append(self.dic2[char] + " ")

            result.append("/")
        return "".join(result)

    def morse_to_alpha(self, line):
        result = []
        space_sig = 0
        linelist = line.split(" ")[1:]
        for word in linelist:
            if "/" in word:
                space_sig = 1
            word = word.replace('/', "")
            if word != "":
                if space_sig != 0:
                    result.append(" ")
                result.append(self.dic[word])
            space_sig = 0

        return "".join(result)

# print(alpha_to_morse('HE SLEEPS EARLY'))
# print(morse_to_alpha('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
# print(morse_to_alpha('-.. --- /-.-- --- ..- /.-. . -- . -- -... . .-. /..-. .-. --- -- /-... . ..-. --- .-. . /- .... .. ... /-.. .-. . .- -- /'))
# print("="*30)

class MorseTalk:
    def __init__(self, spy1, spy2):
        self.spy1 = spy1
        self.spy2 = spy2
        # natural->morse##############################################################3
    def n_to_m(self):
        f = open("inception.txt", "r")
        f_in = f.read()
        f_in = f_in.upper()

        i = 0
        f_out = ""
        tmplist = f_in.split("\n")
        for line in tmplist:
            morseline = ""
            if i % 2 == 0:
                f_out += self.spy1.my_name()
                morseline = self.spy1.alpha_to_morse(line)
            else:
                f_out += self.spy2.my_name()
                morseline = self.spy2.alpha_to_morse(line)
            f_out += morseline
            if i != len(tmplist) - 1:
                f_out += "\n"
            i += 1

        fw = open("inception_eng_to_morse.txt", "w")
        fw.write(f_out)
    # ##############################################################3

    # morse -> alpha ###############################################
    def m_to_n(self):
        f = open("inception_eng_to_morse.txt", "r")
        f_in = f.read()

        i = 0
        f_out = ""
        for line in f_in.split("\n"):
            if i % 2 == 0:
                f_out += self.spy1.my_name()  # "cobb: "
                naturalline = self.spy1.morse_to_alpha(line)
            else:
                f_out += self.spy2.my_name()  # "fischer: "
                naturalline = self.spy2.morse_to_alpha(line)
            f_out += naturalline + "\n"
            i += 1

        fw = open("inception_morse_to english.txt", "w")
        fw.write(f_out)
    # more -> alpha ###############################################

cobb = Spy('cobb')
fischer = Spy('fischer')

inception = MorseTalk(cobb, fischer)
inception.n_to_m()
inception.m_to_n()
#
# n_to_m(cobb, fischer)
# m_to_n(cobb, fischer)