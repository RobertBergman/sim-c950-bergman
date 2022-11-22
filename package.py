import enum


class Package:
    """
    Package class to manage packages for simulation
    """
    class STATUS(enum.Enum):
        at_depot = 0
        on_truck = 1
        delivered = 2
        not_arrived = 3
        unknown = 4

        def __str__(self):
            return self.name

    def __init__(self,
                 package_id=None,
                 package_mass=0,
                 package_dest_city="not set",
                 package_dest_state="not set",
                 package_expected_delivery_time="None",
                 package_dest_zipcode="not set",
                 package_dest_address="not set",
                 package_deliver_notes=None):
        self._delivery_address = package_dest_address
        self._id = int(package_id)  # package_id has to be an integer for hashtable
        self._weight = package_mass
        self._delivery_status = Package.STATUS.not_arrived
        self._dest_city = package_dest_city
        self._dest_deadline = package_expected_delivery_time
        self._dest_state = package_dest_state
        self._dest_zipcode = package_dest_zipcode
        self._delivery_notes = package_deliver_notes
        self._arrival_time = 0
        self._delivery_truck = None
        self._delivery_location = None
        self._delivery_time = None

    @property
    def id(self):
        """O(1) Time O(1) Space
        package_id has to be an integer for hashtable"""

        return int(self._id)

    @property
    def weight(self):
        """O(1) Time O(1) Space
        return the package weight"""
        return self._weight

    @property
    def status(self) -> STATUS:
        """O(1) Time O(1) Space
        return the status of a package"""
        return self._delivery_status

    @status.setter
    def status(self, value):
        """O(1) Time O(1) Space
        set the status of the package based on enum STATUS"""
        if isinstance(value, self.STATUS):
            self._delivery_status = value
        else:
            raise ValueError

    @property
    def delivery_address(self):
        """O(1) Time O(1) Space
        return the delivery address for the package"""
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        """O(1) Time O(1) Space
        set the delivery address for the package"""
        self._delivery_address = value

    @property
    def dest_city(self):
        """O(1) Time O(1) Space
        return the destination city for the package """
        return self._dest_city

    @dest_city.setter
    def dest_city(self, value):
        """O(1) Time O(1) Space
        set the destination city for the package"""

    @property
    def delivery_notes(self):
        """O(1) Time O(1) Space
        return the delivery notes for the package"""
        return self._delivery_notes

    @delivery_notes.setter
    def delivery_notes(self, value):
        """O(1) Time O(1) Space
        set the delivery notes for the package"""
        self._delivery_notes = value

    @property
    def delivery_location(self):
        """O(1) Time O(1) Space
        return the delivery location for the package"""
        return self._delivery_location

    @delivery_location.setter
    def delivery_location(self, value):
        """O(1) Time O(1) Space
        set the delivery location for the package"""
        self._delivery_location = value

    @property
    def delivery_truck(self):
        """O(1) Time O(1) Space
        return the delivery truck the package used"""
        return self._delivery_truck

    @delivery_truck.setter
    def delivery_truck(self, value):
        """O(1) Time O(1) Space
        set the delivery truck the package used"""
        self._delivery_truck = value

    @property
    def dest_zipcode(self):
        """O(1) Time O(1) Space
        return Destination Zipcode"""
        return self._dest_zipcode

    @property
    def arrival_time(self):
        """O(1) Time O(1) Space
        Return the Time the package shows up at the depot in seconds after 8:00AM"""
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        """O(1) Time O(1) Space
        Set the Time the package shows up at the depot in seconds after 8:00AM"""
        self._arrival_time = value

    @property
    def delivery_time(self):
        """O(1) Time O(1) Space
        Return the time the package was delivered or None of not delivered"""
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        """O(1) Time O(1)
        Space set the time the package was delivered or None if not delivered"""
        self._delivery_time = value

    @property
    def deadline(self):
        """O(1) Time O(1) Space When the package should arrive by"""
        if self._dest_deadline == "EOD":
            return "EOD"
        if "10:30" in self._dest_deadline:
            return "10:30AM"
        if "9:00" in self._dest_deadline:
            return "9:00AM"
        raise ValueError(f"Didn't expect {self._dest_deadline}")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.delivery_truck is None:
            truck = "None"
        else:
            truck = self.delivery_truck.truck_info['name']
        return f"Package ID: {self.id} Destination Address: {self.delivery_address}, Weight: {str(self.weight)}, Truck: {truck}, Status: {self.status}, Deadline: {self.deadline} Delivered: {self.delivery_time} "
