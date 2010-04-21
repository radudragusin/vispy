
class Graph(datastructure.Datastructure):

    def __init__ (self):
        self.nodes = {}
        self.edges = []
        
    def insertNode(self, nodename): # a node is simply a label
        self.nodes.update({nodename: nodename})
        
    def deleteNode(self, nodename):
        try:
            node = self.nodes[nodename]
            neighbours = self.getNeighbours(node)
            for neighbour in neighbours:
                self.deleteEdge(node, neighbour)
                self.deleteEdge(neighbour, node)
            del self.nodes[node]
        except: # node does not exist!
            return False
    
    def updateNode(self, oldnodename, newnodename):
        return False

    def insertEdge(self, startnode, endnode, weight):
        self.edges.append(self.edge(startnode, endnode, weight))
    
    def updateEdge(self, startnode, endnode):
        return False
    
    def deleteEdge(self, startnode, endnode, weight=None):
        for i in range(len(self.edges)):
            if self.edges[i].startnode == startnode:
                if self.edges[i].endnode == endnode:
                    if weight == None or self.edges[i].weight == weight:
                        del self.edges[i]
                        return True
        return False

    def getNeighbours(self, nodename):
        buffer = []
        for i in range(len(self.edges)):
            if self.edges[i].startnode == nodename:
                buffer.append(self.edges[i].endnode)
            elif self.edges[i].endnode == nodename:
                buffer.append(self.edges[i].startnode)                
        return buffer  
        
        
    class edge:
        def __init__(self, startnode, endnode, weight):
            self.startnode = startnode
            self.endnode = endnode
            self.weight = weight
            
        def setStart(self, newstart):
            self.startnode = newstart
            return True
        
        def setEnd(self, newend):
            self.endnode = newend
            return True
            
        def setWeight(self, newweight):
            self.weight = newweight
            return True
            
        def getStart(self):
            return self.startnode
        
        def getEnd(self):
            return self.endnode
            
        def getWeight(self):
            return self.weight

