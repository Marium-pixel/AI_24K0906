#task5:
 

from ortools.sat.python import cp_model

 
model = cp_model.CpModel()
 
A = model.NewIntVar(0, 3, 'A')
B = model.NewIntVar(0, 3, 'B')
C = model.NewIntVar(0, 3, 'C')

# Constraints
model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)
 
class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, A, B, C):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.A = A
        self.B = B
        self.C = C
        self.count = 0

    def OnSolutionCallback(self):
        self.count += 1
        print(f"Solution {self.count}: A={self.Value(self.A)}, B={self.Value(self.B)}, C={self.Value(self.C)}")

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True

solution_printer = SolutionPrinter(A, B, C)
solver.Solve(model, solution_printer)
