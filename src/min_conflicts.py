from abc import ABC, abstractmethod
import random


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
            vs = []
            for v in csp.domains[var]:
                conflict_count = self.conflicts(var, v, current, csp)
                if min_conflicts == -1 or conflict_count <= min_conflicts:
                    min_conflicts = conflict_count
            for v in csp.domains[var]:
                conflict_count = self.conflicts(var, v, current, csp)
                if conflict_count == min_conflicts:
                    vs.append(v)
            value = random.choice(vs)

            current[var] = value
        return None

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
        return col1 - col0 == row0 - row1
    elif col1 < col0 and row1 < row0:
        return col0 - col1 == row0 - row1
    elif col1 < col0 and row1 > row0:
        return col0 - col1 == row1 - row0
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
    return \
        different_square((col0, row0), (col1, row1)) and (same_row(row0, row1) or
                                                          same_col(col0, col1) or same_diag((col0, row0), (col1, row1)))


class EightQueensProblem(MinConflicts):
    def conflicts(self, var, v, current, csp):
        current_copy = current.copy()
        current_copy[var] = v
        count = self.get_conflict_counts_for_row(current_copy, var, v)

        return count

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
            conflict_counts = self.get_conflict_counts_for_row(assignment, column, assignment[column])
            if conflict_counts > 0:
                conflicted.append(column)

        return random.choice(conflicted)

    def get_conflict_counts(self, assignment, column):
        conflict_counts = [0] * 8
        for row in range(8):
            conflict_counts[row] = self.get_conflict_counts_for_row(assignment, column, row)

        return conflict_counts

    @staticmethod
    def get_conflict_counts_for_row(assignment, column, row):
        conflict_counts = 0
        for c in range(8):
            if c == column:
                continue
            r = assignment[c]
            if attacks((column, row), (c, r)):
                conflict_counts += 1
        return conflict_counts
