import sys

line = sys.argv[1]
numO = 0
numE = 0

commas = 0
for c in line:
    if c == ",":
        commas += 1

num = commas + 1

for i in range(num):
    index = line.find(',')
    if  index == -1:
        value = int(line)
    else:
        value = int(line[:index])
        line  = line[index + 1:]
    
    if  value % 2 == 1:
        numO  += value
    else:
        numE  += value

print("Odd numbers total:" + str(numO) + " , even numbers total:" + str(numE))
