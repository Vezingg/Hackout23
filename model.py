from sklearn.tree import DecisionTreeClassifier

# Sample database of cases (symptoms, disease)
database = [
    ("00000", "DiseaseA"),
    ("10001", "DiseaseB"),
    ("10101", "DiseaseC"),
    ("10111","DiseaseD"),
    ("11111","DiseaseC"),
    # ... Add more cases here
]

X = [list(symptom) for symptom, _ in database]
y = [disease for _, disease in database]

model = DecisionTreeClassifier()
model.fit(X, y)
