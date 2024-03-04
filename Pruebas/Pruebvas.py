import networkx as nx
import matplotlib.pyplot as plt

# Creamos un árbol binario utilizando NetworkX
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])

# Definimos una disposición en cascada para el árbol
pos = {0: (0, 1), 1: (-1, 0), 2: (1, 0), 3: (-2, -1), 4: (0, -1), 5: (0, -2), 6: (2, -1)}

# Dibujamos el árbol binario con la disposición en cascada
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=12)

# Insertamos un nuevo nodo
new_node = max(G.nodes()) + 1  # Creamos un nuevo nodo
parent_node = 2  # Nodo padre al que queremos agregar el nuevo nodo
G.add_edge(parent_node, new_node)  # Agregamos una arista desde el nodo padre al nuevo nodo

# Mostramos el árbol binario actualizado
plt.show()