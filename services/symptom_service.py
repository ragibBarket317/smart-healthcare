from collections import defaultdict
class SymptomEngine:
    def __init__(self, data):
        self.data = data
        # self.symptoms = data.load("symptoms.json")
        # self.mapping = data.load("mapping.json")
        # self.categories = data.load("categories.json")

    def get_category(self, cat_id):
        query = "SELECT * FROM categories WHERE id = ?"
        cat = self.data.fetch_one(query, (cat_id,))

        if cat:
            return cat
        return None


    def get_symptom(self, symptom):  
        query = "SELECT * FROM symptoms"
        find_symptoms = self.data.fetch_all(query)

        for sym in find_symptoms:
            if sym["name"].lower() == symptom.lower():
                return sym

        return None    

    def recomendation(self, symptoms):
        scores = defaultdict(int)
        query = "SELECT * FROM mapping"
        all_map = self.data.fetch_all(query)

        for symptom in symptoms:
            single_symptom = self.get_symptom(symptom)
            print(f"S SYM: {single_symptom}")

            if not single_symptom:
                continue
            for m in all_map:
                if m["symptom_id"] == single_symptom["id"]:
                    scores[m["category_id"]] += single_symptom["weight"]

        return sorted(scores.items(), key=lambda x:x[1], reverse=True)            