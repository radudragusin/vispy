# Introduction #

This page will highlight how the visualization works for any algorithm applied to one of the support data structures.

# Visualizing a data structure #
## `vizMe(figNum=num, markEdges=[], markNodes=[], savefig=None, savefig_format='png', nodeLabels={})` ##
Assuming you have a data structure saved as an object, you may call the method `vizMe` to visualize the object. `vizMe` supports the following arguments, available for customizing your visualization:

| figNum       | Specification of which figure window the visualization must be placed. `figNum=1` by default. |
|:-------------|:----------------------------------------------------------------------------------------------|
| markEdges    | Which edges must be specifically highlighted. List of sets, for each set denoting an edge: `(start_node, end_node)` |
| markNodes    | List of `nodeID` to be highlighted                                                            |
| savefig       | name of output file where the figure will be saved. If unset, no file will be saved           |
| savefig\_format | Format to be saved, default= 'png'. Recommended = 'eps'                                       |
| nodeLabels   | Dictionary key by `nodeID` with label to be printed for those nodes                           |

### Example ###
The graph `a` is made with 10 random nodes:

`>>> from graph import *`

`>>> a = Graph()`

`>>> a.random(10)`

`>>> a.vizMe(markNodes=[1,2,0], markEdges=[(2,0),(0,1)], nodeLabels={2:'This is node 2', 1:'This is node 1', 3:3, 0:'This is node 0', 5:5, 4:4, 6:6,7:7,8:8,9:9}, savefig='figure0.png')`

Visualizing the graph as such and saving the graph to `figure0.png`:

![http://vispy.googlecode.com/files/figure0.png](http://vispy.googlecode.com/files/figure0.png)


## `vizMeNot()` ##
Terminates the current visualization.