import re, random
from graphviz import Digraph

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tokenize(expr):
    return re.findall(r'\d+|[()+\-*/]', expr)

def infix_to_postfix(tokens):
    prec = {'+':1, '-':1, '*':2, '/':2}
    out, stack = [], []
    for t in tokens:
        if t.isdigit():
            out.append(t)
        elif t in prec:
            while stack and stack[-1] in prec and prec[stack[-1]] >= prec[t]:
                out.append(stack.pop())
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
    out += reversed(stack)
    return out

def build_tree(postfix):
    st = []
    for t in postfix:
        if t.isdigit():
            st.append(Node(int(t)))
        else:
            r, l = st.pop(), st.pop()
            st.append(Node(t, l, r))
    return st[0]

def eval_tree(node):
    if isinstance(node.value, int):
        return node.value
    l, r = eval_tree(node.left), eval_tree(node.right)
    return {'+': l+r, '-': l-r, '*': l*r, '/': l/r}[node.value]

def draw_tree(node, filename):
    g = Digraph()
    def rec(n):
        nid = str(id(n))
        g.node(nid, str(n.value))
        if n.left:
            g.edge(nid, str(id(n.left)))
            rec(n.left)
        if n.right:
            g.edge(nid, str(id(n.right)))
            rec(n.right)
    rec(node)
    return g.render(filename, format='png', cleanup=True)

# Exemplo fixo
expr = '(((7+3)*(5-2))/(10*20))'
tokens = tokenize(expr)
postfix = infix_to_postfix(tokens)
tree = build_tree(postfix)
print('Expressão:', expr)
print('Postfix:', postfix)
print('Valor:', eval_tree(tree))
print('Árvore salva em:', draw_tree(tree, 'fixed_tree'))

# Exemplo aleatório
def gen_tree(k):
    if k == 0:
        return Node(random.randint(1, 20))
    op = random.choice(['+','-','*','/'])
    left = gen_tree(random.randint(0, k-1))
    right = gen_tree(k-1 - random.randint(0, k-1))
    if op == '/' and isinstance(right.value, int) and right.value == 0:
        right.value = random.randint(1, 20)
    return Node(op, left, right)

rand_tree = gen_tree(2)
print('Expressão randômica:', eval_tree(rand_tree))
print('Árvore randômica salva em:', draw_tree(rand_tree, 'random_tree'))