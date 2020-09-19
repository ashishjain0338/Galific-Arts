def pig(str):
    out = str.lower()
    if(out[0] == 'a' or out[0] == 'e' or out[0] == 'i' or out[0] == 'o' or out[0] == 'u'):
        out += 'way'
    else:
        out = out + out[0] + 'ay'
        out = out[1:]
    return out

list1 = ['happy','pencil','Enter','Out','other']
for x in list1:
    print(pig(x))