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
    
def main_menu():
    while True:
        print("Hello! Please enter:")
        print("1- To add a driver")
        print("2- To add a city")
        print("3- To exit the system")

        choice= input("Enter your choice: ")
        if choice == "1":
            add_driver()
        elif choice == "2":
            add_city()
        elif choice == "3":
            print("exiting, Goodbye!")
            break
        else:
            print("Invalid input, please try again")

def driver_menu():
    while True:
        print("\nDRIVER'S MENU")
        print("Enter:")
        print("1- To view all the drivers")
        print("2- To add a driver")
        print("3- To go back to main menu")
        choice = input("Your choice: ")

        if choice == "1":
            view_drivers()
        if choice == "2":
            add_driver()
        if choice == "3":
            print("Going back to main menu...")
            break
        else:
            print("Invalid input, please try again")


