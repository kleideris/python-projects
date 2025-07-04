from collections import deque
#TODO add enumerate and the ability to choose if you take out a car by plate or by number.
def display_garage(garage: dict[str, str]) -> None:
    if garage:
        print("Current cars in the garage:")
        for plate, car in garage.items():
            print(f"{plate:7} — Car: {car}")
    else:
        print("The garage is empty")

def add_car_to_garage(garage: dict[str, str], max_capacity: int) -> None:
    if len(garage) >= max_capacity:
        print("The garage is full. Cannot add more cars.")

    user_input = input("Enter the car's plate and the name seperated by coma (ex: ABC123, Toyota Corolla): ")

    try:
        plate, car_name = map(str.strip, user_input.split(","))
    except ValueError:
        print("Invalid format. Please enter the plate and car name separated by a comma.")

    if not plate.strip() or not car_name.strip():
         print("Both plate and name are required.")
         return
    
    if plate in garage:
        print(f"Plate {plate} already exists.")
        return

    garage[plate] = car_name
    print(f"{car_name} with plate {plate} has been added.")
   
def remove_car_from_garage(garage: dict[str, str], plate: str) -> None:
    if not garage:
        print("Garage is empty. No cars to remove.")
        return
    if plate in garage:
        car_left = garage.pop(plate)
        print(f"{car_left} with plate {plate} has left the garage.")
    else:
        print(f"There are no cars in the garage with plate '{plate}'.")



def get_garage(use_defaults=False):
    """
    Initializes the garage with defaults car for testing purposes.

    Params:
        use_defaults (bool): Whether to include the DEFAULT_CARS preset.

    Returns:
        dict: a copy of DEFAULT_CARS if use_defaults is True, otherwise an empty dict.
    """
    DEFAULT_CARS = {"XXX1234": "toyota", "YYY5678": "mini cooper"}
    return DEFAULT_CARS.copy() if use_defaults else {}


def main():
    MAX_CAPACITY = 100
    garage = get_garage(use_defaults=True)
    
    while True:
        print("\nChoose an operation:")
        print("1. Display garage")
        print("2. Add a car to the garage")
        print("3. Remove a car from the garage")
        print("4. Exit")

        try:
            choice = int(input("Please choose an option number 1 and 4: "))
        except ValueError:
            print("Invalid input.")
            continue
        
        match choice:
            case 1:
                display_garage(garage)
            case 2:
                add_car_to_garage(garage, MAX_CAPACITY)
            case 3:
                plate = input("Enter the plate of the car you want to remove: ").strip()
                remove_car_from_garage(garage, plate)
            case 4:
                print("Goodbye")
                break
            case _:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()