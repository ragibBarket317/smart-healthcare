class Doctor:
    def __init__(self, name, category, location, rating):
        self.name = name
        self.category = category
        self.location = location
        self.rating = rating

    def __str__(self):
        return f"Doctor Name: {self.name}, Category: {self.category}, Location: {self.location}, Rating:{self.rating}"
    



