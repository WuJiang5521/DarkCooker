from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def run(self):
        pass
