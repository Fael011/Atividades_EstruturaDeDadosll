import random
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def rec(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = rec(node.left, value)
            elif value > node.value:
                node.right = rec(node.right, value)
            return node
        self.root = rec(self.root, value)

    def search(self, value):
        def rec(node, value):
            if not node:
                return None
            if node.value == value:
                return node
            elif value < node.value:
                return rec(node.left, value)
            else:
                return rec(node.right, value)
        return rec(self.root, value)

    def delete(self, value):
        def rec(node, value):
            if not node:
                return None
            if value < node.value:
                node.left = rec(node.left, value)
            elif value > node.value:
                node.right = rec(node.right, value)
            else:
                # Caso 1: folha
                if not node.left and not node.right:
                    return None
                # Caso 2: um filho
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # Caso 3: dois filhos
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.value = succ.value
                node.right = rec(node.right, succ.value)
            return node
        self.root = rec(self.root, value)

    def height(self):
        def rec(node):
            if not node:
                return -1
            return 1 + max(rec(node.left), rec(node.right))
        return rec(self.root)

    def depth(self, value):
        def rec(node, value, d):
            if not node:
                return -1
            if node.value == value:
                return d
            elif value < node.value:
                return rec(node.left, value, d+1)
            else:
                return rec(node.right, value, d+1)
        return rec(self.root, value, 0)

    def draw(self, filename):
        g = Digraph()
        def rec(node):
            if not node:
                return
            nid = str(id(node))
            g.node(nid, str(node.value))
            if node.left:
                g.edge(nid, str(id(node.left)))
                rec(node.left)
            if node.right:
                g.edge(nid, str(id(node.right)))
                rec(node.right)
        rec(self.root)
        g.render(filename, format='png', cleanup=True)
        print(f'Árvore salva em: {filename}.png')

# Demonstração com valores fixos
bst = BinarySearchTree()
valores_fixos = [55, 30, 80, 20, 45, 70, 90]
for v in valores_fixos:
    bst.insert(v)
print("Árvore com valores fixos:")
bst.draw('bst_fixa')

print("Busca pelo valor 45:", bst.search(45) is not None)
bst.delete(30)
print("Árvore após remover 30:")
bst.draw('bst_fixa_removido_30')
bst.insert(35)
print("Árvore após inserir 35:")
bst.draw('bst_fixa_inserido_35')
print("Altura da árvore:", bst.height())
print("Profundidade do nó 45:", bst.depth(45))

# Demonstração com valores aleatórios
bst_rand = BinarySearchTree()
valores_rand = random.sample(range(1, 201), 15)
print("Valores aleatórios:", valores_rand)
for v in valores_rand:
    bst_rand.insert(v)
print("Árvore aleatória:")
bst_rand.draw('bst_aleatoria')
print("Altura da árvore aleatória:", bst_rand.height())