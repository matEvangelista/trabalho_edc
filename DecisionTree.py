class Tree:

    # construtor para nó interno, folha ou raiz
    def __init__(self, value, left_tree=None, right_tree=None):
        self._value = value
        self._left = left_tree
        self._right = right_tree

    def __str__(self):
        return self._stringify("")

    def _stringify(self, string: str):
        string += '(' + str(self._value)
        if self._left is not None:
            string = self._left._stringify(string)
        if self._right is not None:
            string = self._right._stringify(string)
        return string + ')'

    def nash_equilibrium_output(self):
        if (self.leftmost_value(0) >= self._right.leftmost_value(0)
                and self._left.rightmost_value(0) >= self.rightmost_value(0)):
            return self._left._best_strategy()
        if (self._right.leftmost_value(0) > self.leftmost_value(0)
                and self.rightmost_value(0) > self._left.rightmost_value(0)):
            return self._right._best_strategy()

    def pareto_efficient_output(self) -> list:
        outputs: list = self._get_all_outputs()
        pareto: list = self.nash_equilibrium_output()
        n1, n2 = self.nash_equilibrium_output()
        for output in outputs:
            if output[0] > n1 and output[1] > n2:
                pareto = output
        return pareto

    def _get_all_outputs(self) -> list:
        if self._left is None and self._right is None:
            return [self._value]
        outputs: list = []
        if self._left is not None:
            outputs += (self._left._get_all_outputs())
        if self._right is not None:
            outputs += (self._right._get_all_outputs())
        return outputs

    def _best_strategy(self) -> list:
        if self._left._value[1] >= self._right._value[1]:
            return self._left._value
        return self._right._value

    def leftmost_value(self, index: int) -> int:
        if self.is_output():
            return self._value[index]
        return self._left.leftmost_value(index)

    def rightmost_value(self, index: int) -> int:
        if self.is_output():
            return self._value[index]
        return self._right.rightmost_value(index)

    def is_output(self) -> bool:
        return self._left is None and self._right is None
