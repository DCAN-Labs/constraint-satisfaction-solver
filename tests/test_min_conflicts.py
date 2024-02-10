from unittest import TestCase
import itertools

from min_conflicts import EightQueensProblem, CSP


class TestMinConflicts(TestCase):
    def test_min_conflicts(self):
        eight_queens_problem = EightQueensProblem()
        variables = list(range(8))
        domains = {range(8): range(8)}
        constraints = \
            {(col0, col1):
                 [[row0, row1] for row0, row1 in itertools.product(range(8), repeat=2)
                  if not eight_queens_problem.attacks(row0, col0, row1, col1)] for col0, col1 in
             itertools.product(range(8), repeat=2)}
        csp = CSP(variables, domains, constraints)
        solution = eight_queens_problem.min_conflicts(csp, 64)
        print(solution)

    def test_get_conflict_counts(self):
        assignments = [6, 3, 1, 4, 7, 5, 2, 0]
        col = 7
        expected_values = [-1, 2, 1, 3, 2, 1, 2, 2]
        eight_queens_problem = EightQueensProblem()
        actual_values = eight_queens_problem.get_conflict_counts(assignments, col)
        self.assertListEqual(expected_values, actual_values)
