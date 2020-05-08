class Node:
    def __init__(self,val,right = None,left = None):
        self.__val = val
        self.__right = right
        self.__left = left

    def getval(self):
        return self.__val

    def getright(self):
        return self.__right

    def getleft(self):
        return self.__left

    def setval(self,val):
        self.__val=val

    def setright(self,right):
        self.__right = right

    def setleft(self,left):
        self.__left = left

    def __str__(self):
        return "Donnée du noeud :"+str(self.__val)+", fils droit :"+str(self.__right)+", fils gauche :"+str(self.__left)


#N1 = Node(17,7,9)
#print(N1)
