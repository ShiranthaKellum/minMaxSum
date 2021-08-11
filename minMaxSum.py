
list = []
print ("Enter elements")

for i in range (5):
    x = int(input())  # 256741038 623958417 467905213 714532089 938071625
    list.append (x)

print (sum (list) - max(list), sum (list) - min (list))

