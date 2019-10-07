#FN-3
def  rep ( lista_original ):
    lista_nueva = []
    cont = 0
    for j in range ( len (lista_original)):
        cont = 0
        for i in  range ( 0 , len (lista_original)):
            if (lista_original [j] == lista_original [i]):
                cont = cont + 1 
        if (cont == 1 ):   
            lista_nueva.append (lista_original [j])
    print (lista_nueva)
    return lista_nueva

rep ([ 9 , 3 , 1 , 3 , 2 , 9 ]) # [1,2]
rep ([ 6 , 2 , 2 , 2 , 1 , 8 ]) # [6,1,8]
rep ([ 1 ]) # [1]