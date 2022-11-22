import sys
import copy

from clock import Clock
from environment import Environment

from util import get_matrix
"""
for test purposes
matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
data = [1, 2, 3, 4]
"""


class BF_DP:
    """A Brute-force-best-path solution using dynamic programming"""

    def __init__(self, to_visit, env):

        self.matrix = get_matrix()

        self.to_visit = to_visit
        self.n = len(env.locations)
        self.env = env
        self.all_sets = []
        self.g = {}
        self.p = []
        self._to_visit = ()

    @property
    def to_visit(self):
        """
        O(1) Time O(1) Space
        returns the array with the locations to be visited
        :return:
        """
        return self._data

    @to_visit.setter
    def to_visit(self, location):
        """
        O(n) Time O(n) Space
        sets the locations to be visited using the location index
        :param location:
        :return:
        """
        self._data = tuple(list(map(lambda x: x.index, location)))

    def path(self):
        """
        O(2^n) Time and O(2^n) Space  - NP Hard Problem

        Not scalable - better algorithm would be minimum shortest path tree for scalability after 16 locations time
        to solve is too high for practicle use

        returns the optimal path using a recursive function to explore every potential path to the end
        and then finds the least cost path as the recursive function rolls out

        :return:
        """
        for x in range(1, self.n):
            self.g[x + 1, ()] = self.matrix[x][0]

        # recursive function that find the minimum path of from the tree root set as 1 here
        self.get_minimum(1, self._data)  # add locations to be visited on this path
        final_path = []

        solution = self.p.pop()

        final_path.append(solution[1][0])
        for x in range(self.n - 2):
            for new_solution in self.p:
                if tuple(solution[1]) == new_solution[0]:
                    solution = new_solution

                    final_path.append(solution[1][0])
                    break

        location_path = [self.env.locations[i-1] for i in final_path]
        return [self.env.depot]+location_path+[self.env.depot]

    def get_minimum(self, i, S):
        """
        O(2^n) Time O(2^n) Space

        get the minimum path from all_min

        :param i:
        :param S:
        :return:
        """
        if (i, S) in self.g:  #memoization
            # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
            return self.g[i, S]

        values = []
        all_min = []
        for j in S:
            set_S = copy.deepcopy(list(S))
            set_S.remove(j)
            all_min.append([j, tuple(set_S)])
            result = self.get_minimum(j, tuple(set_S))
            values.append(self.matrix[i - 1][j - 1] + result)

        # get minimum value from set as optimal solution for
        self.g[i, S] = min(values)
        self.p.append(((i, S), all_min[values.index(self.g[i, S])]))

        return self.g[i, S]


if __name__ == '__main__':
    clock = Clock()
    env = Environment(clock)
    to_visit = [
        env.locations[4],
        env.locations[5],
        env.locations[8],
        env.locations[2],
        env.locations[6],
        env.locations[11],
        env.locations[23],
        env.locations[21],
        env.locations[7],
    ]
    tsp = BF_DP(to_visit, env)

    tsp.to_visit = to_visit
    path = tsp.path()
    print(path)
    sys.exit(0)
