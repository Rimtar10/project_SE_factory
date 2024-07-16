class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

    def __str__(self): #str means display a string
        #describe the driver
        driver_info = "Driver ID: " + str(self.worker_id) + ", Name: " + self.name + ", Start City: " + self.start_city
        return driver_info
    
class City:
    def __init__(self, name):
        self.name = name
        self.destinations = []

    def add_destination(self, destination):
        self.destinations.append(destination)
    
    def __str__(self):
        city_info = "City: " + self.name + ", Destinations: "
        for destination in self.destinations:
            city_info += destination + ", "
        if self.destinations:
            city_info = city_info[:-2]
            #remove the last comma and space example: "city1, city2"
        return city_info
    
def main_menu(drivers, cities):
    while True:
        print("Hello! Please enter:")
        print("1- To go to the drivers menu")
        print("2- To go to the cities menu")
        print("3- To exit the system")

        choice= input("Enter your choice: ")
        if choice == "1":
            driver_menu(drivers, cities)
        elif choice == "2":
            cities_menu(drivers, cities)
        elif choice == "3":
            print("exiting, Goodbye!")
            break
        else:
            print("Invalid input, please try again")

def driver_menu(drivers, cities):
    while True:
        print("DRIVER'S MENU")
        print("Enter:")
        print("1- To view all the drivers")
        print("2- To add a driver")
        print("3- To go back to main menu")
        choice = input("Your choice: ")

        if choice == "1":
            view_drivers(drivers)
        if choice == "2":
            add_driver(drivers, cities)
        if choice == "3":
            print("Going back to main menu")
            break
        else:
            print("Invalid input, please try again")

def view_drivers(drivers):
    if drivers:  
        print("DRIVERS LIST")
        for driver in drivers:
            print(driver)
    else:
        print("No drivers available.")

def add_driver(drivers, cities):
    name = input("Enter the driver's name: ")
    start_city = input("Enter the driver's start city: ")

    # Check if the start city exists
    if start_city not in cities:
        add_city = input(start_city + " do not exist. Do you want to add it? (yes/no): ").strip().lower() #strip: remove white spaces from the beginning and end
        if add_city == "yes":
            cities[start_city] = City(start_city)
            print(start_city + " has been added.")
        else:
            print("Cannot add driver without a valid start city.")
            return
    while True:
        destination_city = input("Enter a destination city for " + start_city + " (or 'done' to finish): ")
        if destination_city.lower() == 'done':
            break
        if destination_city not in cities:
            cities[destination_city] = City(destination_city)
            print(destination_city + " has been added.")
        cities[start_city].add_destination(destination_city)

        
    # Generate a new worker ID
    worker_id = "ID" + str(len(drivers) + 1).zfill(3) #zfill: fill the string with zeros until it reaches the specified length

    # Add the driver to the list
    new_driver = Driver(worker_id, name, start_city)
    drivers.append(new_driver)
    print("Driver " + str(new_driver) + " has been added.")


def cities_menu(drivers, cities):
    while True:
        print("cities menu")
        print("Enter:")
        print("1- To show all cities")
        print("2- To print neighboring cities")
        print("3- To print drivers delivering to a city")
        print("4- To go back to main menu")
        choice = input("Your choice: ")

        if choice == "1":
            show_cities(cities)
        elif choice == "2":
            print_neighboring_cities(cities)
        elif choice == "3":
            print_drivers_delivering_to_city(drivers, cities)
        elif choice == "4":
            print("Going back to main menu...")
            break
        else:
            print("Invalid input, please try again")


def show_cities(cities):
    if cities:
        print("cities list: ")
        for city in cities.values(): # to iterate over values in the dict without accessing each key
            print(city)
    else:
        print("No cities available.")



def print_neighboring_cities(cities):
    city_name = input("Enter the city name: ")
    if city_name in cities:
        city = cities[city_name]
        if city.destinations:
            print("Neighboring cities to " + city_name + ":")
            for destination in city.destinations:
                print(destination)
        else:
            print("No neighboring cities found for " + city_name)
    else:
        print("City " + city_name + " not found.")


def print_drivers_delivering_to_city(drivers, cities):
    city_name = input("Enter the city name: ")
    if city_name in cities:
        # empty set to keep track of visited cities
        visited = set()
        # empty set to keep track of reachable cities
        reachable_cities = set()
        # list to use as a queue, starting with the given city name
        queue = [city_name]

        while queue:
            current_city = queue.pop(0) # remove and return the first element from a queue
            if current_city not in visited:
                visited.add(current_city)
                reachable_cities.add(current_city)
                for destination in cities[current_city].destinations:
                    if destination not in visited:
                        queue.append(destination)

        delivering_drivers = []

        for driver in drivers:
            if driver.start_city in reachable_cities:
                delivering_drivers.append(driver)

        if delivering_drivers:
            print("Drivers delivering to " + city_name + ":")
            for driver in delivering_drivers:
                print(driver)

        else:
            print("No drivers delivering to " + city_name )

    else:
        print("City " + city_name + " not found.")


# Initialize the drivers and cities databases
drivers = []
cities = {
    "Beirout": City("Beirout"),
    "Zahle": City("Zahle"),
    "Baabda": City("Baabda"),
}


cities["Beirout"].add_destination("Zahle")
cities["Zahle"].add_destination("Baabda")
cities["Baabda"].add_destination("Beirout")

if __name__ == "__main__":
    main_menu(drivers, cities)