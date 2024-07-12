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