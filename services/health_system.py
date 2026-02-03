class HealthSystem:
    def __init__(self, data):
        self.data = data
        self.doctors = data.load("doctors.json")
    
    def find_doctor(self, category_id):
        result = []
        for doctor in self.doctors:
            if doctor["category_id"] == category_id:
                result.append(doctor)

        if len(result) > 0:
            return result

        return "Not found any doctor"    

    def search_doctor(self, name=None, category=None, location=None, rating=None):
        result = []

        for doctor in self.doctors:
            if name.lower() not in doctor["name"].lower():
                continue
            if category.lower() not in doctor["category"].lower():
                continue
            if location.lower() not in doctor["location"].lower():
                continue
            if rating and doctor["rating"] < rating:
                continue

            result.append(doctor)

        if len(result) > 0:
            return result

        return "Not found any doctor"     