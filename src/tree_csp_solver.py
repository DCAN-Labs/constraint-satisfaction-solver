import itertools
import random

from CC import CC
from Graph import Graph


def concatenate(*lists):
    return itertools.chain(*lists)


def topological_sort(variables, tree, root):
    if len(variables) == 0:
        return [root]
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
            new_variables = variables.copy()
            new_variables.remove(root)
            rec_result = topological_sort(new_variables, reduced_tree, new_root)
            result += rec_result

        return result


def parent(variable):
    pass


def make_arc_consistent(parent_variable, variable):
    pass


def any_consistent_value(domain):
    pass


def decompose_into_disjoint_trees(csp):
    pass


def get_csp(v):
    pass


def tree_csp_solver(csp):
    """
    The TREE-CSP-SOLVER algorithm for solving tree-structured CSPs.  If the CSP has a solution, we will find it in
    linear time; if not, we will detect a contradiction.
    :param csp: a CSP with components X, D, C
    :return: a solution, or failure
    """
    graph = create_graph_from_csp(csp)
    cc: CC = CC(graph)
    n = len(csp.variables)
    assignment = dict()
    root = random.choice(csp.variables)
    tree = [c for c in csp.constraints]
    connected_component_count: int = cc.count
    sub_csps = []
    for i in range(connected_component_count):
        sub_csps[i] = get_csp(i)
        csp.variables = topological_sort(csp.variables, tree, root)
        for j in range(n, 1, -1):
            arc_consistent = make_arc_consistent(parent(csp.variables[j]), csp.variables[j])
            if not arc_consistent:
                return None
        for j in range(n):
            consistent_value = any_consistent_value(csp.domains[j])
            if consistent_value:
                assignment[csp.variables[j]] = consistent_value
            else:
                return None
        return assignment


def create_graph_from_csp(csp):
    graph: Graph = Graph(len(csp.variables))
    for edge in [c for c in csp.constraints.keys()]:
        graph.add_edge(csp.variables.index(edge[0]), csp.variables.index(edge[1]))
    return graph
