from unicodedata import name

from partie1 import ajouter_arrete


g = [[1,2],[0,2],[0,1],[]]

def existe_entre_0_et_2(g):
    return [0,2] in g or [2,0] in g

def existe_entre_1_et_2(g):
    return [1,2] in g or [2,1] in g

def taille (graphe):
    res=0
    for i in graphe:
        if len(i)!=0:
            res+=1
    return res

def creer (graphe, nombre_de_sommets):
    res=[]
    cpt =0
    for i in graphe:
        res.append([i[0],i[1]])
        cpt+=1
    if cpt <nombre_de_sommets:
        for i in range(cpt,nombre_de_sommets):
            res.append([])
    return res

def ajouter_arete (graphe, sommet1, sommet2):
    assert([sommet1,sommet2] not in graphe or [sommet2,sommet1]not in graphe)
    graphe.append([sommet1,sommet2])


if __name__=='__main__':
    print("***** QUESTION 1 *****")
    print("existe t il un sommet entre 0 et 2 \n"+ str(existe_entre_0_et_2(g)))
    print("existe t il un sommet entre 1 et 2 \n"+ str(existe_entre_1_et_2(g)))
    print()
    print("***** QUESTION 2 *****")
    print("la taille de g est "+str(taille(g)))

    print()
    print("***** QUESTION 3 *****")

    g = creer([(0,3), (1, 2), (1, 3)],4)
    print ("newg = "+str(g))
    print("taille de new g est "+str(taille(g)))

    print("***** QUESTION 4 *****")
    ajouter_arete(g,2,3)
    print ("apres ajout d une arrete newg = "+str(g))
    print("la taille de g est "+str(taille(g)))    



