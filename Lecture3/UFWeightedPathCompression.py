from Lecture3.UFWeighted import UFWeighted


class UFWeightedPathCompression(UFWeighted):
    def __init__(self, n):
        UFWeighted.__init__(self, n)

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]

