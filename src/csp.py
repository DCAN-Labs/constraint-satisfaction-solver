class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def make_arc_consistent(self, parent_variable, variable):
        constraints = self.constraints[(parent_variable, variable)]
        sub_domain = [c[0] for c in constraints]

        return sub_domain
