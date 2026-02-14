class HealthSystem:
    def __init__(self, data):
        self.data = data
    
    def all_doctors(self):
        query = "SELECT * FROM doctors"
        doctors = self.data.fetch_all(query)
        if doctors:
            return doctors
        return "Empty doctor list"
    def find_doctor(self, category_id):
        query = "SELECT * FROM doctors WHERE category_id = ?"
        doctors = self.data.fetch_one(query, (category_id,))

        if doctors:
            return doctors
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
        
