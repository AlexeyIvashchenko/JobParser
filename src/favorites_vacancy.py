import json
from abc import ABC, abstractmethod


class FavVac(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_to_file(self):
        pass

    @abstractmethod
    def delete_from_file(self, number):
        pass

    @abstractmethod
    def get_the_information(self):
        pass


class FavJson(FavVac):
    def __init__(self, diction):
        self.diction = {}

    def add_to_file(self):
        try:
            with open('favorites_vacancy.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(self.diction)

        with open('favorites_vacancy.json', 'w') as file:
            json.dump(data, file, indent=4, encoding='utf-8')

    def delete_from_file(self, number):
        try:
            with open('favorites_vacancy.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.remove(number)

        with open('favorites_vacancy.json', 'w') as file:
            json.dump(data, file, indent=4, encoding='utf-8')

    def get_the_information(self):
        try:
            with open('favorites_vacancy.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        print(data)
