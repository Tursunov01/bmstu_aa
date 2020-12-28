from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
import operator
from threading import Thread

def isOperator(c):
    if (c == "+" or c == "-" or c == "*"
        or c == "/"):
        return True
    else:
        return False

OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
@dataclass
class Node:
    data: str
    left: Optional[Node] = None
    right: Optional[Node] = None

res = []

@dataclass
class Tree:
    root: Node


    def post_order(self, node: Optional[Node]) -> None:
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            if isOperator(node.data) == False:
                res.append(int(node.data))
            else:
                tmp = OPERATORS[node.data](res[-2], res[-1])
                del res[-1]
                del res[-1]
                res.insert(1, tmp)
                


    def height(self,node):
      if node==None:
          return 0
      else:
        lheight = self.height(node.left)
        rheight = self.height(node.right)
    
        if lheight > rheight:
            return(lheight+1)
        else:
          return(rheight+1)





if __name__ == "__main__":

    j = Node("6")
    k = Node("2")
    h = Node("+", j, k)
    i = Node("3")
    d = Node("*", h, i)
    e = Node("4")
    b = Node("-", d, e)
    f = Node("7")
    g = Node("3")
    c = Node("+", f, g)
    a = Node("/", b, c)

    tree = Tree(a)
    h1 = tree.height(a.left)
    h2 = tree.height(a.right)
    w1 = 4 if h1 > h2 else 1
    w2 = 2 if h1 < h2 else 1
    for i in range(w1):
        th = Thread(target = tree.post_order, args=(a.left, )) 
        th.start()
    for i in range(w2):
        th = Thread(target = tree.post_order, args=(a.right, )) 
        th.start()
    print("Result = ", OPERATORS[a.data](res[0], res[1]))