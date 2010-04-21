def FBA(threshold, damping, graph):
    kinetic_energy = 0
    while (kinetic_energy < threshold):
        for thisNode in graph.AllNodes():
        
            for otherNode in nodes.getNeighbours():
                otherNode.net_force = otherNode.net_force + Coulumb_repulsion(thisNode, otherNode)
            

    
