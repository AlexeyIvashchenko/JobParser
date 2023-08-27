from abc import ABC, abstractmethod
import requests
import json
import os


class Parser(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def to_json(self):
        pass


class HHParser(Parser):
    def __init__(self, keyword=None):
        self.base_url = 'https://api.hh.ru/vacancies/?area=113'
        self.keyword = keyword

    def get_info(self):
        """Получает информацию о вакансиях по API"""
        params = {
            'text': self.keyword,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['items']
        else:
            return []

    def to_json(self):
        with open('vacansies_from_hh.json', 'w', encoding='utf-8') as file:
            request = self.get_info()
            sorted_vacancies = sorted(request, key=lambda x: (
                x['salary']['from'] if x.get('salary') and 'from' in x['salary'] and x['salary'][
                    'from'] is not None else 0,
                x['salary']['to'] if x.get('salary') and 'to' in x['salary'] and x['salary']['to'] is not None else 0,
                x['salary']['currency'] if x.get('salary') and 'currency' in x['salary'] else '',),
                                      reverse=True)
            json.dump(sorted_vacancies, file, indent=4, ensure_ascii=False)


class SJParser:
    def __init__(self, params=None):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key = 'v3.r.137776472.0ac84d69266fe4c87319cbcd3bf890a7a5f576e4.98cd32a7598f507f8a21258477cc81ae2e76b1a2'
        self.params = params

    def get_info(self):
        headers = {
            'X-Api-App-Id': self.api_key,
        }
        params = {
            'keyword': self.params,
        }

        response = requests.get(self.url, headers=headers, params=params)
        data = response.json()
        vacancies = data.get('objects', [])
        return vacancies

    def to_json(self):
        with open('vacansies_from_sj.json', 'w', encoding='utf-8') as file:
            request = self.get_info()
            sorted_vacancies = sorted(request, key=lambda x: (
                x.get('payment_from', 0),
                x.get('payment_to', 0),
                x.get('currency', '') == 'rub'), reverse=True)
            json.dump(sorted_vacancies, file, indent=4, ensure_ascii=False)
