from DecisionTree import Tree

f1 = Tree([-7, -8, -8])
f2 = Tree([-6, -6, -12])
f3 = Tree([-6, -10, -6])
f4 = Tree([100, 15, -12])
f5 = Tree([20, -6, -6])
f6 = Tree([14, 100, 12])
f7 = Tree([12, 2, 0])
f8 = Tree([-4, -4, -4])

no3_1 = Tree("Jogador 3", f1, f2)
no3_2 = Tree("Jogador 3", f3, f4)
no3_3 = Tree("Jogador 3", f5, f6)
no3_4 = Tree("Jogador 3", f7, f8)

no2_1 = Tree("Jogador 2", no3_1, no3_2)
no2_2 = Tree("Jogador 2", no3_3, no3_4)

raiz = Tree("Jogador 1", no2_1, no2_2)

print("Resultado do jogo: " + str(raiz.nash_equilibrium()))
print("Resultado mais eficiente: " + str(raiz.pareto_efficient_output()))

cc = [3, 3]
cnc = [6, 0]
ncc = [0, 6]
ncnc = [5, 5]

f1 = Tree(cc)
f2 = Tree(cnc)
f3 = Tree(ncc)
f4 = Tree(ncnc)

j2_1c = Tree("Jogador 2", f1, f2)
j2_1nc = Tree("Jogador 2", f3, f4)
j1 = Tree("Jogador 1", j2_1c, j2_1nc)
print("\nResultado do jogo: " + str(j1.nash_equilibrium()))
print("Resultado mais eficiente: " + str(j1.pareto_efficient_output()))
