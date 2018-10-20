class UFQuickFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, p):
        return self.parent[p]

    def union(self, p, q):
        parent_p = self.parent[p]
        parent_q = self.parent[q]

        if parent_p == parent_q:    # points are already in one component
            return

        for index in range(self.n):
            if self.parent[index] == parent_q:
                self.parent[index] = parent_p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_components_count(self):
        return len([i for i in range(len(self.parent)) if i == self.parent[i]])

