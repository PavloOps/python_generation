import json


def task1():
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

    result = json.dumps(countries, separators=(',', ' - '), indent=3, sort_keys=True)
    return result


def task2():
    words = {
             frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
             "travel": "trævl",
             ("hello", "world"): ("həˈləʊ", "wɜːld"),
             "moonlight": "muːn.laɪt",
             "sunshine": "ˈsʌn.ʃaɪn",
             ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
             "adventure": "ədˈventʃər",
             "beautiful": "ˈbjuːtɪfl",
             frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
             "bicycle": "baisikl",
             ("pilot", "fly"): ("pailət", "flai")
            }
    data_json = json.dumps(words, ensure_ascii=False, skipkeys=True)
    return data_json


def task3():
    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump([club1, club2, club3], json_file, indent=3)

    with open("data.json", encoding="utf-8") as json_file:
        print(json.load(json_file))


def task4():
    specs = {
             'Модель': 'AMD Ryzen 5 5600G',
             'Год релиза': 2021,
             'Сокет': 'AM4',
             'Техпроцесс': '7 нм',
             'Ядро': 'Cezanne',
             'Объем кэша L2': '3 МБ',
             'Объем кэша L3': '16 МБ',
             'Базовая частота': '3900 МГц'
            }

    specs_json = json.dumps(specs, indent=3, ensure_ascii=False)
    return specs_json


def is_correct_json(string: str) -> bool:
    try:
        res = json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


def task6():
    json_string = """{
     "type": "donut", 
     "name": "Cake", 
     "tastes": ["chocolate", "cream", "strawberry"]
    }"""
    for key, value in json.loads(json_string).items():
        if isinstance(value, list):
            print(f"{key}:", end=' ')
            print(*value, sep=', ', end='\n')
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    print(task1())
    print(task2())
    print(task3())
    print(task4())
    print(is_correct_json('number = 17'))
    print(task6())
