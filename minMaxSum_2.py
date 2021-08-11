
def getList ():
    list = []
    for i in range (5):
        x = int (input ("ele = "))
        list.append (x)

    minMaxSum (sum (list), list)
        

def sum (list):
    sum = 0
    for i in range (5):
        sum += list [i]
    
    return sum

def minMaxSum (sum, list):
    sumList = []
    for i in range (5):
        x = sum - list [i]
        sumList.append (x)

    print (sumList [0], sumList [4])


    

getList ()

