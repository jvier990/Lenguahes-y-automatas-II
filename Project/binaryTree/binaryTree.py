from .tree import Tree
import os

binaryTree = Tree()
binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, 7)
binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, 4)
binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, 9)
binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, 15)
binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, 5)

def practica01():
    while True:
        os.system('cls')

        print('Arbol ABB')
        opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")

        if opc == '1':
            node = input("\nIngresa el nodo -> ")
            if node.isdigit():
                node = int(node)
                binaryTree.treeStatus = binaryTree.insert(binaryTree.treeStatus, node)
            else: 
                print('ingresa solo digitos')
        elif opc == '2':
            if binaryTree.treeStatus == None:
                print('Arbol vacio')
            else:
                binaryTree.inodern(binaryTree.treeStatus)
        elif opc == '3':
            if binaryTree == None:
                print('Arbol Vacio')
            else:
                binaryTree.preorden(binaryTree.treeStatus)
        elif opc == '4':
            if binaryTree == None:
                print('Arbol Vacio')
            else:
                binaryTree.postorden(binaryTree.treeStatus)
        elif opc == '5':
            node = input("\nIngresa el nodo a buscar -> ")
            if node.isdigit():
                node = int(node)
            if binaryTree.search(node,binaryTree.treeStatus) == None:
                print('Nodo no encontrado')
            else:
                print("\nNodo encontrado -> ",binaryTree.search(node, binaryTree.treeStatus), " si existe...")

        elif opc == '6':
            print("\nElegiste salir...\n")
            os.system("pause")
            break
        else:
            print("\nElige una opcion correcta...")
        print()
        os.system("pause")
    return None

 

        