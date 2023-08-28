import json
from abc import ABC, abstractmethod


class FavVac(ABC):

    @abstractmethod
    def add_to_file(self, diction):
        pass

    @abstractmethod
    def delete_from_file(self, number):
        pass


class FavJson(FavVac):

    def add_to_file(self, diction):
        try:
            with open('favorites_vacancy.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(diction)

        with open('favorites_vacancy.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_from_file(self, number):
        try:
            with open('favorites_vacancy.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.remove(number)

        with open('favorites_vacancy.json', 'w') as file:
            json.dump(data, file, indent=4, encoding='utf-8')
