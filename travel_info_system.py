from transport_data import autos, cabs, buses
from utils import show_autos, show_cabs, show_buses


emergency_contacts = [
    {"service": "VIT Bhopal Security", "contact": "0755-1234567"},
    {"service": "Local Police", "contact": "100"},
    {"service": "Fire Department", "contact": "101"},
    {"service": "Ambulance", "contact": "108"},
]

def search_transport(keyword):
    if not keyword:  
        return []

    keyword = keyword.lower()
    results = []

    
    for a in autos:
        if keyword in a["name"].lower():
            results.append(("Auto", a))

    
    for c in cabs:
        if keyword in c["type"].lower():
            results.append(("Cab", c))
    for b in buses:
        if keyword in b["route"].lower() or keyword in b["time"].lower():
            results.append(("Bus", b))

    return results

def show_emergency_contacts():
    print("\n--- Emergency Contacts ---")
    for e in emergency_contacts:
        print(f"{e['service']}: {e['contact']}")
    print("\nThanks, Wishing You a Trip!\n")

def main():
    print("\n--- VIT Bhopal → Bhopal City Transport Information System ---")
    print("1. Auto Options")
    print("2. Cab Options")
    print("3. Bus Options")
    print("4. Search")
    print("5. Emergency Contacts")
    print("6. Exit\n")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_autos(autos)
        print("Thank you, Have a Safe Journey!")

    elif choice == "2":
        show_cabs(cabs)
        print("Thank you, Have a Safe Journey!")

    elif choice == "3":
        show_buses(buses)
        print("Thank you, Have a Safe Journey!")

    elif choice == "4":
        keyword = input("Type what you wish to look for (Swift, ISBT, 6 PM): ")

        results = search_transport(keyword)
        if results:            print("\n--- Search Results ---")
            for category, item in results:
                print(f"\nCategory: {category}")
                for key, value in item.items():
                    print(f"{key.capitalize()}: {value}")
        else:
            print("\nNo matches were found for your query.")
            print("\nThanks, Wishing You a Safe Trip!")

    elif choice == "5":
        show_emergency_contacts()

    elif choice == "6":
        print("\nThank you Wishing You a Safe Trip!")
        return

    else:
        print("\nInvalid choice. Please enter 1–6.")
        print("Thank you, Have a Safe Journey!")
if __name__ == "__main__":
    main()

