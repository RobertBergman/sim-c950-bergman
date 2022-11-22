from pathlib import Path
from location import Location
from hashtable import HashTable
from package import Package
import os

import csv


def import_packages(locations):

    package_file = os.getcwd() / Path("data/") / "WGUPS Package File.csv"


    header = 0
    packages = HashTable()
    with open(package_file, newline='') as csvfile:
        package_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(package_reader)
        for row in package_reader:

            package_id = row[0]
            package_dest_address = row[1]
            package_dest_city = row[2]
            package_dest_state = row[3]
            package_dest_zipcode = row[4]
            package_expected_delivery_time = row[5]
            package_mass = int(row[6])
            package_deliver_notes = row[7]
            package = Package(
                package_id=int(package_id),
                package_mass=package_mass,
                package_dest_city=package_dest_city,
                package_dest_state=package_dest_state,
                package_expected_delivery_time=package_expected_delivery_time,
                package_dest_zipcode=package_dest_zipcode,
                package_dest_address=package_dest_address,
                package_deliver_notes=package_deliver_notes

            )
            package.status = Package.STATUS.not_arrived
            package.arrival_time = 0 if "will not arrive" not in package.delivery_notes else 65
            for location in locations:
                if package.delivery_address == location.address:
                    location.packages.append(package)
                    package.delivery_location = location
            packages[int(package_id)] = package

    return packages


def get_locations():
    data_folder = Path("data/")
    package_file = os.getcwd() / Path("data/") / "WGUPS Package File.csv"
    distance_file = os.getcwd() / Path("data/") / "WGUPS Distance Table.csv"
    locations = []
    with open(distance_file, newline='') as csvfile:

        distance_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        row_count = 0

        for row in distance_reader:
            # first row is a list of locations
            row_count += 1
            if row_count == 1:
                column_count = 0
                for location in row:
                    column_count += 1
                    # the first two columns are not locations and should be skipped
                    if column_count > 2:
                        locations.append(Location(column_count - 2, location))
    return locations


def get_matrix():

    package_file = os.getcwd() / Path("data/") / "WGUPS Package File.csv"
    distance_file = os.getcwd() / Path("data/")/ "WGUPS Distance Table.csv"
    distance_table = []
    locations = []
    with open(distance_file, newline='') as csvfile:

        distance_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        row_count = 0

        for row in distance_reader:
            # first row is a list of locatio0ns
            row_count += 1
            if row_count == 1:
                pass

            else:


                string_distances = row[2:]

                float_distances = list(map(lambda d: float(d) if len(d) > 0 else 0.0, string_distances))
                distance_table.append(float_distances)

                # first column is location
                # second column is zipcode
                # third column is distance from location[

    # set the opposite direction distances
    # O(n^2)
    for x in range(0, len(distance_table)):
        for y in range(0, len(distance_table[0])):
            if x != y:
                if distance_table[x][y] == 0.0:
                    distance_table[x][y] = distance_table[y][x]
    return distance_table