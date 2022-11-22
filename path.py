from algs.bruteforce_dp import BF_DP

class Path:
    """
    class Path holds the path the trucks are using to deliver packages at the locations
    """
    def __init__(self, env):
        self._path = []
        self.start_time = int()
        self.env = env

    def add(self, location):
        """
        O(1) Time O(1) Space

        add a location to the path
        :param location:
        :return:
        """
        self._path.append(location)

    @property
    def current_distance(self):
        """
        O(1) Time O(1) Space

        return the current distance the truck has travelled assuming the truck has been moving continuously since
        8:00AM  of course this isn't true,  so I don't think this function is getting used.
        :return:
        """
        return self.env.clock.time * 18/360

    @property
    def next_stop(self):
        """
        O(n) Time O(1) Space
        checks is location in path if it has been visited and returns the first path that has not

        :return:
        """
        for location in self._path[1::]:
            if not location.visited and location is not self.env.depot:
                return location
            elif location is self._path[-1]:
                return location


    @property
    def prev_stop(self):
        """
        O(n) Time O(1) Space

        returns the location from the path that was visited
        :return:
        """
        prev_stop = self.env.depot
        for location in self._path:
            if location.visited:
                prev_stop = location
        return prev_stop

    @property
    def distance_to_next_stop(self):
        """
        O(1) Time O(1) Space
        returns the distance between the prev stop and the next stop using a lookup in the distance matrix
        :return:
        """
        u = self.prev_stop.index
        if self.next_stop is None:
            v = self.env.depot.index
        else:
            v = self.next_stop.index
        return self.env.matrix[u - 1][v - 1]

    @property
    def path(self):
        """
        O(1) Time O(1) Space
        returns the path
        :return:
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        O(1) Time O(1) Space

        sets the path.  used in the case where we want to externally modify the path.  like by the truck priority
        function that moves locations around by priority.  We didn't use that function though so this likely
        doesn't get called as part of this simulation
        :param value:
        :return:
        """
        self._path = value

    @property
    def total_distance(self) -> float:
        """
        O(n) Time O(1) Space
        returns the sum of the distances for each segment in the path
        :return:
        """
        total = 0
        count = 0
        while count < len(self._path) - 1:
            u = self._path[count]
            v = self._path[count + 1]

            total += self.env.matrix[u.index - 1][v.index - 1]
            count += 1
        return total

    def optimize_path(self):
        """
        O(2^n) Time O(n^2) Space
        optimize path using brute force traveling salesman algorithm
        checks every path and returns a hamilton cycle including all locations starting and ending at the depot
        :return:
        """
        # print(self._path)
        # p = NN(self._path, self.env)

        p = BF_DP(self._path, self.env)

        # p = random_best_path(self._path, self.env)

        self._path = p.path()
