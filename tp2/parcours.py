import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt

g = nx.Graph([(0,1),(0,2),(1,3),(2,4),(2,1),(3,5),(5,1)])



def parcours_en_profondeur(graphe, depart):
    res=[]
    deja_visite=dict()
    for node in graphe.nodes():
        deja_visite[node]=False
    
    a_traiter=[]
    a_traiter.append(depart)
    print("*****parcours 1******")
    while a_traiter !=[]:
        print("pile = "+str(a_traiter))
        sommet = a_traiter.pop()
        if  deja_visite[sommet]==False:
            res.append(sommet)
            deja_visite[sommet]=True
            for voisin in list(graphe.neighbors(sommet)):
                if deja_visite[voisin]==False:
                    a_traiter.append(voisin);
    return res

def parcours_ameliore(graphe,depart):
    res=[]
    deja_visite=dict()
    colors = dict()
    for node in graphe.nodes():
        deja_visite[node]=False
        colors[node]="blue"

    a_traiter = []
    a_traiter.append(depart)
    print("*****parcours amelioree******")
    while(a_traiter!=[]):
        print("pile = "+str(a_traiter))
        sommet=a_traiter.pop()

        if(not deja_visite[sommet]):
            res.append(sommet)
            deja_visite[sommet]=True
            colors[sommet]="red"
            for i in list(graphe.neighbors(sommet)):
                if colors[i]=="blue":
                    colors[i]="gray"
                    a_traiter.append(i)
    return res

def arbre_couvrantes(graphe,depart):
    arretes_of_tree=[]

    return nx.Graph(arretes_of_tree)


def est_connexe(graphe):
    return set(parcours_ameliore(graphe,0))== set(graphe.nodes())

def composantes_connexes(graphe):
    res=[]
    deja_visite=dict()
    for node in graphe.nodes():
        deja_visite[node]=False
    for node in graphe.node:
        if not deja_visite[node]:
            res.append(parcours_ameliore(g,node))
    return res

















if __name__=="__main__":
    nx.draw(g,with_labels=True)
    print(parcours_en_profondeur(g,0))
    print(parcours_ameliore(g,0))

    print("g est il connexe {}".format(est_connexe(g)))
    # oui notre parcours est toujours un parcours en profondeur
    plt.show()


