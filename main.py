from services.health_system import HealthSystem
from utils.load_data import DataLoader
from services.admin_service import AdminService
from services.symptom_service import SymptomEngine
from utils.load_data_with_db import DataLoadWithDB
from database.init_db import init_db

data = DataLoader()
data_db = DataLoadWithDB()
init_db(data_db)


admin = AdminService(data_db)
system = HealthSystem(data_db)
symptom_eng = SymptomEngine(data)

def main():
    while True:
        print("_____Smart HealthCare_____")
        print("1. Find Doctor")
        print("2. Find Doctor by symptoms: ")
        print("3. Admin Panel")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            cat = int(input("Category_id: "))

            doctors = system.find_doctor(cat)
            print(f"Result: {doctors}")

        elif choice == "2":
            sym = input("Enter your symptom: ")

            symptom = sym.split(",")

            category = symptom_eng.recomendation(symptom)
            # print(f"category: {category}")
            for cat_id, weight in category:
                cat = symptom_eng.get_category(cat_id)
                doctors = system.find_doctor(cat_id)
                for doc in doctors:
                    print(f"Doctor Name: {doc["name"]} Category: {cat["name"]}, Weigth: {weight}")
                

        elif choice == "3":
            while True:
                print("\n--- Admin Panel ---")
                print("1. Add Doctor")
                print("2. Add Diagnostic")
                print("3. Add Category")
                print("4. Add Symptom")
                print("5. Add Symptom-Category Mapping")
                print("6. Back")


                admin_choice = input("Choose: ")

                if admin_choice == "1":
                    admin.add_doctor()
                elif admin_choice == "2":
                    admin.add_diagnostic()
                elif admin_choice == "3":
                    admin.add_category()
                elif admin_choice == "4":
                    admin.add_symptom()
                elif admin_choice == "5":
                    admin.add_mapping()
                else:
                    break

        else:
            break


main()                    
             
      

