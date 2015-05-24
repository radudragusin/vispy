# Introduction #

We have extended the built-in list data structure with methods to visualize
lists of arbitrary length.


# Details #

You may instantiate the list as such:
  * from list import `*`
  * L = list(), generates and empty list
  * L = list( [1,2,3,4 ] ), generate list with [1,2,3,4 ](.md) content

You now have access to the following methods:
  * vizMe(figNum) - visualizes the list in a separate window, where 'fignum' refers to which window, default=1.
  * vizMeNot() - closes visualization.
  * randomMe(size) - generates and occupies a list of random numbers of specified length=size.