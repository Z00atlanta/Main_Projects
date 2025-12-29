import sys


def getletter(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
total = 0    
count = 0
inp = sys.argv[1]
sep = ' '
ind = inp.find(sep)
while ind != -1:
    value = inp[:ind]
    total = total + int(value)
    count = count + 1
    inp = inp[ind + 1:]
    ind = inp.find(sep)
total += int(inp)
count += 1
average = total / count   
letter = getletter(average)
print(average, letter)
