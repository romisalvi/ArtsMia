import networkx as nx
from database import DAO


class Model:
    def __init__(self):
        self.DAO=DAO.DAO()
        self.G=nx.Graph()
        self.allObjects=self.DAO.getAllObjects()
        self.G.add_nodes_from(self.allObjects)
        self.idMap={}
        for v in self.allObjects:
            self.idMap[v.object_id]=v



    def creaGrafo(self):
        self.addEdges()
        print(self.G)
        print(self.G[self.idMap[12345]])

    def getCompConn(self,id):
        root=self.idMap[id]
        print(root)
        #modo1:successori
        successors=nx.dfs_successors(self.G,root)
        allSuccessors=[]
        for v in successors.values():
            allSuccessors.extend(v) #EXTEND!!!!

        print(f"MET1:{len(allSuccessors)}")

        #modo2: predecessori
        predecessors=nx.dfs_predecessors(self.G,root)
        print(f"MET2:{len(predecessors.values())}")

        #modo3: albero e conto i nodi
        tree = nx.dfs_tree(self.G, root)
        print(f"MET3:{len(tree.nodes)}")

        #met4:
        connComp=nx.node_connected_component(self.G,root)
        print(f"MET4:{len(connComp)}")
        return len(connComp)




    def addEdges(self):
        res=DAO.DAO.getEdges(self.idMap)
        for r in res:
            self.G.add_edge(r.o1,r.o2,peso=r.peso)


    def getNumNodes(self):
        return len(self.G.nodes)
    def getNumEdges(self):
        return len(self.G.edges)