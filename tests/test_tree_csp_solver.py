from unittest import TestCase

from csp import CSP
from tree_csp_solver import tree_csp_solver, topological_sort


class TreeCSPSolverTest(TestCase):
    def test_tree_csp_solver(self):
        X = ['WA', 'NT', 'Q', 'NSW', 'V', 'T']
        D = dict()
        for x in X:
            D[x] = ['red', 'green', 'blue']
        # sa = 'red'
        C = {('WA', 'NT'): [('green', 'blue'), ('blue', 'green')],
             ('NT', 'Q'): [('green', 'blue'), ('blue', 'green')],
             ('Q', 'NSW'): [('green', 'blue'), ('blue', 'green')],
             ('NSW', 'V'): [('green', 'blue'), ('blue', 'green')]}
        csp = CSP(X, D, C)
        can_be_satisfied = tree_csp_solver(csp)
        print(can_be_satisfied)
        self.assertTrue(can_be_satisfied)

    def test_topological_sort(self):
        tree = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['D', 'E'], ['D', 'F']]
        root = 'A'
        expected_result = ['A', 'B', 'C', 'D', 'E', 'F']
        variables = ['A', 'B', 'C', 'D', 'E', 'F']
        actual_result = topological_sort(variables, tree, root)
        self.assertListEqual(expected_result, actual_result)

    def test_topological_sort_2(self):
        tree0 = [['NSW', 'V'], ['NT', 'Q'], ['NSW', 'Q'], ['NT', 'WA']]
        root0 = 'WA'
        tree1 = []
        root1 = 'T'
        expected_result = ['WA', 'NT', 'Q', 'NSW', 'V', 'T']
        variables0 = ['NSW', 'NT', 'Q', 'T', 'V', 'WA']
        variables1 = ['T']
        actual_result = topological_sort(variables0, tree0, root0) + topological_sort(variables1, tree1, root1)
        self.assertListEqual(expected_result, actual_result)
