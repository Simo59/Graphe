import numpy as np
g = np.array([[0,1,1,0],[1,0,1,0],[1,1,0,0],[0,0,0,0]])


def existe_arrete(graphe,s1,s2):
    assert(s1 <g.shape[0])
    assert(s2 <g.shape[0])
    return graphe[s1][s2]==1


def voisins (graphe, sommet):
    """
    Retourne la liste des successeurs du sommet dans le graphe.
    CU: le sommet existe
    """
    assert(sommet<g.shape[0])
    res=[]
    for i in range(0,g.shape[0]):
        if graphe[i][sommet]==1:
            res.append(i)
    return res


def taille (graphe):
    """
    Retourne la taille du graphe
    """
    nbOne=0
    for i in range(0,g.shape[0]):
            for j in range(0,g.shape[0]):
                if graphe[i][j]==1:
                    nbOne+=1
    return nbOne//2

def creer( graphe ,nbSommets):
    res=np.zeros((nbSommets,nbSommets),dtype=np.int32)
    for i in graphe:
        res[i[0]][i[1]]=1
        res[i[1]][i[0]]=1
    return res


def ajouter_arrete(graphe,s1,s2):
    """
    ajoute un arrete entre s1 et s2 dans le graphe g
    """
    assert(s1 <g.shape[0])
    assert(s2 <g.shape[0])
    g[s1][s2]=1
    g[s2][s1]=1


if __name__=="__main__":
    print("g="+str(g))
    print()
    print("***** QUESTION 1 *****")
    print("exesite t il une arrete en 1 et 2? "+str(existe_arrete(g,1,2)))
    print("exesite t il une arrete en 1 et 3? "+str(existe_arrete(g,1,3)))
    print()
    print("***** QUESTION 2 *****")
    for i in range(4):
        print("les voisins de "+str(i)+" sont " + str(voisins(g,i)))
    print()
    print("***** QUESTION 3 *****")
    print("la taille de g est = "+str(taille(g)))
    print()
    print("***** QUESTION 4 *****")
    print("taille apres ajout d une arrete entre 0 et 3 \n")
    ajouter_arrete(g,0,3)
    print(g)
    print(" la taille de g est "+str(taille (g)))
