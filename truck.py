from path import Path
from package import Package


class Truck:

    def __init__(self, env, name):
        self.distance_travelled_at_last_top = 0.0
        self.env = env
        self.truck_info = {'name': name}

        # Have a need to keep track of more than one path for each circuit adding paths array.
        self.paths = []
        self.path = Path(self.env)
        self._start_time = 0
        self.stop = False

    def load_truck(self, packages):
        """
        O(n) Time O(n) space
        load truck with packages and optimize the route based on locations needed to visit to deliver all the packages

        """
        for load_package in packages:

            ref_package = self.env.packages[load_package]

            if self.env.debug:
                print(f"Truck: {self.truck_info['name']} - Loading package {ref_package.id} at {self.env.clock}")
            if ref_package.delivery_location not in self.path.path:
                self.path.add(ref_package.delivery_location)
                ref_package.delivery_location.visited = False
            ref_package.status = Package.STATUS.on_truck
            ref_package.delivery_truck = self
        self.path.optimize_path()
        self.path.start_time = self.env.clock.clock_time

    def prioritize_path(self):
        """O(n) Time O(n) Space
        We don't use this function, but it was intended to move the locations to the front of the path
        based on their priority this would need a better implementation that should be accounted for in
        the optimization function to take priority into account and weight priority with path distance
        """
        high_priority_stops = []
        medium_priority_stops = []
        the_rest = []
        last = []
        for location in self.path.path:
            for p in location.packages:
                if p.deadline is None:
                    if location not in high_priority_stops + medium_priority_stops + the_rest + last:
                        the_rest.append(location)

                elif p.deadline == "9:00AM":
                    if location not in high_priority_stops + medium_priority_stops + the_rest + last:
                        high_priority_stops.append(location)

                elif p.deadline == "10:30AM":
                    if location not in high_priority_stops + medium_priority_stops + the_rest + last:
                        medium_priority_stops.append(location)

                elif p.id == 9:
                    if location not in high_priority_stops + medium_priority_stops + the_rest + last:
                        last.append(location)

                else:
                    if location not in high_priority_stops + medium_priority_stops + the_rest + last:
                        the_rest.append(location)
        self.path.path = high_priority_stops + medium_priority_stops + the_rest + last

    @property
    def start_time(self):
        """
        O(1) Time O(1) Space

        Returns the start_time of the truck
        :return:
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        O(1) Time O(1) Space
        set the start_time of the truck
        :param value:
        :return:
        """
        self._start_time = value

    @property
    def path_time(self):
        """
        O(1) Time O(1) Space
        :return:
        """
        pd = self.distance_travelled
        return (pd * (60 / 18) * 60) + self._start_time

    @property
    def distance_travelled(self):
        """
        O(1) Time O(1) Space
        :return:
        """
        if self._start_time <= self.env.clock.time:
            return ((self.env.clock.time - self._start_time) * 18 / 60)/60
        else:
            return 0.0

    # def deliver_package(self, package):
    #
    #     print(f"Delivering package {package.id} at {self.env.clock.time}.")
    #     package.truck = None
    #     package.status = package.STATUS.delivered
    #     package.delivered_time = int(str(self.env.clock.time))

    def check_deliveries(self):
        """
        O(1) Time O(1) Space
        :return:
        """
        if self.path.next_stop is None:
            return False

        last_stop_in_path = self.path.path[-1]
        if self.path.next_stop == last_stop_in_path:
            # Is the truck at the depot?
            if self.distance_travelled > self.path.total_distance:
                self.distance_travelled_at_last_top = self.distance_travelled + self.path.distance_to_next_stop

                self.paths.append(self.path)
                self.path = Path(self.env)
                self.stop = True
            return False

        # if self.path.next_stop == self.path.prev_stop:
        #     return False
        if self.distance_travelled > (self.path.distance_to_next_stop + self.distance_travelled_at_last_top):

            self.path.next_stop.set_visited(str(self.env.clock), self)
            self.distance_travelled_at_last_top = self.distance_travelled
