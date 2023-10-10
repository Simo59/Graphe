from xml.dom.minicompat import NodeList
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4)])

def nbSommets(G):
    return G.number_of_nodes()
def nbEdges(G):
    return G.number_of_edges()

def degrées(G,n):
    return G.degree(n)

def neighbors(G,n):
    return list(G.neighbors(n))

h = nx.Graph([('Paul','Jacques'),('Paul','Maryse')])
h.add_node('Séverine')

def degre_max(g):
    assert isinstance(g,nx.classes.graph.Graph)
    max = 0
    for i in list(g.nodes):
        tmp =g.degree(i)
        if max < tmp:
            max=tmp 
    return max  

def est_complet(g):
    assert isinstance(g,nx.classes.graph.Graph)
    max_deg = degre_max(g)
    if max_deg != len(list(g.nodes()))-1:
        return False
    else:
        for i in g.nodes:
            tmp =g.degree(i)
            if tmp !=max_deg:
                return False
    return True

    
comp = nx.complete_graph(6)




if __name__=='__main__':
    #nx.draw(G, with_labels=True, font_weight='bold')
    #nx.draw(h, with_labels=True, font_weight='bold')

    #print (degre_max(h))

    #plt.show()



    print(" le graphe h est il complet ? ===>" + str(est_complet(h)))
    print ()
    print(" le graphe comp est il complet ? ===>" + str(est_complet(comp)))
    print("les graphes g et h sont ils isomorphes ===>"+str(nx.is_isomorphic(h,G)))
