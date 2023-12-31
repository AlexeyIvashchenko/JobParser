from abc import ABC, abstractmethod
import requests
import json


class Parser(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def to_json(self):
        pass


# класс для парсинга сайта hh.ru
class HHParser(Parser):
    def __init__(self, keyword=None):
        self.base_url = 'https://api.hh.ru/vacancies/?area=113'
        self.keyword = keyword

# получает информацию с сайта через API
    def get_info(self):
        params = {
            'text': self.keyword,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['items']
        else:
            return []

# сортирует данные по заработной плате и сохраняет в файл vacansies_from_hh.json
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


# класс для парсинга сайта Superjob.ru
class SJParser:
    def __init__(self, params=None):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key = 'v3.r.137776472.0ac84d69266fe4c87319cbcd3bf890a7a5f576e4.98cd32a7598f507f8a21258477cc81ae2e76b1a2'
        self.params = params

    # получает информацию с сайта через API
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

    # сортирует данные по заработной плате и сохраняет в файл vacansies_from_sj.json
    def to_json(self):
        with open('vacansies_from_sj.json', 'w', encoding='utf-8') as file:
            request = self.get_info()
            sorted_vacancies = sorted(request, key=lambda x: (
                x.get('payment_from', 0),
                x.get('payment_to', 0),
                x.get('currency', '') == 'rub'), reverse=True)
            json.dump(sorted_vacancies, file, indent=4, ensure_ascii=False)


# класс для парсинга обоих сайтов
class FullParser:
    def __init__(self, keyword=None):
        self.base_url_hh = 'https://api.hh.ru/vacancies/?area=113'
        self.keyword = keyword
        self.url_js = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key_js = 'v3.r.137776472.0ac84d69266fe4c87319cbcd3bf890a7a5f576e4.98cd32a7598f507f8a21258477cc81ae2e76b1a2'

# приводит данные к стандартному виду
    def get_salary(self, vacancy):
        if 'salary' in vacancy and vacancy['salary'] is not None:
            return vacancy['salary']['from'] if 'from' in vacancy['salary'] else 0
        elif 'payment_from' in vacancy:
            return vacancy['payment_from']
        return 0

    # получает информацию с сайтов через API
    def get_info(self):
        headers = {
            'X-Api-App-Id': self.api_key_js,
        }
        params = {
            'keyword': self.keyword,
        }
        response_hh = requests.get(self.base_url_hh, params=params)
        response_js = requests.get(self.url_js, headers=headers, params=params)

        data_hh = response_hh.json()
        vacancies_hh = data_hh.get('items', [])

        data_js = response_js.json()
        vacancies_js = data_js.get('objects', [])

        for vacancy in vacancies_js:
            vacancy['payment_from'] = vacancy.get('payment_from', 0)
            vacancy['currency'] = vacancy.get('currency', '')
            vacancy['requirement'] = vacancy.get('candidat', '')
            vacancy['responsibility'] = vacancy.get('vacancyRichText', '')

        all_vacancies = vacancies_hh + vacancies_js
        return all_vacancies

    # сортирует данные по заработной плате и сохраняет в файл combined_vacancies.json
    def to_json(self):
        with open('combined_vacancies.json', 'w', encoding='utf-8') as file:
            request = self.get_info()

            sorted_vacancies = sorted(request, key=lambda x: (
                self.get_salary(x),
                'RUR' in x.get('currency', '')), reverse=True)
            json.dump(sorted_vacancies, file, indent=4, ensure_ascii=False)
