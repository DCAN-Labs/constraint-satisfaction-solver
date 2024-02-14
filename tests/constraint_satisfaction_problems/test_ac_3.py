from unittest import TestCase

from ac_3 import ac_3


class Test(TestCase):
    def test_ac_3(self):
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
        csp = (X, D, C)
        can_be_satisfied = ac_3(csp)
        print(can_be_satisfied)
        self.assertTrue(can_be_satisfied)
