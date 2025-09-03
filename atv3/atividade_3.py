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

    def inorder(self):
        def rec(node):
            if not node:
                return []
            return rec(node.left) + [node.value] + rec(node.right)
        return rec(self.root)

    def preorder(self):
        def rec(node):
            if not node:
                return []
            return [node.value] + rec(node.left) + rec(node.right)
        return rec(self.root)

    def postorder(self):
        def rec(node):
            if not node:
                return []
            return rec(node.left) + rec(node.right) + [node.value]
        return rec(self.root)

# Árvore com valores fixos
bst_fixa = BinarySearchTree()
valores_fixos = [55, 30, 80, 20, 45, 70, 90]
for v in valores_fixos:
    bst_fixa.insert(v)
print("Árvore com valores fixos:")
bst_fixa.draw('bst_fixa')

print("Travessia INORDER (Esquerda-Raiz-Direita):", bst_fixa.inorder())
print("Travessia PREORDER (Raiz-Esquerda-Direita):", bst_fixa.preorder())
print("Travessia POSTORDER (Esquerda-Direita-Raiz):", bst_fixa.postorder())
print("-" * 50)

# Árvore com valores randômicos
bst_rand = BinarySearchTree()
valores_rand = random.sample(range(1, 101), 10)
for v in valores_rand:
    bst_rand.insert(v)
print("Árvore com valores randômicos:", valores_rand)
bst_rand.draw('bst_rand')

print("Travessia INORDER (Esquerda-Raiz-Direita):", bst_rand.inorder())
print("Travessia PREORDER (Raiz-Esquerda-Direita):", bst_rand.preorder())
print("Travessia POSTORDER (Esquerda-Direita-Raiz):", bst_rand.postorder())