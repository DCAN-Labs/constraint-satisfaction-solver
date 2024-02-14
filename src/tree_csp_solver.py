import itertools
import random


def concatenate(*lists):
    return itertools.chain(*lists)


def topological_sort(tree, root):
    if len(tree) == 0:
        return []
    else:
        links_to_recurse_on = [link for link in tree if link[0] == root or link[1] == root]
        result = [root]
        for link in links_to_recurse_on:
            reduced_tree = tree.copy()
            reduced_tree.remove(link)
            new_root = None
            if root == link[0]:
                new_root = link[1]
            elif root == link[1]:
                new_root = link[0]
            rec_result = topological_sort(reduced_tree, new_root)
            result += rec_result

        return result


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
