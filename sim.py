import sys
from clock import Clock
from environment import Environment

from truck import Truck
from package import Package

from datetime import time
from search import search


class Simulate:
    ERROR = "\nCommand not recognized!!!!\n"

    def __init__(self):

        self.sim_time = time(8, 0, 0)
        self._command = None
        self.env = None
        self.menu_main_txt = """

Delivery Simulation Menu
-------------------------------------------
    status - package status menu
    end - terminate the simulation    
"""

        self.menu_status_txt = """

Package Status Menu
-------------------
    Package lookup - select a component to lookup a package

    Current SimTime = {}

    M. Total truck miles - set sim time to 17:00:00 to see final tally
    T. Set the sim time
    A. status of all packages
    1. Package ID
    2. delivery address
    3. deliver deadline
    4. delivery city
    5. delivery zip code
    6. package weight
    7. delivery status
    X. Exit to main menu


"""

        self.menu_load_txt = """

Load Menu
----------------------
    1. Load 3 trucks with the predefined loads and departure time
    0. Return to main menu
"""

    def start(self):
        """
        O(1) Time O(n) Space

        starts the simulation menu

        :return:
        """
        command = None
        menu = self.menu_main_txt
        while True:
            print(menu)

            command = input("Enter a command:")

            if command == "status":
                self.menu_package_status()
                continue

            if command == "end" or command == "exit":
                sys.exit()
            else:
                print(self.ERROR)

    def print_search_results(self, results):
        """
        O(n) time O(n) space

        prints the search results of the packages in order of package id
        :param results:
        :return:
        """
        packages = [self.env.packages[key] for key in results]
        for package in sorted(packages, key=id):
            print(package)

    def menu_package_status(self):
        """
        O(1) time O(1) space

        Displays Status menu and accepts a command to perform until exited to the previous menu

        :return:
        """
        self.env = self.sim()
        while True:
            print(self.menu_status_txt.format(self.sim_time))
            command = input("Select an option and hit enter: ")

            if command.lower() == 'm':
                total = 0
                for truck in self.env.trucks:

                    for i, path in enumerate(truck.paths):
                        print(f"Truck {truck.truck_info['name']} path {i} = {path.total_distance}")
                        total += path.total_distance
                print(f"Total mileage for all trucks and paths: {total}")
                continue

            if command.lower() == 't':
                try:
                    self.sim_time = time.fromisoformat(
                        input("Enter a time in 24 Hour ISO format (09:30:00) : "))  # No error checking
                    self.env = self.sim()
                except:
                    print("Setting Sim Time failed")
                continue

            if command == '1':
                search_term = input("Enter search ID: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '2':
                search_term = input("Enter search address: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '3':
                search_term = input("Enter search deadline: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '4':
                search_term = input("Enter search city: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '5':
                search_term = input("Enter search zip code: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '6':
                search_term = input("Enter search weight: ")
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue
            if command == '7':
                search_term = input(
                    "Enter search delivery status ('not_arrived', 'at_depot', 'on_truck', 'delivered': ")
                if search_term not in ['at_deport', 'on_truck', 'delivered']:
                    print(f"No packages have a status of {search_term}")
                    continue
                results = search(command, search_term, self.env)
                self.print_search_results(results)
                continue

            if command.lower() == 'a':
                print(self.env.clock.clock_time)
                print(self.env.packages)

                continue
            if command.lower() == 'x':
                return

            else:
                print(self.ERROR)

    def menu_load(self):
        """
        O(1) time O(1) space

        Displays main menu with option to view status or exit the program
        :return:
        """
        while True:
            print(self.menu_load_txt)
            option = input("Select an option and hit enter: ")

            if option == '1':
                self.loading_default()
                return
            if option == '0':
                return
            else:
                print(self.ERROR)

    def sim(self):
        """
        O(n) Time O(n) Space

        Simulates the system by starting a clock at 8:00AM and incrementing seconds by 1 for each iteration of the
        simulation until the simulation end time has been reached.  The env is returned to allow for query of
        objects at the desired time

        :return: Environment
        """
        env = Environment(Clock())
        env.debug = True
        env.trucks = [Truck(env, str(i)) for i in range(1, 4)]

        # package list to load in trucks as needed
        package_list1 = [13, 14, 15, 37, 16, 34, 19, 20, 21, 39, 7, 29, 32, 31]
        package_list2 = [6, 1, 25, 26, 5, 3, 18, 4, 40, 8, 30]
        package_list3 = [28, 2, 33, 35, 27]
        package_list4 = [10, 11, 36, 38, 12, 17]
        package_list5 = [22, 23, 24, 9]

        # initial state requires that all packages that are not delays get status set to at_depot
        for key in env.packages.keys:
            package = env.packages[key]
            if package.status == Package.STATUS.not_arrived and package.arrival_time == 0:
                env.depot.packages.append(package)
                package.status = Package.STATUS.at_depot

        # main loop for simulation
        while env.clock.clock_time <= self.sim_time:

            # trucks 1 and 2 are loaded with packages
            if env.clock.time == 0:
                env.depot.set_visited()
                env.trucks[0].load_truck(package_list1)
                env.trucks[1].load_truck(package_list2)

            # when packages show up at the depot as know by the arrival_time, change status to at_depot
            if env.clock.time > 0:  # after initial start time, wait for packages to show up at the depot
                for key in env.packages.keys:
                    package = env.packages[key]
                    if env.clock.time == package.arrival_time:
                        package.status = package.STATUS.at_depot
                        if env.debug:
                            print(f"Package {package.id} has arrived at the depot")

            # at 10:20AM package 9 get its address updated to the correct delivery location
            if env.clock.clock_time == time(10, 20, 0):  # Change the delivery address on package 9
                package = env.packages[9]
                package.delivery_address = "410 S State St"
                package_location = package.delivery_location

                packages_for_location = []
                for p in package.delivery_location.packages:
                    if p is not package:
                        packages_for_location.append(package)
                package_location.packages = packages_for_location
                new_location = None
                for location in env.locations:
                    if location.address == package.delivery_address:
                        package.delivery_location = location
                        location.packages.append(package)

            # at 11:00AM both the trucks have already returned and a loaded with more packages to be delivered
            if env.clock.clock_time == time(11, 00, 0):
                env.trucks[0].load_truck(package_list3)
                env.trucks[1].load_truck(package_list4)

            # at 1:30PM the final load is put on truck 2
            if env.clock.clock_time == time(13, 30, 0):
                env.trucks[1].load_truck(package_list5)

            # every second the trucks are checked for deliveries
            for truck in env.trucks:
                truck.check_deliveries()

            # when the sim_time has been reached return the environment to be analyzed
            if self.sim_time == env.clock.clock_time:
                return env

            # advance the clock 1 second
            env.clock.advance()
