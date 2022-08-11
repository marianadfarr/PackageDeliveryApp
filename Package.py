'''
The package class creates package objects with
id, address, zip code, deadline, weight, status, and time_delivered parameters
'''
class Package:
    def __init__(self, id, address, city, zipcode, deadline, weight, status, time_delivered):
        self.ID = id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.time_delivered = time_delivered

    def __str__(self):  # overwrite print(package) otherwise it will print object reference in memory instead
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.deadline, self.city, self.zipcode, self.weight, self.status,
            self.time_delivered)

#For printing to the console after a given user input

    def print_status_for_time(self, time_requested, truck_start_time):
        if self.time_delivered < time_requested:
            status = "Delivered"
        elif time_requested < truck_start_time:
            status = "At Hub"
        else:
            status = "En Route"
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.deadline, self.city, self.zipcode, self.weight, status, self.time_delivered)
