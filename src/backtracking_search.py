from abc import ABC, abstractmethod
import operator


class BacktrackingSearch(ABC):
    def __init__(self, csp):
        self.csp = csp

    @abstractmethod
    def select_unassigned_variable(self, assignment):
        pass

    @abstractmethod
    def order_domain_values(self, var, assignment):
        pass

    def complete(self, assignment):
        X = self.csp[0]
        for x in X:
            if x not in assignment.keys():
                return False
        return True

    def backtrack(self, assignment):
        if self.complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            inferences = dict()
            if self.assignment_is_consistent(assignment, var, value):
                assignment[var] = value
                inferences = self.inference(assignment, var, value)
                if inferences is not None:
                    assignment.extend(inferences)
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
            assignment.pop(var)
            for key in inferences.keys():
                assignment.pop(key)
        return None

    def backtracking_search(self):
        self.backtrack(dict())

    @abstractmethod
    def inference(self, assignment, var, value):
        pass

    def consistent(self, assignment):
        variables = list(assignment.keys())
        n = len(variables)
        C = self.csp[2]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                arc = (variables[i], variables[j])
                if arc in C:
                    valid_vals = C[arc]
                    actual_vals = (assignment[arc[0]], assignment[arc[1]])
                    if actual_vals not in valid_vals:
                        return False
        return True

    def assignment_is_consistent(self, assignment, var, value):
        extended_assignment = assignment.copy()
        extended_assignment[var] = value

        return self.consistent(extended_assignment)


class AustraliaColoring(BacktrackingSearch):
    def inference(self, assignment, var, value):
        return self.forward_checking(assignment, var, value)

    def select_unassigned_variable(self, assignment):
        X = self.csp[0]
        min_remaining_values = -1
        D = self.csp[1]
        for x in X:
            if x in assignment.keys():
                continue
            if min_remaining_values == -1 or len(D[x]) < min_remaining_values:
                min_remaining_values = len(D[x])
        keys_with_min = [key for key in D.keys() if len(D[key]) == min_remaining_values]
        if len(keys_with_min) == 1:
            return keys_with_min[0]
        else:
            max_degree = -1
            max_degree_var = None
            for x in X:
                if x in assignment.keys():
                    continue
                degree = 0
                C = self.csp[2]
                for c in C.keys():
                    if x == c[0] or x == c[1]:
                        degree += 1
                if max_degree == -1 or degree > max_degree:
                    max_degree_var = x
                    max_degree = degree
            return max_degree_var

    def get_neighboring_variables(self, var):
        C = self.csp[2]
        neighboring_variables = []
        for c in C.keys():
            if var == c[0]:
                neighboring_variables.append(c[1])
            elif var == c[1]:
                neighboring_variables.append(c[0])
        return neighboring_variables

    def get_value_constraints(self, assignment, variable):
        neighboring_variables = self.get_neighboring_variables(variable)
        D = self.csp[1]
        possible_values = D[variable]
        value_to_constraint_factor = {d: 1 for d in D[variable]}
        for value in possible_values:
            extended_assignment = assignment.copy()
            extended_assignment[variable] = value
            for neighboring_variable in neighboring_variables:
                legal_values_left = self.get_legal_values_left_count(extended_assignment, neighboring_variable)
                value_to_constraint_factor[value] = value_to_constraint_factor[value] * legal_values_left
        return value_to_constraint_factor

    def order_domain_values(self, assignment, var):
        constraints = self.get_value_constraints(var, assignment)
        sorted_d = sorted(constraints.items(), key=operator.itemgetter(1), reverse=True)
        sorted_list = [v[0] for v in sorted_d]

        return sorted_list

    def get_legal_values_left_count(self, assignment, neighboring_variable):
        if neighboring_variable in assignment.keys():
            return 1
        else:
            count = 0
            D = self.csp[1]
            for value in D[neighboring_variable]:
                extended_assignment = assignment.copy()
                extended_assignment[neighboring_variable] = value
                if self.consistent(extended_assignment):
                    count += 1
            return count

    def forward_checking(self, assignment, var, value):
        pass
