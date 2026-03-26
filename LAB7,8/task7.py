# Task 7

from ortools.sat.python import cp_model
 
model = cp_model.CpModel()

n = 4
 
queens = []
for i in range(n):
    queens.append(model.NewIntVar(0, n-1, f'q{i}'))

# Constraint: no same column
model.AddAllDifferent(queens)

# Constraint: no same diagonal
for i in range(n):
    for j in range(i + 1, n):
        model.Add(queens[i] - queens[j] != i - j)
        model.Add(queens[i] - queens[j] != j - i)
 
solver = cp_model.CpSolver()
status = solver.Solve(model)
 
if status == cp_model.FEASIBLE:
    print("4-Queens Solution:\n")
    for i in range(n):
        row = ["_"] * n
        row[solver.Value(queens[i])] = "Q"
        print(" ".join(row))
else:
    print("No solution found")
