
list = []
for i in range (5):
    x = int (input ("ele"))   #256741038 623958417 467905213 714532089 938071625
    list.append (x)

list.sort ()

minSum = 0
for i in range (4):
    minSum += list [i]

maxSum = 0
for i in range (1, 5):
    maxSum += list [i]

print (minSum, maxSum)