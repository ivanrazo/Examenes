#A-2
def div ( lista , n ):
    lista_nueva = []
    for i in  range ( len (lista)):
        if (lista [i] % n == 0 ):
            lista_nueva.append (lista [i])
    print (lista_nueva),
    return lista_nueva

div ([ 1 , 2 , 3 , 4 , 5 , 6 ], 2 ) # [2,4,6]
div ([ 9 , 12 , 3 , 0 , 1 , 4 ], 3 ) # [9, 12, 3]
div ([ 10 , 11 , 3 ], 1 ) # [10, 11, 3]