from abc import ABC, abstractmethod
import json


class Parser(ABC):
    @abstractmethod
    def parse(self, data):
        pass
