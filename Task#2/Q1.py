def CountLetters(str):
    return len(str)

def PatternMatch(str,pattern):
    i = 0
    j = 0
    while(i<len(str)):
        if(str[i] == pattern[0]):
            j = 0
            while(j < len( pattern ) ):
                if( str[i + j] != pattern[j]):
                    break
                j = j + 1
            if(j == len(pattern)):
                return True
        i = i + 1
    return False

def DictOrder(l1):
    l1.sort()
    return l1

def FindLongest(list1):

    out = []
    if(len(list1)):
        max_length = len(list1[0])
        for x in list1:
            if(len(x) > max_length):
                max_length = len(x)
                out = []
                out.append(x)
            elif(len(x) == max_length):
                out.append(x)
    return out


list1 = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
list2 = ['Supercalifragilisticexpialidocious','Honorificabilitudinitatibus','Bababadalgharaghtakamminarronnkonn']
# list3 = ['a','b','c','d']
print('There are ',CountLetters('Supercalifragilisticexpialidocious'),' letters in Supercalifragilisticexpialidocious')
print("'Supercalifragilisticexpialidocious' contain 'ice' as a substring-->",PatternMatch('Supercalifragilisticexpialidocious','ice'))
print('Longest word is -->',FindLongest(list2))
print("First word acc to dict order --> ",DictOrder(list1)[0])
print("Last word acc to dict order --> ",DictOrder(list1)[-1])