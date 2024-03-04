from .node import Node
import networkx as nx
import matplotlib.pyplot as plt

class Tree:
    def __init__(self):
        self.treeStatus = None
        self.G = nx.Graph()

    def getGraph(self):
        return self.G
    
    def defPositions(self,node,pos,x,y):
        
        if node is not None:
            if (x,y) in pos.values():
                pos[node.data] = (x + 0.75, y +0.5)
            else:
                pos[node.data] = (x , y)

        if node.left is not None:
            self.defPositions(node.left, pos, x - 2, y - 1)
        if node.right is not None:
            self.defPositions(node.right, pos, x + 2, y - 1)

        print(pos)
        return pos    


    def insert(self,node,data):
        if node == None:
            node = Node(data)
        else:
            if data < node.data:
                if node.left is None:
                    self.G.add_edge(node.data, data)
                node.left = self.insert(node.left,data)
            else:
                if node.right is None:
                    self.G.add_edge(node.data, data)
                node.right = self.insert(node.right,data)
        return node
    
    #izquierdo, raíz, derecha
    def inodern(self, node):
        if node == None:
            return None
        else:                           # Empieza por 7
            self.inodern(node.left)     # Pasa por:     4,null,null,null,null           
            print(node.data)            # Imprime:      4,5,7,9,15
            self.inodern(node.right)    # Pasa por:     5,null,9,15,null   
    #raiz,izq,derecha
    def preorden(self,node):
        if node == None:
            return None
        else:                           #Empieza por 7
            print(node.data)            #Imprime:       7,4,5,9,15         
            self.preorden(node.left)    #Pasa por:      4,null,null,null,null
            self.preorden(node.right)   #Pasa por:      5,null,9,15,null
   #izquierdo, derecha, raíz
    def postorden(self,node):
        if node == None:
            return None
        else:                           #Empieza por 7 
            self.postorden(node.left)   #Pasa por:      4,null,null,null,null              
            self.postorden(node.right)  #Pasa por:      5,null,9,15,null
            print(node.data)            #Imprime:       5,4,15,9,7
    
    def search(self,data,node):
        if node == None:
            return None
        else:
            if data == node.data:
                return node.data
            else:
                if int(data) < node.data:
                    return self.search(data,node.left)
                else:
                    if data > node.data:
                        return self.search(data,node.right)

    def find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteInGraph(self, node, data):
        if node is None:
            return node

        if data == node:
            father = None
            for i, j in self.G.edges():
                if i == data:
                    father = j
                    break
            if father is not None:
                for child in nx.descendants(self.G, data):
                    self.G.add_edge(father, child)
            self.G.remove_node(data)
            return None

        if data < node.data:
            self.G.remove_edge(node, data)
            self.delete(data, data)
        else:
            self.G.remove_edge(node, data)
            self.delete(data, data)

        return node
    
    def delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.find_min_node(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        return node
