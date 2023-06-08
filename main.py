from DecisionTree import *

f1 = Tree(Output(-3, -3))
f2 = Tree(Output(-1, -10))
f3 = Tree(Output(-10, -1))
f4 = Tree(Output(-2, -2))

f5 = Tree("Jogador 2", f1, f2)
f6 = Tree("Jogador 2", f3, f4)

root = Tree("Jogador 1", f5, f6)

print(root)
