import matplotlib.pyplot as plt
import networkx as nx
l=[("henri","jacquline"),("henri","roger"),("roger","jacquline"),("marcel","Bernadete"),("marcel","jean"),("Bernadete","henri"),("Bernadete","anatole"),("anatole","marcel")]
amis = nx.Graph(l)


def degre_max(g):
    assert isinstance(g,nx.classes.graph.Graph)
    max = 0
    for i in list(g.nodes):
        tmp =g.degree(i)
        if max < tmp:
            max=tmp 
    return max 

def who_with_max_frinds(g):
    deg_max=degre_max(g)
    res=[]
    for i in list(g.nodes):
        if g.degree(i)==deg_max  :
            res.append(i) 
    return res

def friends_of_friends(g,s):
    res=[]
    for i in g.neighbors(s):
            for j in g.neighbors(i):
                if j not in res and j not in g.neighbors(s) and j!=s:
                    res.append(j)
    return res



if __name__=="__main__":
    # les arretes se coisent pas on appelle ca un graphe planaire
    # pour verifier celui avec le plus d amis on verivier celui avec le plus grand degrees
    print("celui avec bcp d amis est "+str(who_with_max_frinds(amis)))

    print()
    print(" les amis des amis de {} sont:\n {} \n".format("marcel",friends_of_friends(amis,"marcel")))
    nx.draw(amis, with_labels=True, font_weight='bold')
    plt.show()