class UFWeighted:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            return

        if self.size[p_id] <= self.size[q_id]:
            self.parent[p_id] = q_id
            self.size[q_id] += self.size[p_id]
        else:
            self.parent[q_id] = p_id
            self.size[p_id] += self.size[q_id]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_components_count(self):
        return len([i for i in range(len(self.parent)) if i == self.parent[i]])

    def get_max_tree_height(self):
        max_height = 0
        for i in range(len(self.parent)):
            curr_height = 0

            while self.parent[i] != i:
                curr_height += 1
                i = self.parent[i]

            if curr_height > max_height:
                max_height = curr_height

        return max_height

