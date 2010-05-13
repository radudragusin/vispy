##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
##
##
## graph.py
##
## LICENSED UNDER: GNU General Public License v2
##

import random as r
import matplotlib.pyplot as plt
import networkx as nx
import datastructure as abstract

class Graph(abstract.GraphDatastructure):
    def __init__ (self):
        self.vertices = []
        self.edges = []
        self._lastaddedvertex = -1
        self._lastaddededge = -1
        self._edgeIdCount = 0
        #needed for internal networkX representation
        plt.ion()
        self._G = nx.Graph()
        self._oldGVertices = []
        self._oldGEdges = []
        self._pos = {}

    def addVertex(self, vertex_id):
        if vertex_id == self._lastaddedvertex: return
        for vertex in self.vertices:
            if vertex.getId() == vertex_id:
                return
        self.vertices.append(Vertex(vertex_id))
        self.last_added_id = vertex_id
        
    def addEdge(self, (vertex_id_1, vertex_id_2), weight=0): 
# TO DO:
# remove possibilies of adding an edge that already exists:
# edges.contain( (1,2) ) such that add((2,1)) or add((1,2)) must fail.
# TO DO:
# automatically create vertices according to vertex_id_ if they do not already exist.
        if self.vertexExists(vertex_id_1) and self.vertexExists(vertex_id_2):
            edge_id = self._edgeIdCount
            self._edgeIdCount += 1
            newedge = Edge(edge_id, (vertex_id_1, vertex_id_2), weight)
            self.edges.append(newedge)
            return
        return False
    
    def removeVertex(self, vertex_id):
        for vertex in self.vertices:
            if vertex.getId() == vertex_id:
                self.vertices.remove(vertex)
                adjEdges = self.getAdjEdges(vertex_id)
                self.removeEdges(adjEdges)
                return True
        return False

    def vertexExists(self, vertex_id):
        for vertex in self.vertices:
            if vertex.getId() == vertex_id:
                return True
        return False

#    def edgeExists(self, (vertex_id_1, vertex_id_2)):
#        for edge in self.edges:
#            if ((edge.start_vertex, edge.end_vertex) == (vertex_id_1, vertex_id_2)):
#                return True
#        return False
    
    def removeEdge(self, (vertex_id_1, vertex_id_2)):
        for edge in self.edges:
            if ((edge.start_vertex, edge.end_vertex) == (vertex_id_1, vertex_id_2)) or ((edge.start_vertex, edge.end_vertex) == (vertex_id_2, vertex_id_1)):
                self.edges.remove(edge)
                return True
        return False

    def removeEdges(self, edge_list):
        # suppose edge_list is list of sets
        for edge in edge_list:
            self.removeEdge(edge)
        return True

    def getVertices(self):
        return [n.getId() for n in self.vertices]
    
    def getEdges(self): 
        return [(e.start_vertex, e.end_vertex) for e in self.edges]
    
    def degreeList(self): 
        return False
    
    def getAdjEdges(self, vertex_id):
        buf = []
        for edge in self.edges:
            if edge.start_vertex == vertex_id or edge.end_vertex == vertex_id:
                buf.append((edge.start_vertex, edge.end_vertex))
        return buf

    def getAdjvertices(self, vertex_id):
        buf = []
        adjEdges = self.getAdjEdges(self, vertex_id)
        for edge in adjEdges:
            if edge.start_vertex == vertex_id:
                buf.append(edge.end_vertex)
            elif edge.end_vertex == vertex_id:
                buf.append(edge.start_vertex)
        return buf
    
    def getVertex(self, vertex_id): 
        for vertex in self.vertices:
            if vertex.vertex_id == vertex_id:
                return vertex
        return False
    
    def visualise(self, figNum=1, markEdges=[], markVertices=[], savefig=None,
        savefig_format='png', vertexLabels=None):
        plt.figure(figNum, facecolor='white')
        plt.clf()
        plt.axis('off')
        self._G.clear()
        for vertex in self.vertices:
            self._G.add_node(vertex.getId())

        for edge in self.edges:
            self._G.add_edge(edge.start_vertex,edge.end_vertex)
            
        if (not self._oldGVertices and not self._oldGEdges) or (not self._oldGVertices == self._G.nodes() or not self._oldGEdges == self._G.edges()):
            self._pos = nx.spring_layout(self._G)

        self._oldGVertices = self._G.nodes()
        self._oldGEdges = self._G.edges()

        if not markVertices and not markEdges:
            nx.draw_networkx_nodes(self._G, self._pos, node_color='#557A66')#, edge_color='#272E2E')
            nx.draw_networkx_edges(self._G, self._pos)#, edge_color='#272E2E')
            nx.draw_networkx_labels(self._G, self._pos, labels=vertexLabels)
#            nx.draw_networkx_edge_labels(self.G, self._pos, edge_labels=vertexLabels)
# drawing edge labels are only avaliable from networkX 1.1 and beyond
        else:
            unmarkedVertices = list(set(self._G.nodes()).difference(markVertices))
            unmarkedEdges = list(set(self._G.edges()).difference(markEdges))

            nx.draw_networkx_nodes(self._G, self._pos, nodelist=unmarkedVertices, node_color='#557A66')#, vertex_size=700)
            nx.draw_networkx_nodes(self._G, self._pos, nodelist=markVertices, node_size=700, node_color='#9ed95e')
            # E82B1E <- roed sort trae
            nx.draw_networkx_edges(self._G, self._pos, edgelist=unmarkedEdges)#, edge_color='#272E2E')#, width=6)
            nx.draw_networkx_edges(self._G, self._pos, edgelist=markEdges,width=6)#, edge_color='#272E2E')

            nx.draw_networkx_labels(self._G, self._pos, labels=vertexLabels)

        if savefig:
            plt.savefig(savefig, format=savefig_format)

    def clearVisualisation(self):
        self._pos = {}
        plt.close()
        
    def generateRandomGraph(self, numberofvertices, numberofedges=0):
        self.clear()
        vertexId = 0
        self.addVertex(vertexId)
        for i in range(1,numberofvertices):
            neighbor = r.randint(0,len(self.vertices)-1)
            vertexId += 1
            self.addVertex(i)
            self.addEdge((i, neighbor))
        
    def __str__(self):
        return
        
        
    def clear(self): 
        self.vertices = []
        self.edges = []
        self._lastaddedvertex = -1
        self._lastaddededge = -1
        self._edgeIdCount = 0
        self._G = nx.Graph()
        self._oldGVertices = []
        self._oldGEdges = []
        self._pos = {}



class Vertex:
    def __init__(self, vertex_id, label=None):
        self._id = vertex_id
        self.label = label
        
    def getId(self):
        return self._id
        
    def getLabel(self):
        if not self.label:
            return self.getId()
        return self.label
    
class Edge:
    def __init__(self, edge_id, (start_vertex_id, end_vertex_id), weight):
        self._id = edge_id
        self.weight = weight
        self.start_vertex = start_vertex_id
        self.end_vertex = end_vertex_id
            
    def getId(self):
        return self._id
    def getWeight(self):
        return self.weight
    
    
