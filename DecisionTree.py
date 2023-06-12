def _pareto_improvement(stt1: list, stt2: list) -> bool:
    for i in range(len(stt1)):
        if stt1[i] < stt2[i]:
            return False
    return True


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

    def nash_equilibrium(self, count: int = 0) -> list:
        if type(self._right._value) is list and type(self._left._value) is list:
            return self._best_strategy(count)
        s1: list = self._left.nash_equilibrium(count + 1)
        s2: list = self._right.nash_equilibrium(count + 1)
        return s1 if s1[count] > s2[count] else s2

    def pareto_efficient_output(self) -> list:
        outputs: list = self._get_all_outputs()
        pareto: list = self.nash_equilibrium()
        for output in outputs:
            if _pareto_improvement(output, pareto):
                pareto = output
        return pareto

    def _get_all_outputs(self) -> list:
        if self._left is None and self._right is None:
            return [self._value]
        outputs: list = []
        if self._left is not None:
            outputs += self._left._get_all_outputs()
        if self._right is not None:
            outputs += self._right._get_all_outputs()
        return outputs

    def _best_strategy(self, index: int) -> list:
        if self._left._value[index] >= self._right._value[index]:
            return self._left._value
        return self._right._value

    def _is_output(self) -> bool:
        return self._left is None and self._right is None
