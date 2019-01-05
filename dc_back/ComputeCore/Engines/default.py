from .Engine import Engine
from Model import *


class DefaultEngine(Engine):
    def run(self):
        root = Node()
        root.situations = [i for i in range(len(self.model['situations']))]



        return root.transform()
