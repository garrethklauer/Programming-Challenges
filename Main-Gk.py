from functools import reduce

def uncensor(censoredword, vowels):
    vowelwordspread = []
    uncensoredword = []
    vowelcount = 0
    for k in range(len(vowels)):
        for l in vowels[k]:
            vowelwordspread.append(vowels[k])
    for i in range(len(censoredword)):
        for j in censoredword[i]:
            if censoredword[i] == "*":
                uncensor = censoredword[i].replace(censoredword[i], vowelwordspread[vowelcount])
                uncensoredword.append(uncensor)
                vowelcount += 1
            elif censoredword[i] != "*":
                uncensoredword.append(censoredword[i])
    merged = reduce(lambda x, y: x + y, uncensoredword)
    print(merged)


uncensor("*PP*RC*S*", "UEAE")
