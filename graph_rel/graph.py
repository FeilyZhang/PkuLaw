import random
import networkx as nx
import matplotlib.pyplot as plt

class graph:

    __dg = None

    def __init__(self):
        #self.__dg = nx.DiGraph()
        self.__dg = nx.Graph()

    def add_nodes(self, nodes):
        for i in range(0, len(nodes)):
            self.__dg.add_node(nodes[i])

    def add_edges(self, edges):
        for edge in edges:
            for ele in edge['rel']:
                self.__dg.add_edge(edge['word'], ele['to'])

    def drawAndShow(self, size):
        nx.draw(self.__dg, with_labels=True, node_size = size, node_color = self.randomcolor(size), edge_color = self.randomcolor(size))
        plt.rcParams['font.sans-serif'] = ['simsun']
        plt.show()

    def drawAndShow1(self):
        nx.draw(self.__dg, with_labels=True)
        plt.rcParams['font.sans-serif'] = ['simsun']
        plt.show()

    def randomcolor(self, size):
        rst = []
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for ele in size:
            color = ""
            for i in range(6):
                color += colorArr[random.randint(0, 14)]
            rst.append('#' + color)
        return rst
