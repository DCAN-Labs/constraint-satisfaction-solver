from typing import List

from Graph import Graph


class CC:
    def __init__(self, g: Graph):
        self.marked: List[bool] = [False] * g.v
        self.count: int = 0
        self.id: List[int] = [0] * g.v
        for s in range(g.v):
            if not self.marked[s]:
                self.dfs(g, s)
                self.count += 1

    def dfs(self, g: Graph, v: int) -> None:
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)

    def connected(self, v: int, w: int):
        return self.id[v] == self.id[w]

    def id(self, v: int) -> int:
        return self.id[v]
