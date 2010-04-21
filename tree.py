##
## tree.py
##

import matplotlib.pyplot as plt
import networkx as nx
import random as r

class Tree():
    def __init__ (self, children=[]):
        self.children = children
        plt.ion()
        self.G=nx.Graph()
    def getChildren(self):
        return self.children
    def setChildren(self, children):
        self.children = children
    def addChild(self, child):
        self.children.append(child)
    def removeChild(self):
        self.children.pop()
    
    def getPos(self,num=0, ph=0, pw=0, space=1):
        p = self.pos(num, ph, pw, space)
        return p[0]
    def pos(self,num=0, ph=0, pw=0, space=1):
        d = {num:(pw,ph)}
        l = float(space)/float(len(self.children))
        edge = pw-(space/2.0)+(l/2.0)
        for t in self.children:
            res=t.pos(num+1, ph-1, edge, l)
            edge += l
            num = res[1]
            d.update(res[0])
        return [d, num]
    def getEdges(self,p=0,num=0):
        this = num
        if(p != this):
            e = [(p,this)]
        else:
            e = []
        for t in self.children:
            res = t.getEdges(this,num+1)
            num = res[1]
            e += res[0]
        if(p != this):
            return [e, num]
        else:
            return e

    def vizMe(self, figNum=1):

        plt.figure(figNum)
        plt.clf()
        plt.axis('on')
        self.G.clear()
        p = self.getPos()
        e = self.getEdges()
        for i in range(0,self.getCount()):
            self.G.add_node(i)
        self.G.add_edges_from(e)
        nx.draw_networkx(self.G, p)


    
    def getDepth(self):
        highest = 0
        for child in self.children:
            highest = max(child.getDepth(), highest)
        return highest+1;
    def getCount(self):
        c = 1
        for t in self.children:
            c += t.getCount()
        return c
    
class Leaf:
    def __init__(self, content):
        self.content = content        
    def getContent(self):
        return self.content
    def setContent(self,content):
        self.content = content
    def getDepth(self):
        return 1
    def getCount(self):
        return 1
    def pos(self,num, ph, pw, space):          
        return [{num:(pw,ph)}, num]
    def getEdges(self,p=0,num=0):
        if(p!=num):
            return [[(p,num)],num]
        else:
            return []
        
t1 = Tree([Tree([Tree([Leaf('a'),Leaf('b')]),Tree([Leaf('c'),Leaf('d')])]),Tree([Leaf('e'),Leaf('f')])])
t2 = Tree([Tree([Tree([Leaf('a'),Leaf('b')]),Tree([Leaf('c'),Leaf('d')])]),Tree([Leaf('e'),Leaf('f')]), Tree([Tree([Leaf('g'),Leaf('h')]), Tree([Tree([Leaf('i'),Leaf('j'),Leaf('k'),Leaf('l')])])])])
t3 = Tree([Tree([Tree([Leaf('a'),Leaf('b')]),Tree([Leaf('c'),Leaf('d')])]),Tree([Leaf('e'),Leaf('f')]), Tree([Tree([Leaf('g'),Leaf('h'),Tree([Tree([Leaf('i'),Leaf('j'),Leaf('k'),Leaf('l')])])]), Tree([Tree([Leaf('m'),Leaf('n'),Leaf('o'),Leaf('p')])])])])
