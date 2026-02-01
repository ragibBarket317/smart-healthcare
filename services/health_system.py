from models.doctors import Doctor


class HealthSystem:
    
    def find_doctor(self, category, location):
        result = []
        for doctor in self.doctors:
            if doctor["category"].lower() == category.lower() and doctor["location"].lower() == location.lower():
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