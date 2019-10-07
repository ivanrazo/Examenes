#A-3
def  lista ( arr ):
    pos = 0
    neg = 0
    for i in  range ( len (arr)):
        if (arr [i] > 0 ):
            pos = pos + 1
        else :
            neg = neg + arr [i]
    print ( " El numero de los positivos es: " +  str (pos))
    print ( " La suma de los negativos es: " +  str (neg))


lista ([1, 2, 3, 4, 5, 6, -11, -12, -13, -14, -15]) #3,-10
#lista ([1, 2, 3, 4, 5, 6, -11, -12, -13, -14, -15]) 6,-65