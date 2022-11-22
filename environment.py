from util import get_matrix, import_packages, get_locations


class Environment:
    """
    class Environment holds the data imported from the external documents

    Package HashTable
    location array
    trucks array
    distance 2d array

    """
    def __init__(self, clock):
        self.clock = clock
        self.depot = None

        self.locations = get_locations()
        self.trucks = []
        self.package_list1 = [13, 14, 15, 16, 19, 20]
        self.package_list2 = [3, 18, 36, 38]
        self.package_list3 = [6, 25, 28, 32, 9]


        # self.matrix = [
        #     # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        #     [0, 2, 4, 3, 8],  # 1
        #     [2, 0, 6, 2, 3],  # 2
        #     [4, 6, 0, 3, 2],  # 3
        #     [3, 2, 3, 0, 5],  # 4
        #     [8, 3, 2, 5, 0]   # 5
        # ]
        self.matrix = get_matrix()

        self.depot = self.locations[0]
        self.packages = import_packages(self.locations)


