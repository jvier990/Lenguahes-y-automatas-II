import os

from Calculadora.calculator import lexer
from utils.isAcceptable import isAcceptable as practica01
from binaryTree.binaryTree import BinaryTree as practica02


def improvMenu():
    while True:
        os.system('cls')

        print('Lenguajes y Automatas II')
        opc = input("\n1.-Aritmeticamente Correcto \n2.-Arbol Binario \n3.-Tokens para calculadora \n6.-Salir \n\nElige una opcion -> ")
        if opc == '1':
            practica01()
        if opc == '2':
            practica02()
            print("\nElegiste salir...\n")
            os.system("pause")
            break
        if opc == '3':
            expression = input('Ingresa tu expresion matematica: ')
            print(f'Aqui esatn tus resultados: {lexer(expression)}')

            print("\nElegiste salir...\n")
            os.system("pause")
            break
        elif opc == '6':
            print("\nElegiste salir...\n")
            os.system("pause")
            break
        else:
            print("\nElige una opcion correcta...")
        print()
        os.system("pause")
    return None
improvMenu()