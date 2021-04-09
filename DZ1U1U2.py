# Konstantin Filippov 09.04.2021
#
# 1. Посмотреть документацию к API GitHub, разобраться как вывести
# список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json; написать функцию,
# возвращающую список репозиториев.

import requests
import json
from pprint import pprint

# https://docs.github.com/en/rest/reference/repos#list-organization-repositories

# curl \
#   -H "Accept: application/vnd.github.v3+json" \
#   https://api.github.com/orgs/ORG/repos

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    , "Accept": "application/vnd.github.v3+json"

}

def f_write_git_data(org):
    url = f"https://api.github.com/orgs/{org}/repos"

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        path = f"{org}.json"
        with open(path, "w") as f:
            json.dump(r.json(), f, indent=2)
        print("File written:", f.name)
        return r.json()
    else:
        print("Status code: ", r.status_code)
        return None


def f_solution_1_1():
    print("Lesson 1. Excercise 1.")
    G_ORG = input("Company name: ") # e.g. Microsoft
    pprint(f_write_git_data(G_ORG))
    print()

# 2. Зарегистрироваться на https://openweathermap.org/api и написать функцию,
# которая получает погоду в данный момент для города,
# название которого получается через input.
# https://openweathermap.org/current

def f_get_weather(city_name, API_key):
    return requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}", headers=headers)

def f_solution_1_2():
    print("Lesson 1. Excercise 2.")
    city_name = "London"
    API_key = input("API key for api.OpenWeather.org:") # e.g. 91dd1ee97ece1899321bb6c356ff637a
    pprint(f_get_weather(city_name, API_key).text)
    print()

# 1
f_solution_1_1()

# 2
f_solution_1_2()


