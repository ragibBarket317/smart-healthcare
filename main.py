from services.health_system import HealthSystem
from utils.load_data import DataLoader
from services.admin_service import AdminService

data = DataLoader()
admin = AdminService(data)
system = HealthSystem()

def main():
    while True:
        print("_____Smart HealthCare_____")
        print("1. Find Doctor")
        print("2. Search Doctor")
        print("3. Admin Panel")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            cat = input("Category: ")
            loc = input("Location: ")

            doctors = system.find_doctor(cat, loc)
            print(f"Result: {doctors}")

        elif choice == "2":
            name = input("Doctor name: ")
            cat = input("Category: ")
            loc = input("Location: ")
            rat = input("Rating: ")

            doctors = system.search_doctor(name, cat, loc, rat)
            print(f"Result: {doctors}")

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
             
      

