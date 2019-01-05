from .Engine import Engine
from Model import *


class DefaultEngine(Engine):
    def run(self):
        root = Node()
        root.situations = [i for i in range(len(self.model['situations']))]

        child = Node()
        child.pos = (1, 1)
        child.meet = 0
        child.situations = [i for i in range(len(self.model['situations']))]
        child.father = root
        root.children[4].append(child)

        return root.transform()
