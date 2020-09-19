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

def FindLongest(s1,s2,s3):
    out = max(s1 , s2)
    out = max(out , s3)
    return out


list1 = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']

print('There are ',CountLetters('Supercalifragilisticexpialidocious'),' letters in Supercalifragilisticexpialidocious')
print("'Supercalifragilisticexpialidocious' contain 'ice' as a substring-->",PatternMatch('Supercalifragilisticexpialidocious','ice'))
print('Longest word is -->',FindLongest('Supercalifragilisticexpialidocious','Honorificabilitudinitatibus','Bababadalgharaghtakamminarronnkonn'))
print("First word acc to dict order --> ",DictOrder(list1)[0])
print("Last word acc to dict order --> ",DictOrder(list1)[-1])