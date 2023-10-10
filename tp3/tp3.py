import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

g8=nx.Graph([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8)])#(1,4),(1,6),(1,8),(3,6),(3,8),(5,2),(5,8),(7,4),(7,2)])
g4 = nx.Graph([(1,2),(1,3),(3,4),(4,2),(1,4)])
g2 =nx.Graph([(1,2)])


def partition(collection):
    """
    Prend en entrée une collection d'objets (typiquement une liste d'entiers) 
    et produit une énumération de toutes les partitions.
    
    >>> list(partition([1, 2, 3]))
    [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]], [[2], [1, 3]], [[1], [2], [3]]]
    """
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller


def est_biparti_naif (graphe):
    list_sommets=list(graphe.nodes())
    list_partition=list(partition(list_sommets))
    found=False
    cpt =0
    for part in list_partition:
        breaked=False
        
        for i in part:
            if len(i)==1:
                breaked=True
            for j in i:
                for h in i :
                    if(h in list(graphe.neighbors(j))):
                        breaked=True
                        break
        
        if not breaked :
            found = True

    return found







if __name__=="__main__":
    nx.draw(g8,with_labels=True)
    #plt.show()
    #v1, v2 = bipartite.sets(g4)
    #print(v1,v2)
    print(est_biparti_naif(g8));