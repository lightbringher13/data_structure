"""
binary tree: https://www.youtube.com/watch?v=LnxEBW29DOw
binary tree: each node has max 2 or min 0 node
node, link == edge, root node, child node, parent node
path length: num of edges
leaf node: the last node no child node
level, height
"""

"""
binary tree expression

list:
1.
a = [a,b,c,None,d,e,f,None,None,h,i,g,None,None,None]

2.
a = [a,[a's left tree],[a's right tree]]
a = [a,[b, [], [d, [], [] ]], [c, [e,[],[] ], [f, [] [] ]]]

3.
use node class
class Node:
    def __init__(self):
        self.data = data
        self.right = None
        self.left = None
"""
