from abstract import abstract

class GraphDatastructure():

    def vertexexists(self, node_id): abstract()

    def edgeexists(self, edge_id): abstract()
    
    def removeedge(self, (node_id_1, node_id_2), edge_id=None): abstract()

    def removeedges(self, edge_list): abstract()

    def getvertices(self): abstract()
    
    def getedges(self):  abstract()
    
    def degreelist(self):  abstract()
    
    def getadjedges(self, node_id): abstract()

    def getadjvertices(self, node_id): abstract()
        
    def getvertex(self, node_id):  abstract()
    
    def __str__(self): abstract()

    # the following functions are following a strict naming scheme across
    # our datastructures
    def visualisegraph(self, figNum=1, markEdges=[], markNodes=[]): abstract()

    def clearvisualisation(self): abstract()
        
    def generaterandomstructure(self, n): abstract()
        
    def clear(self):  abstract()

