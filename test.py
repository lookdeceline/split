import re

def ex_ftn(str):
    st = str.lower()
    sv = re.sub("[,.!]","",st)
    cha = sv.split()
    dic = {}
    for a in cha :
        if a not in dic.keys():
            dic[a] = 1
        else:
            dic[a] = dic[a] + 1
    return dic

print(ex_ftn('Baby shark, doo doo doo doo doo doo. Baby shark!'))