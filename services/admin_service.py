class AdminService:
    def __init__(self, data):
        self.data = data

    def add_doctor(self):
        doctors = self.data.load("doctors.json")
        
        name = input("Enter doctor name: ")
        cat_id = int(input("Category Id: "))
        exp = int(input("Experience: "))
        rating = float(input("Rating: "))

        new_id = max([d["id"] for d in doctors], default=0) + 1

        doctors.append({
            "id": new_id,
            "name": name,
            "category_id": cat_id,
            "experience": exp,
            "rating": rating
        })

        self.data.save("doctors.json", doctors)
        print("Doctor added")



    def  add_diagnostic(self):
        diagnostics = self.data.load("diagnostics.json")

        name = input("Enter diagnostic name: ")
        loc = input("Enter your location: ")
        rating = float(input("Enter your rating: "))

        new_id = max([d["id"] for d in diagnostics], default=0) + 1

        diagnostics.append({
            "id": new_id,
            "name": name,
            "location": loc,
            "rating": rating
        })

        self.data.save("diagnostics.json", diagnostics)
        print("Diagnostics added")

    def add_category(self):
        pass

    def  add_symptom(self):
        pass

    def add_mapping(self):
        pass 