from Lecture3.UFWeighted import UFWeighted
import time


class UFWeightedPathCompression(UFWeighted):
    def __init__(self, n):
        UFWeighted.__init__(self, n)

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]

if __name__ == "__main__":
    with open("/Users/ukhanoff/Downloads/mediumUF.txt") as file:
        point_count = int(file.readline())
        uf = UFWeightedPathCompression(point_count)
        counter = 0

        connections = []
        for line in file:
            p, q = map(int, line.split(sep=" "))
            connections.append((p, q))

        start = time.time()
        for p, q in connections:
            uf.union(p, q)

  #          counter += 1
   #         if counter % 100000 == 0:
    #            end = time.time()
     #           print(end - start)
      #          start = time.time()

        end = time.time()
        print(end - start)
        print(uf.get_components_count())
        print(uf.get_max_tree_height())
