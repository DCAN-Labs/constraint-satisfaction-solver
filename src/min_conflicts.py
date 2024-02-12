from abc import ABC, abstractmethod
import random


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints


class MinConflicts(ABC):
    @abstractmethod
    def get_initial_complete_assignment(self, csp):
        pass

    def min_conflicts(self, csp, max_steps):
        """
        The MIN-CONFLICTS algorithm for solving CSPs by local search,
        :param csp: a constraint satisfaction problem
        :param max_steps: the number of steps allowed before giving up
        :return: a solution or failure
        """
        current = self.get_initial_complete_assignment(csp)
        for i in range(max_steps):
            if self.is_solution(csp, current):
                return current
            var = self.randomly_conflicted_variable(current, csp.variables)
            min_conflicts = -1
            value = None
            for v in csp.domains[var]:
                conflict_count = self.conflicts(var, v, current, csp)
                if min_conflicts == -1 or conflict_count < min_conflicts:
                    min_conflicts = conflict_count
                    value = v
            current[var] = value

    @abstractmethod
    def is_solution(self, csp, current):
        pass

    @abstractmethod
    def randomly_conflicted_variable(self, assignment, variables):
        pass

    @abstractmethod
    def conflicts(self, var, v, current, csp):
        pass


def same_diag(pos0, pos1):
    col0 = pos0[0]
    row0 = pos0[1]
    col1 = pos1[0]
    row1 = pos1[1]
    if col1 > col0 and row1 > row0:
        return col1 - col0 == row1 - row0
    elif col1 > col0 and row1 < row0:
        return col1 - col0 == -(row1 - row0)
    else:
        return False


def conflicts():
    pass


def same_row(row0, row1):
    return row0 == row1


def different_square(pos0, pos1):
    return pos0 != pos1


def same_col(col0, col1):
    return col0 == col1


def attacks(pos0, pos1):
    col0 = pos0[0]
    row0 = pos0[1]
    col1 = pos1[0]
    row1 = pos1[1]
    return different_square((col0, row0), (col1, row1)) and \
           (same_row(row0, row1) or same_col(col0, col1) or same_diag((col0, row0), (col1, row1)))


class EightQueensProblem(MinConflicts):
    def conflicts(self, var, v, current, csp):
        pass

    def get_initial_complete_assignment(self, csp):
        return {i: 0 for i in range(8)}

    def is_solution(self, csp, current):
        for i in range(8):
            for j in range(i + 1, 8):
                if attacks((i, current[i]), (j, current[j])):
                    return False
        return True

    def randomly_conflicted_variable(self, assignment, variables):
        conflicted = []
        for column in variables:
            conflict_counts = self.get_conflict_counts(assignment, column)
            if conflict_counts[column] > 0:
                conflicted.append(column)

                continue
        return random.choice(conflicted)

    def get_conflict_counts(self, assignment, column):
        conflict_counts = [0] * 8
        for row in range(8):
            self.get_conflict_counts_for_row(assignment, column, conflict_counts, row)

        return conflict_counts

    def get_conflict_counts_for_row(self, assignment, column, conflict_counts, row):
        for c in range(8):
            if c == column:
                continue
            r = assignment[c]
            if self.attacks((column, row), (c, r)):
                conflict_counts[row] = conflict_counts[row] + 1
        return conflict_counts[row]

    def attacks(self, pos0, pos1):
        col0 = pos0[0]
        row0 = pos0[1]
        col1 = pos1[0]
        row1 = pos1[1]
        return different_square((col0, row0), (col1, row1)) and \
               (same_row(row0, row1) or same_col(col0, col1) or same_diag((col0, row0), (col1, row1)))
