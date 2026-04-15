from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

#task 2

model2 = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_intel = TabularCPD('Intelligence', 2, [[0.7], [0.3]])
cpd_study = TabularCPD('StudyHours', 2, [[0.6], [0.4]])
cpd_diff = TabularCPD('Difficulty', 2, [[0.4], [0.6]])

cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.60, 0.85, 0.30, 0.55, 0.25, 0.50, 0.10, 0.25],
        [0.30, 0.12, 0.45, 0.35, 0.45, 0.38, 0.35, 0.50],
        [0.10, 0.03, 0.25, 0.10, 0.30, 0.12, 0.55, 0.25],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],
        [0.05, 0.20, 0.50],
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

model2.add_cpds(cpd_intel, cpd_study, cpd_diff, cpd_grade, cpd_pass)
assert model2.check_model()

inference2 = VariableElimination(model2)

# Query 1
result_q1 = inference2.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
print("\nP(Pass | StudyHours=Sufficient, Difficulty=Hard)")
print(result_q1)

# Query 2
result_q2 = inference2.query(variables=['Intelligence'], evidence={'Pass': 0})
print("\nP(Intelligence | Pass=Yes)")
print(result_q2)
