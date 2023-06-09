from DecisionTree import Tree

f1 = Tree([-3, -3])
f2 = Tree([-1, -10])
f3 = Tree([-10, -1])
f4 = Tree([-2, -2])

f5 = Tree("Jogador 2", f1, f2)
f6 = Tree("Jogador 2", f3, f4)

root = Tree("Jogador 1", f5, f6)

print(root)
print(root.nash_equilibrium_output())
print(root.pareto_efficient_output())
