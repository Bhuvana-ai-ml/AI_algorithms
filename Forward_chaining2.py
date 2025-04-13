
symptoms = {
    'john': {'fever', 'cough', 'shortness_of_breath'},
    'alice': {'headache', 'runny_nose', 'sneezing'}
}

disease_definitions = {
    'covid': {'fever', 'cough', 'shortness_of_breath'},
    'flu': {'fever', 'cough', 'runny_nose'},
    'common_cold': {'runny_nose', 'sneezing', 'headache'}
}

def diagnose(person):
    person_symptoms = symptoms.get(person, set())
    possible_diseases = []
    
    for disease, required_symptoms in disease_definitions.items():
        if required_symptoms.issubset(person_symptoms):
            possible_diseases.append(disease)
    
    return possible_diseases


print("John has:", diagnose('john'))    
print("Alice has:", diagnose('alice'))  
