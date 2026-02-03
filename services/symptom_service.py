from collections import defaultdict
class SymptomEngine:
    def __init__(self, data):
        self.symptoms = data.load("symptoms.json")
        self.mapping = data.load("mapping.json")
        self.categories = data.load("categories.json")

    def get_category(self, cat_id):
        for cat in self.categories:
            if cat["id"] == cat_id:
                return cat

        return None

    def get_symptom(self, symptom):
        for sym in self.symptoms:
            if sym["name"].lower() == symptom.lower():
                return sym
        return None    

    def recomendation(self, symptoms):
        scores = defaultdict(int)

        for symptom in symptoms:
            single_symptom = self.get_symptom(symptom)

            if not single_symptom:
                continue
            for m in self.mapping:
                if m["symptom_id"] == single_symptom["id"]:
                    scores[m["category_id"]] += single_symptom["weight"]

        return sorted(scores.items(), key=lambda x:x[1], reverse=True)            