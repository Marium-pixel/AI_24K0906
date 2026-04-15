from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

#task 3

model3 = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills'),
])

cpd_disease = TabularCPD('Disease', 2, [[0.3], [0.7]])

cpd_fever = TabularCPD('Fever', 2,
                       [[0.9, 0.5], [0.1, 0.5]],
                       evidence=['Disease'], evidence_card=[2])

cpd_cough = TabularCPD('Cough', 2,
                       [[0.8, 0.6], [0.2, 0.4]],
                       evidence=['Disease'], evidence_card=[2])

cpd_fatigue = TabularCPD('Fatigue', 2,
                         [[0.7, 0.3], [0.3, 0.7]],
                         evidence=['Disease'], evidence_card=[2])

cpd_chills = TabularCPD('Chills', 2,
                        [[0.6, 0.4], [0.4, 0.6]],
                        evidence=['Disease'], evidence_card=[2])

model3.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
assert model3.check_model()

inference3 = VariableElimination(model3)

# Inference 1
res1 = inference3.query(variables=['Disease'], evidence={'Fever': 0, 'Cough': 0})
print("\nP(Disease | Fever=Yes, Cough=Yes)")
print(res1)

# Inference 2
res2 = inference3.query(variables=['Disease'], evidence={'Fever': 0, 'Cough': 0, 'Chills': 0})
print("\nP(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
print(res2)

# Inference 3
res3 = inference3.query(variables=['Fatigue'], evidence={'Disease': 0})
print("\nP(Fatigue | Disease=Flu)")
print(res3)
