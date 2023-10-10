import networkx as nx
import matplotlib.pyplot as plt
import DSDArray


g = nx.DiGraph() #DiGraphe pour creer des graphe orientée
l = [(0,1,5),(0,2,7),(0,3,4),(0,4,2),(1,4,2),(3,4,3),(3,6,4),(3,5,7),(3,2,9),(4,6,7),(6,5,12),(5,2,5)]
for a,b,w in l:
    g.add_edge(a,b,weight=w)

def plus_court_chemin (graph, start, dsdo):
    """
    Calcule le plus court chemin dans `graph` entre le sommet de départ `start` et 
    tous les autres sommets accessibles.
    
    Parametres
    ----------
    graph: networkX.DiGraph ou networkx.Graph
        le graphe
    start: int
        le sommet de départ
    dsdo: Class
        le nom d'une classe qui hérite de DSD
        
    Retourne
    --------
    dict
        un dictionnaire des distances entre `start` et les autres sommets
    """
    dsd=dsdo(graph,start)
    #créer un tableau T qui conservera les distances
    t=dict()
    while(not dsd.is_empty()):
        nmin, dmin = dsd.extract_min()
        t[nmin]=dmin
        #print("t ="+str(t))
        for neighbor in graph.neighbors(nmin):
            weight=graph[nmin][neighbor]['weight']
            print(weight)
            dsd.decrease(neighbor,dmin+weight)
    return t


if __name__=="__main__":
    nx.draw(g,with_labels=True,node_color='lightgrey',node_size=600,font_weight='bold')
    print("myVersion {}".format(plus_court_chemin(g,0,DSDArray.DSDArray)))
    print("nx version {}".format(nx.shortest_path_length(g,0,weight='weight',method='dijkstra')))
    plt.show()

