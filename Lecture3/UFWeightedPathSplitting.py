from Lecture3.UFWeighted import UFWeighted


class UFWeightedPathSplitting(UFWeighted):
    def __init__(self, n):
        UFWeighted.__init__(self, n)

    def find(self, p):
        while p != self.parent[p]:
            nxt = self.parent[p]
            self.parent[p] = self.parent[self.parent[p]]
            p = nxt

        return self.parent[p]

