'''
Name: Mariana Farr
Student ID:  008491124
WGU Data Structures and Algorithms II (c950)
'''

import csvreader
import datetime
import truck
''''
Load package data to hash table: 
Time Complexity: O(N)
Space Complexity: O(N)
'''
csvreader.loadPackageData('Packages.csv')

''''
Load the trucks with their appropriate packages
Time Complexity: O(1)
Space Complexity: O(N)
'''
truck_one_ids = [25, 26, 29, 7, 40, 4, 31, 6, 23, 32]
truck_two_ids = [15, 16, 34, 14, 13, 19, 36, 38, 3, 5, 37, 30, 12, 20, 18, 1]
truck_three_ids = [28, 21, 17, 8, 9, 24, 27, 35, 39, 10, 11, 22, 33, 2]
'''
Search the hash table for the package objects using the package IDs.
Then, pass objects onto truck packages lists
Time Complexity: O(N)
Space Complexity: O(N)
'''
truck_one_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_one_ids]
truck_two_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_two_ids]
truck_three_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_three_ids]

''' Load distance data to a list
Time Complexity: O(1)
Space Complexity: O(N)
'''
csvreader.loadDistanceData('Distance.csv')
''' Load address data to a list
Time Complexity: O(1)
Space Complexity: O(N)
'''
csvreader.loadAddressData('Addresses.csv')

''' Convert address list to a tuple (immutable) to use as keys for address dictionary
Time Complexity: O(1)
Space Complexity: O(N)
'''
addressTuple = tuple(csvreader.addressList)

'''Create distance data dictionary with address tuple as the key and distance list as values
Time Complexity: O(N)
Space Complexity: O(N)
'''
distanceDictionary = {addressTuple[i]: csvreader.distanceList[i] for i in range(len(addressTuple))}


''' Define nearest neighbor algorithm:  given a list of packages, find the closest package distance to the current address
Time Complexity: O(N)
Space Complexity: O(N)
'''
def distance_to_address(packages_list, current_address):
    winning_distance = 10000  # purposefully a high number
    winning_package = None
    for package in packages_list:
        # using each package address, enter it as a key for the distance dictionary.
        # Returns alist of every single distance in relation to that address.
        distance_list = distanceDictionary[package.address]
        # Find the current address' index in the tuple [and dictionary]:
        distance_index = addressTuple.index(current_address)
        # Using the current address' index, find the distance from the package address
        # on the package list (in relation to current address).
        current_distance = distance_list[distance_index]

        if current_distance < winning_distance:  # If this current package distance is less than the winner distance
            winning_distance = current_distance  # This becomes the new winning distance
            winning_package = package  # This package becomes the winning package object
    return winning_package, winning_distance  # after looping through all distances,
    # return the winning package object with the winning distance


'''Define a function to pass in truck objects and deliver packages 
Time Complexity: O(N^2)
Space Complexity: O(N)
'''
def deliver_packages(truck):
    while True:
        winning_package, winning_distance = distance_to_address(truck.packages_list, truck.current_address)
        if winning_package is None:
            # If there is no winning package, break out of loop.
            break
        # Else, the mileage of the truck goes up by that amount/distance visited
        truck.mileage += winning_distance
        # Truck_address is changed to the winning package address
        truck.current_address = winning_package.address
        time_passed = (winning_distance * 60) / 18
        # Truck current_time is increased by the time_passed
        truck.current_time += datetime.timedelta(minutes=time_passed)
        # Update current "winning" package's time delivered and status
        winning_package.time_delivered = truck.current_time
        winning_package.status = "Delivered"  # Changes the status of the winning package object to delivered
        truck.packages_list.remove(winning_package)  # Removes winning package from truck_one_packages list
        csvreader.WGUPSHash.insert(winning_package.ID,
                                   winning_package)  # Updates the status and the time of the package to the hashtable
'''Initiate truck objects 
Time Complexity: O(1)
Space Complexity: O(N)
'''
truck_one = truck.Truck(1, 0.0, truck_one_packages, datetime.timedelta(hours=9, minutes=5), "HUB",
                        datetime.timedelta(hours=9, minutes=5))
truck_two = truck.Truck(2, 0.0, truck_two_packages, datetime.timedelta(hours=8, minutes=0), "HUB",
                        datetime.timedelta(hours=8, minutes=0))
truck_three = truck.Truck(3, 0.0, truck_three_packages, datetime.timedelta(hours=0, minutes=0), "HUB",
                          datetime.timedelta(hours=0, minutes=0))


'''
Function to go back to the hub and reload packages
Entering the truck's current address, returns the distance to the hub.
Time Complexity: O(1)
Space Complexity: O(N)
'''

def return_to_hub(current_address):
    hub_address = "HUB"
    # Creates a list of every single distance in relation to the hub address.
    dist_list = distanceDictionary[hub_address]
    # Find the current address' index in the tuple [and dictionary]:
    dist_index = addressTuple.index(current_address)
    # using the current address' index, finds
    # the distance from the hub address on list (in relation to current address).
    distance_to_hub = dist_list[dist_index]
    return distance_to_hub  # returns the distance from current address to hub


'''
Deliver packages for truck one and truck two
Time Complexity: O(N^2)
Space Complexity: O(N)
'''
deliver_packages(truck_one)
deliver_packages(truck_two)

'''
Return truck one to hub - driver will switch to truck 3
Use the distance_to_hub function to change truck info and bring it back to the hub.
Time Complexity: O(1)
Space Complexity: O(1)
'''
distance_to_hub = return_to_hub(truck_one.current_address)
'''
Time Complexity: O(1)
Space Complexity: O(1)
Increase truck one mileage accordingly, change truck one address to HUB, figure out the time passed

'''
truck_one.mileage += distance_to_hub
truck_one.current_address = "HUB"
time_passed = (distance_to_hub * 60) / 18
'''
Change  truck one's current time by adding the time passed.
Time Complexity: O(1)
Space Complexity: O(1)
'''
truck_one.current_time += datetime.timedelta(minutes=time_passed)
'''
Change truck three's current time and departure time to be the same time as truck one's current time
Time Complexity: O(1)
Space Complexity: O(1)
'''
truck_three.current_time = truck_one.current_time
truck_three.departure_time = truck_one.current_time

'''
Deliver truck three packages
Time Complexity: O(N^2)
Space Complexity: O(N)
'''
deliver_packages(truck_three)

'''
While loop: given a time entered by the user, return appropriate time in time delta format
Time Complexity: O(1)
Space Complexity: O(1)
'''

while True:
    user_input = input("Please enter what time you want to see package information: "
                       "HH:MM-Hours:Minutes-in 24 hour format. " +
                       "Press 'X' to exit the program")
    if user_input == 'X':
                exit()

    else:
        try:
            time_requested_string = datetime.datetime.strptime(user_input, "%H:%M")
            time_requested_delta = datetime.timedelta(hours=time_requested_string.hour,
                                                              minutes=time_requested_string.minute)
            break
        except ValueError:
            print('Time must be in appropriate format. Try again')

'''
Put packages back on their list after delivery in order to do the Command Line Interface- gets package objects
Time Complexity: O(N)
Space Complexity: O(N)
'''
truck_one_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_one_ids]
truck_two_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_two_ids]
truck_three_packages = [csvreader.WGUPSHash.search(pID) for pID in truck_three_ids]
print("Time requested: %s" % time_requested_delta)

'''
For the hashtable objects that belong to truck 1,2, and three, print the package statuses.
Time Complexity: O(N)
Space Complexity: O(N)
'''
print("Packages in Truck One:")
print("Package ID, Address, Deadline, City, Zip Code, Package Weight, Delivery Status, Time Delivered")
for package in truck_one_packages:
    print(package.print_status_for_time(time_requested_delta, truck_one.departure_time))
print("Packages in Truck Two:")
print("Package ID, Address, Deadline, City, Zip Code, Package Weight, Delivery Status, Time Delivered")
for package in truck_two_packages:
    print(package.print_status_for_time(time_requested_delta, truck_two.departure_time))
print("Packages in Truck Three:")
print("Package ID, Address, Deadline, City, Zip Code, Package Weight, Delivery Status, Time Delivered")
for package in truck_three_packages:
    print(package.print_status_for_time(time_requested_delta, truck_three.departure_time))

'''
Print all truck mileage information
Time Complexity: O(1)
Space Complexity: O(1)
'''
print("Truck one mileage: %s" % truck_one.mileage)
print("Truck two mileage: %s" % truck_two.mileage)
print("Truck three mileage: %s" % truck_three.mileage)
total_mileage = truck_one.mileage + truck_two.mileage + truck_three.mileage
print("Total mileage traveled by all trucks by the end of day: %s" % (format(total_mileage, '.2f')))
