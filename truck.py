'''The truck class initiates truck objects which holds truck ID,
 mileage, an associated packages list, departure time, current address,
current time'''


class Truck:
    def __init__(self, id, mileage, packages_list, departure_time, current_address, current_time):
        self.ID = id
        self.mileage = mileage
        self.packages_list = packages_list  # package objects, from the hashtable
        self.departure_time = departure_time
        self.current_address = current_address
        self.current_time = current_time
        self.original_packages = packages_list.copy()

    def __str__(self):  # overwrite print(truck) otherwise it will print object reference in memory instead
        return "%s, %s, %s %s %s %s" % (
            self.ID, self.mileage, self.packages_list, self.departure_time, self.current_address, self.current_time)
