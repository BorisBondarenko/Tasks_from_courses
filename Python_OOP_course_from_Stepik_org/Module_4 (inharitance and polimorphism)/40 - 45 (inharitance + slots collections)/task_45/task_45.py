from math import inf


# This is the example of program that can find shortly rout on the map between points A and B.
# I solved this mission for underground railway stations by using Floyd's method.


class Vertex:
    """This is class describes railway station.
    attr: ID - id of each station;
    attr: links - list of link-objects (connections with other stations)."""

    _ID = -1

    def __new__(cls, *args, **kwargs):
        cls._ID += 1
        return object.__new__(cls)

    def __init__(self):
        self._id = self._ID
        self._links = []

    @property
    def links(self):
        return self._links

    @property
    def id(self):
        return self._id


class Link:
    """This class describes the connections between stations.
    attr: v1 - first station in connection;
    attr: v2 - second station in connection;
    attr: dist - distance between stations (1 - default value);"""

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    def __hash__(self):
        return hash(frozenset((self.v1, self.v2)))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def get_verts(self):
        return self.v1, self.v2


class LinkedGraph:
    """This is the class that perform oll manipulations with ours Link and Vertex objects.
    In fact instance of this class create graph.
    attr: _links - all added connections;
    attr: _vertex - all added stations;
    attr: _matrix - adjacency matrix (that describes each connection between every station.)"""

    def __init__(self):
        self._links = []
        self._vertex = []
        self._matrix = []

    def add_vertex(self, v):

        if v not in self._vertex:
            self._vertex.append(v)

        max_id = max(self._vertex, key=lambda x: x.id).id
        self._matrix = [[0 if j == i else inf for j in range(max_id + 1)] for i in range(max_id + 1)]

    def add_link(self, link):

        if link not in self._links:
            self._links.append(link)

        for vert in link.get_verts():
            vert._links.append(link)
            self.add_vertex(vert)

        for link in self._links:
            idx_1, idx_2 = link.v1.id, link.v2.id
            self._matrix[idx_1][idx_2] = self._matrix[idx_2][idx_1] = link.dist

    def find_path(self, start_v, stop_v):

        def get_path(tops, end_vert, start_vert):

            end, start, chain_v, chain_l = end_vert.id, start_vert.id, [end_vert], []
            while end != start:
                end = tops[end][start]
                chain_v.extend(list(filter(lambda x: x.id == end, self._vertex)))
                a, b = [set(vert.links) for vert in chain_v[-2:]]
                chain_l.extend(list(a & b))

            return chain_v[::-1], chain_l

        N = len(self._matrix)
        tops = [[j for j in range(N)] for _ in range(N)]

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d = self._matrix[i][k] + self._matrix[k][j]
                    if self._matrix[i][j] > d:
                        self._matrix[i][j] = d
                        tops[i][j] = k

        return get_path(tops, stop_v, start_v)


class Station(Vertex):
    """This is the child-class from Vertex-class.
    In this class added attr-name (name of station),
    and was redefined magic-methods __str__ and __repr__."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    """This is the child-class from Link (basic class).
    Here I added opportunity to set the distance between stations."""

    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


# tests:

map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")
v8 = Station("Китай-город 3")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))

path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
