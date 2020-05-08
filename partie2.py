from partie1 import *

class BinaryTree:
    def __init__(self,root):
        self.__root = root

    def getroot(self):
        return self.__root

    def isRoot(self,node):
        if node == self.__root:
            return True
        else:
            return False

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getleft()) + 1 + self.size(node.getright())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getleft()) + self.printValues(node.getright()) + " " + str(node.getval())

    def sumValues(self,node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getleft()) + self.sumValues(node.getright())  + node.getval()

    def numberLeaves(self,node):
        if node is None:
            return 0
        if node.getright() == None and node.getleft() == None:
            return 1
        else:
            return self.numberLeaves(node.getleft()) + self.numberLeaves(node.getright())

    def numberInternalNodes(self,node):
        if node is None:
            return 0
        if node.getright() == None  and node.getleft() == None :
            return 0
        else:
            return 1 + self.numberInternalNodes(node.getleft()) + self.numberInternalNodes(node.getright())

    def height(self, node):
        if node is None:
            return -1
        else:
            leftHeight = self.height(node.getleft())
            rightHeight = self.height(node.getright())
            return max(leftHeight, rightHeight) + 1

    def belongs(self,node,val):
        if node is None:
            return False
        if node.getval() == val:
            return True
        else:
            if self.belongs(node.getleft(),val) == True or self.belongs(node.getright(),val)== True:
                return True
            else:
                return False

    #def ancestors(self,node,val):

NGGG = Node(3, None, None)
NGG = Node(4, None, NGGG)
NGD = Node(6, None, None)
NG = Node(5, NGD, NGG)

NDDG = Node(18, None, None)
NDDD = Node(21, None, None)
NDD = Node(19, NDDD, NDDG)
ND = Node(17, NDD, None)

nodeRoot = Node(12, ND, NG)

Root = BinaryTree(nodeRoot)
print("La racine est bonne?",Root.isRoot(nodeRoot))
print("La taille de l'arbre:",Root.size(nodeRoot))
print("Affichage de toutes les valeurs des noeuds:",Root.printValues(nodeRoot))
print("Somme de tous les noeuds:",Root.sumValues(nodeRoot))
print("Nombre des feuilles de l'arbre:",Root.numberLeaves(nodeRoot))
print("Nombre de noeuds internes de l'arbre:",Root.numberInternalNodes(nodeRoot))
print("Hauteur de l'arbre:",Root.height(nodeRoot))
valeur = 21
print("Est ce que",valeur, "est un noeud de l'arbre?",Root.belongs(nodeRoot,valeur))
