from .node import Node
import networkx as nx
import matplotlib.pyplot as plt

class Tree:
    def __init__(self):
        self.treeStatus = None
        self.G = nx.Graph()
        self.root = None

    def setRoot(self,root):
        self.root = root
    def getRoot(self):
        return self.root
    def getGraph(self):
        print(self.G.edges)
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
    def find_min_nodeForRoot(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current
    

    def getData(self,node):
        return node.data
    

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
    
    def delete2(self, node, data):
        if node is None:
            return node
    
        # Si el nodo a eliminar es la raíz
        if data == node.data:
            # Si el nodo raíz no tiene hijos
            if node.left is None and node.right is None:
                return None
            # Si el nodo raíz solo tiene un hijo
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Si el nodo raíz tiene dos hijos
            else:
                temp = self.find_min_node(node.right)
                node.data = temp.data
                node.right = self.delete(node.right, temp.data)
                return node

        # Si el nodo a eliminar no es la raíz, continuar con el proceso habitual
        if data < node.data:
            node.left = self.delete(node.left, data)
        else:
            node.right = self.delete(node.right, data)

        return node
    

    def deleteInGraph(self, node, data):
        if node is None:
            return node
        if data == node.data:
            print('Nodos:')
            print(self.G.nodes)
            print('Aristas:')
            print(self.G.edges)  
            father = None
            for i, j in self.G.edges():
                if j == data:
                    father = i
            print(data,',',node.data)
            if(data == self.getRoot()):
                temp = self.find_min_nodeForRoot(node.right)
                temp = self.getData(temp)               
                self.G.remove_edge(data, self.getData(node.left))
                self.G.remove_edge(data, self.getData(node.right))
                self.G.remove_edge(self.getData(node.right), temp)
                self.G.remove_edge(data, self.getData(node.right))
                self.G.add_edge( self.getData(node.right) , self.getData(node.left))
                return None

            if node.left is None and node.right is not None:
                self.G.add_edge(father, self.getData(node.right))
                self.G.remove_edge(father, data)
                self.G.remove_edge(data, self.getData(node.right))
                self.G.remove_node(data)
                return None

            if node.right is None and node.left is not None:
                self.G.add_edge(father, self.getData(node.left))
                self.G.remove_edge(father, data)
                self.G.remove_edge(data, self.getData(node.left))
                self.G.remove_node(data)
                return None

            if node.right is None and node.left is None:
                
                self.G.remove_edge(father, data)
                self.G.remove_node(data)
                return None


            temp = self.find_min_node(node.right)
            temp = self.getData(temp)
            self.G.add_edge(father,temp)
            self.G.add_edge(temp, self.getData(node.left))
            self.G.remove_edge(father, data)
            self.G.remove_edge(data, self.getData(node.right))
            self.G.remove_edge(data, self.getData(node.left))
            self.G.remove_node(data)
            print('Nodos:')
            print(self.G.nodes)
            print('Aristas:')
            print(self.G.edges)          
            return None

        if data < node.data:
            self.deleteInGraph(node.left, data)
        elif data > node.data:

            self.deleteInGraph(node.right, data)

        return node
  