from package import Package


class Location:
    """
    Location class used to manage locations imported from csv files
    """
    def __init__(self, index, location=None):
        self._index = index
        self._state = None
        self._city = None
        self._zipcode = None
        self._address = None
        self.name = None
        self.parse_location(location)
        self.hash_loc = hash(self.address)
        self.packages = []
        self._visited = False

    def __str__(self):
        return str(self._index)

    def __repr__(self):
        return self.__str__()

    def parse_location(self, unparsed_location):
        """
        O(1) Time O(1) Space
        Parses the address from the external data file
        :param unparsed_location:
        :return:
        """
        if unparsed_location is None:  # added for testing purposes when we don't have a whole address to parse
            self.name = self.index
            return
        parts = unparsed_location.split('\n')
        self.name = parts[0]
        self.address = parts[1].strip()
        if len(parts) > 2:
            self._city, temp = parts[2].split(',')
            city_state_zip = parts[2]
            self._zipcode = city_state_zip[-5:]
            city_state = city_state_zip[:-6]
            self._city, self._state = city_state.split(',')

    @property
    def index(self):
        """
        O(1) Time O(1) Space
        returns the index of the location
        :return:
        """
        return self._index

    @property
    def name(self):
        """
        O(1) Time O(1) Space
        return the name of the locations
        :return:
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        O(1) Time O(1) Space
        set the name of the location
        :param value:
        :return:
        """
        self._name = value

    @property
    def address(self):
        """
        O(1) Time O(1) Space
        return the address of the locations
        :return:
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        O(1) Time O(1) Space
        set the address of the location
        :param value:
        :return:
        """
        self._address = value

    @property
    def zipcode(self):
        """
        O(1) Time O(1) Space
        return the zipcode of the location
        :return:
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value):
        """
        O(1) Time O(1) Space
        set the zipcode of the location
        :param value:
        :return:
        """
        self._zipcode = value

    @property
    def visited(self):
        """
        O(1) Time O(1) Space
        return the visited state of the locations (NOTE: This gets reset to false when a package is loaded onto a truck)
        :return:
        """
        return self._visited

    @visited.setter
    def visited(self, value):
        """
        O(1) Time O(1) Space
        set the visited state of the location see note above
        :param value:
        :return:
        """
        self._visited = value

    def set_visited(self, time=None, truck=None):
        """
        O(n) Time O(1) Space
        sets the state of a location to visited with a time.  It checks to see if the truck the package is
        on is the same as the truck delivering the package to avoid conflicts when a location is visited multiple
        times in a day

        :param time:
        :param truck:
        :return:
        """
        if time is not None:
            for package in self.packages:

                if package.delivery_truck == truck:
                    package.status = Package.STATUS.delivered
                    package.delivery_time = str(time)

        self._visited = True
