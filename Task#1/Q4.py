def Hash_Fxn(c):
    if(c>='a' and c<='z'):
        ind = ord(c) - ord('a')
        return ind
    else:
        return -1

def Frequencies(str):
    hash = []
    for x in range(0,26):
        hash.append(0)

    for letters in str:
        ind = Hash_Fxn(letters)
        if(ind != -1):
            hash[ind] = hash[ind] + 1
    return hash

str = 'The quick red fox got bored and went home.'
# str = 'abcdefghijklmnopqrstuvwxyzz'
print(Frequencies(str))
