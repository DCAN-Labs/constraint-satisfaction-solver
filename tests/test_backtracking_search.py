from unittest import TestCase

from backtracking_search import AustraliaColoring


class TestAustraliaColoring(TestCase):
    def test_backtracking(self):
        X, D, C = self.get_csp()
        australiaColoring = AustraliaColoring(X, D, C)
        can_be_satisfied = australiaColoring.backtracking_search()
        print(can_be_satisfied)
        self.assertTrue(can_be_satisfied)

    @staticmethod
    def get_csp():
        X = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        D = dict()
        for x in X:
            D[x] = ['red', 'green', 'blue']
        C = {('SA', 'WA'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                            ('blue', 'green')],
             ('SA', 'NT'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                            ('blue', 'green')],
             ('SA', 'Q'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                           ('blue', 'green')],
             ('SA', 'NSW'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                             ('blue', 'green')],
             ('SA', 'V'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                           ('blue', 'green')],
             ('WA', 'NT'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                            ('blue', 'green')],
             ('NT', 'Q'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                           ('blue', 'green')],
             ('Q', 'NSW'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                            ('blue', 'green')],
             ('NSW', 'V'): [('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'blue'), ('blue', 'red'),
                            ('blue', 'green')]}
        return X, D, C

    def test_get_least_constraining_value(self):
        X, D, C = self.get_csp()
        australiaColoring = AustraliaColoring(X, D, C)
        partial_assignment = {'WA': 'red', 'NT': 'green'}
        next_var = 'Q'
        value_to_constraints = australiaColoring.get_value_constraints(partial_assignment, next_var)
        self.assertEqual(value_to_constraints['blue'], 0)
        self.assertGreater(value_to_constraints['red'], value_to_constraints['blue'])

    def test_get_legal_values_left_count(self):
        X, D, C = self.get_csp()
        australiaColoring = AustraliaColoring(X, D, C)
        partial_assignment = {'WA': 'red', 'NT': 'green'}
        next_var = 'Q'

        extended_assignment = partial_assignment.copy()
        extended_assignment[next_var] = 'blue'
        actual_blue_legal_values_left_count = australiaColoring.get_legal_values_left_count(extended_assignment, 'SA')
        self.assertEqual(actual_blue_legal_values_left_count, 0)

        extended_assignment = partial_assignment.copy()
        extended_assignment[next_var] = 'red'
        actual_red_legal_values_left_count = australiaColoring.get_legal_values_left_count(extended_assignment, 'SA')
        self.assertGreater(actual_red_legal_values_left_count, 1)

    def test_inference(self):
        pass

    def test_forward_checking(self):
        X, D, C = self.get_csp()
        australiaColoring = AustraliaColoring(X, D, C)
        australiaColoring.D = D
        assignment = dict()
        australiaColoring.D = australiaColoring.forward_checking(assignment, 'WA', 'red')
        assignment['WA'] = 'red'
        australiaColoring.D = australiaColoring.forward_checking(assignment, 'Q', 'green')
        assignment['Q'] = 'green'
        self.assertEquals(len(australiaColoring.D['NT']), 1)
        self.assertEquals(len(australiaColoring.D['SA']), 1)

        X, D, C = self.get_csp()
        assignment = dict()
        australiaColoring = AustraliaColoring(X, D, C)
        australiaColoring.D = australiaColoring.forward_checking(assignment, 'WA', 'red')
        australiaColoring.D = australiaColoring.forward_checking(assignment, 'Q', 'green')
        australiaColoring.D = australiaColoring.forward_checking(assignment, 'V', 'blue')
        self.assertEquals(len(australiaColoring.D['SA']), 0)
