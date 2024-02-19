import itertools

from CC import CC
from Graph import Graph
from csp import CSP


def concatenate(*lists):
    return itertools.chain(*lists)


def topological_sort(variables, tree, root):
    if len(variables) == 0:
        return [root]
    else:
        tree_list = list(tree)
        links_to_recurse_on = [link for link in tree_list if link[0] == root or link[1] == root]
        result = [root]
        for link in links_to_recurse_on:
            reduced_tree = tree_list.copy()
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


def parent(tree, topological_sorting, variable):
    index = topological_sorting.index(variable)
    for i in range(index - 1, 0, -1):
        if (variable, topological_sorting[i]) in tree or (topological_sorting[i], variable) in tree:
            return topological_sorting[i]


def any_consistent_value(domain):
    pass


def decompose_into_disjoint_trees(csp):
    pass


def get_sub_csp(cc: CC, csp: CSP, v: int) -> CSP:
    sub_variables = []
    for i in range(len(csp.variables)):
        csp_variable: str = csp.variables[i]
        if cc.id[i] == v:
            sub_variables.append(csp_variable)
    sub_domains = dict()
    sub_constraints = dict()
    for variable in sub_variables:
        sub_domains[variable] = csp.domains[variable]
    for i in range(len(sub_variables)):
        for j in range(len(sub_variables)):
            key = (sub_variables[i], sub_variables[j])
            if key in csp.constraints.keys():
                sub_constraints[key] = csp.constraints[key]
    csp: CSP = CSP(sub_variables, sub_domains, sub_constraints)

    return csp


def tree_csp_solver(csp):
    """
    The TREE-CSP-SOLVER algorithm for solving tree-structured CSPs.  If the CSP has a solution, we will find it in
    linear time; if not, we will detect a contradiction.
    :param csp: a CSP with components X, D, C
    :return: a solution, or failure
    """
    graph = create_graph_from_csp(csp)
    cc: CC = CC(graph)
    connected_component_count: int = cc.count
    sub_csps = [get_sub_csp(cc, csp, i) for i in range(connected_component_count)]
    assignment = dict()
    for i in range(len(sub_csps)):
        sub_csp = sub_csps[i]
        sub_csp.variables = topological_sort(sub_csp.variables, sub_csp.constraints.keys(), sub_csp.variables[0])
        n = len(sub_csp.variables)
        for j in range(n - 1, 1, -1):
            parent_variable = parent(sub_csp.constraints.keys(), sub_csp.variables, sub_csp.variables[j])
            sub_domain = \
                sub_csp.make_arc_consistent(
                    parent_variable,
                    sub_csp.variables[j])
            if not sub_domain:
                return None
            else:
                sub_csp.domains[parent_variable] = sub_domain
        for j in range(n):
            consistent_value = any_consistent_value(sub_csp.domains[j])
            if consistent_value:
                assignment[sub_csp.variables[j]] = consistent_value
            else:
                return None
    return assignment


def create_graph_from_csp(csp):
    graph: Graph = Graph(len(csp.variables))
    for edge in [c for c in csp.constraints.keys()]:
        graph.add_edge(csp.variables.index(edge[0]), csp.variables.index(edge[1]))
    return graph
