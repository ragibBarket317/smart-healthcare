from services.health_system import HealthSystem

print("_____Smart HealthCare_____")

system = HealthSystem()

print("1. Find Doctor")
print("2. Search Doctor")

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