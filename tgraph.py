import graph as gr

class tGraph(gr.Graph):

    def __subconstruct__(self, visual):
        """ Contains all initialisations needed for the visualiser"""
        self._visualisation = visual
        gr.plt.ion()
        self._g = gr.nx.DiGraph()
        self._oldgvertices = []
        self._oldgedges = []
        self._pos = {}
        
