# Logan Warren
# Assign 3-3
# Due 9/10

import sys
def calcavg(g1, g2, g3, g4, g5):
    avg = (g1 + g2 + g3 + g4 + g5) / 5
    return avg

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

def printresults(avg, letter):
    print("Average:", avg)
    print("Letter Grade:", letter)
try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    n4 = int(sys.argv[4])
    n5 = int(sys.argv[5])
    average = calcavg(n1, n2, n3, n4, n5)
    letter = getletter(average)
    results = printresults(average, letter)
except:
    print("Please enter a numeric value.")
    quit()
