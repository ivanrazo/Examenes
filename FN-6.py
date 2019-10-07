#FN-6
def  sumDif ( arr ):
    for i in  range ( len (arr)):
        dif = arr [ 0 ]
        dif = dif - arr [i]
    print (dif)


sumDif ([ 10 , 2 , 1 ]) # (10 - 2) + (2 - 1) = 9
sumDif ([ 11 , 10 , 5 ]) # ( 11-10 ) + ( 10-5 ) = 6
sumDif ([ 4 , 3 , 2 , 1 ]) # (4 - 3) + (3 - 2) + (2 - 1) = 3