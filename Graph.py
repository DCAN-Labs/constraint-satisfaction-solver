from typing import List


class Graph:
    def __init__(self, v: int) -> None:
        self.v = v
        self.e: int = 0
        self.adj: List[List[int]] = []
        for i in range(v):
            self.adj.append([])

    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.e += 1

    def adj(self, v: int):
        return self.adj[v]
