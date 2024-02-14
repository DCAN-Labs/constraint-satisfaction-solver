import random


def topological_sort(variables, root):
    pass


def parent(variable):
    pass


def make_arc_consistent(parent_variable, variable):
    pass


def any_consistent_value(domain):
    pass


def tree_csp_solver(csp):
    """
    The TREE-CSP-SOLVER algorithm for solving tree-structured CSPs.  If the CSP has a solution, we will find it in
    linear time; if not, we will detect a contradiction.
    :param csp: a CSP with components X, D, C
    :return: a solution, or failure
    """
    n = len(csp.variables)
    assignment = dict()
    root = random.choice(csp.variables)
    csp.variables = topological_sort(csp.variables, root)
    for j in range(n, 1, -1):
        arc_consistent = make_arc_consistent(parent(csp.variables[j]), csp.variables[j])
        if not arc_consistent:
            return None
    for i in range(n):
        consistent_value = any_consistent_value(csp.domains[i])
        if consistent_value:
            assignment[csp.variables[i]] = consistent_value
        else:
            return None
    return assignment
