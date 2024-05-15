from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._edges = None
        self._nodes = None
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, threshold):
        self._grafo.clear()
        self._nodes = DAO.getAllAirports()
        self.fillIDMap()
        self._grafo.add_nodes_from(self._nodes)
        self._edges = DAO.getAllRotteV2()

        for edge in self._edges:
            w = edge.avgDistance
            a1Object = self._idMap[edge.a1]
            a2Object = self._idMap[edge.a2]
            if w > threshold:
                self._grafo.add_edge(a1Object, a2Object, weight= w)
                print("added edge", edge)

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getAllEdges(self):
        return self._grafo.edges

    def fillIDMap(self):
        for n in self._nodes:
            self._idMap[n.ID] = n

    def getAvgDist(self, v1, v2):
        data =  self._grafo.get_edge_data(v1, v2)
        return data["weight"]