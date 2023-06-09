from DecisionTree import Tree

f1 = Tree([-3, -3])
f2 = Tree([-1, -10])
f3 = Tree([-10, -1])
f4 = Tree([-2, -2])

f5 = Tree("Jogador 2", f1, f2)
f6 = Tree("Jogador 2", f3, f4)

root = Tree("Jogador 1", f5, f6)

print(root)
print("Resultado pareto-eficiente: " + str(root.pareto_efficient_output()))
print("Equilíbrio de Nash: " + str(root.nash_equilibrium()) + "\n")

f1 = Tree([8, 7])
f2 = Tree([10, 11])
f3 = Tree([11, 14])
f4 = Tree([9, 13])

f5 = Tree("Jogador 2", f1, f2)
f6 = Tree("Jogador 2", f3, f4)

root = Tree("Jogador 1", f5, f6)

print(root)
print("Resultado pareto-eficiente: " + str(root.pareto_efficient_output()))
print("Equilíbrio de Nash: " + str(root.nash_equilibrium()))