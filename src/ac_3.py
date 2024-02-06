from collections import deque


def revise(csp, x_i, x_j):
    """
    returns true iff we revise the domain of x_i
    """
    D = csp[1]
    C = csp[2]
    revised = False
    for x in D[x_i]:
        found_satisfaction = False
        for y in D[x_j]:
            if (x_i, x_j,) in C.keys() and (x, y) in C[(x_i, x_j)]:
                found_satisfaction = True
        if not found_satisfaction:
            if x_i in D and x in D[x_i]:
                D[x_i].remove(x)
                revised = True

    return revised


def neighbors(C, x):
    neighborhood = []
    for c in C.keys():
        if c[0] == x:
            neighborhood.append(c[1])
        elif c[1] == x:
            neighborhood.append(c[0])

    return neighborhood


def ac_3(csp):
    """returns false if an inconsistency is found and true otherwise

    Parameters:
    csp: a binary CSP with components (X, D, C)

    Returns:
    int:Returning value
   """
    D = csp[1]
    C = csp[2]
    queue = deque()
    for c in C:
        queue.append(c)
    while len(queue) > 0:
        c = queue.popleft()
        x_i = c[0]
        x_j = c[1]
        if revise(csp, x_i, x_j):
            if len(D[x_i]) == 0:
                return False
            for x_k in neighbors(C, x_i):
                if x_k != x_j:
                    queue.append((x_k, x_i))
    return True
