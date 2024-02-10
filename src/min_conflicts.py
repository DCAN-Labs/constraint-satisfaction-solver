from abc import ABC, abstractmethod


class CSP():
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


class EightQueensProblem(MinConflicts):
    def get_initial_complete_assignment(self, csp):
        return {i: 0 for i in range(8)}

    def is_solution(self, csp, current):
        for i in range(8):
            for j in range(i + 1, 8):
                if self.attacks(i, current[i], j, current[j]):
                    return False
        return True

    def randomly_conflicted_variable(self, assignment, variables):
        pass

    def conflicts(self, var, v, current, csp):
        pass

    def same_row(self, row0, row1):
        return row0 == row1

    def different_square(self, row0, col0, row1, col1):
        return row0 != row1 or col0 != col1

    def same_col(self, col0, col1):
        return col0 == col1

    def same_diag(self, row0, col0, row1, col1):
        if row0 == row1 and col0 == col1:
            return False
        row_diff = max(row1, row0) - min(row1, row0)
        col_diff = max(col1, col0) - min(col1, col0)

        return row_diff == col_diff

    def attacks(self, row0, col0, row1, col1):
        return self.different_square(row0, col0, row1, col1) and \
               (self.same_row(row0, row1) or self.same_col(col0, col1) or self.same_diag(row0, col0, row1, col1))

    def get_conflict_counts(self, assignment, column):
        conflict_counts = [-1] * 8
        for row in range(8):
            count = 0
            for col in range(8):
                assigned_r = assignment[col]
                if assigned_r == row:
                    continue
                if self.attacks(assigned_r, column, row, col):
                    count += 1
            conflict_counts[row] = count
        conflict_counts[assignment[column]] = -1

        return conflict_counts
