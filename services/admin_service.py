class AdminService:
    def __init__(self, data):
        self.data = data

    def add_doctor(self):
        # doctors = self.data.load("doctors.json")
        
        # name = input("Enter doctor name: ")
        # cat_id = int(input("Category Id: "))
        # exp = int(input("Experience: "))
        # rating = float(input("Rating: "))

        # new_id = max([d["id"] for d in doctors], default=0) + 1

        # doctors.append({
        #     "id": new_id,
        #     "name": name,
        #     "category_id": cat_id,
        #     "experience": exp,
        #     "rating": rating
        # })

        # self.data.save("doctors.json", doctors)
        # print("Doctor added")

        name = input("Enter doctor name: ")
        cat_id = int(input("Category Id: "))
        exp = int(input("Experience: "))
        rat = float(input("Rating: "))

        query = """
        INSERT INTO doctors(name, category_id, experience, rating)
        VALUES(?, ?, ?, ?)
        """

        self.data.execute(query, (name, cat_id, exp, rat))
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
        name = input("Enter category name: ")

        query = """
        INSERT INTO categories(name)
        VALUES(?)
        """

        self.data.execute(query, (name,))
        print("Category added")


    def  add_symptom(self):
       name = input("Symptom name: ")
       weight = int(input("Weight: "))

       query = """
        INSERT INTO symptoms(name, weight)
        VALUES(?, ?)
        """
       
       self.data.execute(query, (name, weight))
       print("Symptom added")

    def add_mapping(self):
        sym_id = int(input("Symptom id: "))
        cat_id = int(input("Category id: "))
        

        query = """
            INSERT INTO mapping(symptom_id, category_id)
            VALUES(?, ?)
            """
        
        self.data.execute(query, (sym_id, cat_id))
        print("Mapping complete")