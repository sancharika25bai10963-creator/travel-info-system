# utils.py

def show_autos(auto_list):
    print("\n--- Auto Options ---")
    for a in auto_list:
        print(f"Name: {a['name']}")
        print(f"Price: ₹{a['price']}")
        print(f"Contact: {a['contact']}\n")


def show_cabs(cab_list):
    print("\n--- Cab Options ---")
    for c in cab_list:
        print(f"Type: {c['type']}")
        print(f"Price: ₹{c['price']}")
        print(f"Contact: {c['contact']}\n")


def show_buses(bus_list):
    print("\n--- Bus Options ---")
    for b in bus_list:
        print(f"Route: {b['route']}")
        print(f"Timing: {b['time']}")
        print(f"Fare: ₹{b['fare']}\n")
