'''
Add this file to the project:
Packages.csv

'''
import csv
import Package
import hash

WGUPSHash = hash.PackageHashTable()

addressList = []
distanceList = []


def loadPackageData(fileName):
    with open(fileName, newline='', encoding='utf-8-sig') as allPackages:
        packageData = csv.reader(allPackages, delimiter=',')
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pZip = package[3]
            pDeadline = package[4]
            pWeight = float(package[5])
            pStatus = "Loaded"
            pDelivered = 0

            # create a package object (using the package class)
            package = Package.Package(pID, pAddress, pCity, pZip, pDeadline, pWeight, pStatus, pDelivered)
            WGUPSHash.insert(pID, package)


def loadDistanceData(fileName):
    with open(fileName, newline='', encoding='utf-8-sig') as allDistances:
        distanceData = csv.reader(allDistances, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for distance in distanceData:
            # create a list with one row
            distanceList.append(distance)



# load addresses to a list
def loadAddressData(fileName):
    with open(fileName, newline='', encoding='utf-8-sig') as allAddresses:
        addressData = csv.reader(allAddresses, delimiter=',')
        for address in addressData:
            addressList.extend(address)
