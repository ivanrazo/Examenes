#A-1
def  lista ( arr ):
    total = 45
    aux = 0
    i = 0
    for i in range ( len (arr)):
        aux = aux + arr [i]
    if (total == aux and len (arr) == 10 ):
        print ( " No falta ninguno " )
    else :
        print ( " Falta el número " +  str (total - aux))

arr = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 0 ] # falta 5
arr2 = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 5 ] # falta 0
arr3 = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 0 , 5 ] # no falta ninguno

lista (arr)
lista (arr2)
lista (arr3)