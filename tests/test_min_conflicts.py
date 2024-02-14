import itertools
from unittest import TestCase

from csp import CSP
from min_conflicts import EightQueensProblem, attacks


class TestMinConflicts(TestCase):
    def test_min_conflicts(self):
        eight_queens_problem = EightQueensProblem()
        variables = list(range(8))
        domains = dict()
        for i in range(8):
            domains[i] = list(range(8))
        constraints = \
            {(col0, col1): [[row0, row1] for row0, row1 in itertools.product(range(8), repeat=2)
                            if not attacks((col0, row0), (col1, row1))]
             for col0, col1 in itertools.product(range(8), repeat=2)}
        csp = CSP(variables, domains, constraints)
        solution = eight_queens_problem.min_conflicts(csp, 64)
        print(solution)

    def test_get_conflict_counts(self):
        assignments = [6, 3, 1, 4, 7, 5, 2, 0]
        col = 7
        expected_values = [1, 2, 1, 3, 2, 1, 2, 2]
        eight_queens_problem = EightQueensProblem()
        actual_values = eight_queens_problem.get_conflict_counts(assignments, col)
        self.assertListEqual(expected_values, actual_values)

    def test_get_conflict_counts_2(self):
        assignments = [6, 3, 1, 4, 7, 5, 2, 5]
        col = 5
        expected_values = [0, 3, 2, 3, 2, 1, 3, 3]
        eight_queens_problem = EightQueensProblem()
        actual_values = eight_queens_problem.get_conflict_counts(assignments, col)
        self.assertListEqual(expected_values, actual_values)

    def test_attacks(self):
        assignments = [6, 3, 1, 4, 7, 5, 2, 6]
        col0 = 5
        row0 = 3
        conflicts = [[1, 3], [6, 2], [7, 5]]
        for row1 in range(8):
            for col1 in range(8):
                if assignments[col1] != row1:
                    continue
                if col1 == col0:
                    continue
                conflict = attacks((col0, row0), (col1, row1))
                if [col1, row1] in conflicts:
                    conflict_sentence = "Should conflict"
                else:
                    conflict_sentence = "Shouldn't conflict"
                self.assertEqual(conflict, [col1, row1] in conflicts,
                                 f'{conflict_sentence}: [({col1}, {row1})]: {conflict}')

    def test_get_conflict_counts_for_row(self):
        assignments = [6, 3, 1, 4, 7, 5, 2, 5]
        col = 5
        eight_queens_problem = EightQueensProblem()
        row = 3
        actual_value = eight_queens_problem.get_conflict_counts_for_row(assignments, col, row)
        expected_value = 3
        self.assertEqual(actual_value, expected_value)

    def test_same_diag(self):
        self.assertTrue((0, 0), (7, 7))
        self.assertTrue((7, 7), (0, 0))
        self.assertTrue((0, 7), (7, 0))
        self.assertTrue((7, 0), (0, 7))
