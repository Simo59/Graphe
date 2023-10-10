import math
class DSD (object):
    """
    DSD = Data Structure for Dijkstra algorithm
    
    Cette structure de données implémente les trois opérations nécessaires à la mise en
    œuvre de l'algorithme de Dijkstra.
    
    
    """
    
    def __init__ (self, graph, start):
        """
        Initialise la structure de données avec une distance de 0 associée au sommet 
        `start` du `graph` et l'infini pour les autres.
        """
        assert(start in graph.nodes())
        self.__graph = graph
        self.__start = start
        self.insert(start,0)
        for node in graph.nodes():
            if(node!=start):
                self.insert(node,math.inf)
        
    def insert (self, node, distance):
        """
        Ajoute le sommet `node` à la structure de données en y associant la distance
        `distance`.
        """
        pass
        
    def extract_min (self):
        """
        Retourne un couple (sommet,distance) correspondant à la distance minimale stockée
        dans la structure de données. Par effet de bord, cet élément est retiré de la 
        structure de données.
        
        Si la structure de données est vide produit une erreur.
        """
        pass
        
    def decrease (self, node, distance):
        """
        Met à jour la distance associée au sommet `node`.
        Cette mise à jour n'est réalisée que si `distance`est inférieure à la valeur 
        associée à `node`dans la structure de donnée.
        Sinon ne fait rien.
        """
        pass
    

    def is_empty (self):
        pass