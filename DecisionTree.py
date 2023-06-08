class Tree:
    value = None
    left = None  # árvore à esquerda
    right = None  # árvore à direita

    # construtor para nó interno, folha ou raiz
    def __init__(self, value, left_tree=None, right_tree=None):
        self.value = value
        self.left = left_tree
        self.right = right_tree

    def __str__(self):
        return self._stringify("")

    def _stringify(self, string: str):
        string += '(' + str(self.value)
        if self.left is not None:
            string = self.left._stringify(string)
        if self.right is not None:
            string = self.right._stringify(string)
        return string + ')'

class Output:
    value: list

    def __init__(self, o1: int, o2: int):
        self.value = [o1, o2]

    def __str__(self):
        return str(self.value)
