from Lecture3.UFWeighted import UFWeighted


class UFWeightedPathHalving(UFWeighted):
    def __init__(self, n):
        UFWeighted.__init__(self, n)

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return self.parent[p]
