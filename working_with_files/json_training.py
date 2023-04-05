import json
import csv
from datetime import datetime


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


def task7():
    actions = {
        str: lambda x: f"{x}!",
        int: lambda x: x + 1,
        bool: lambda x: not x,
        list: lambda x: x * 2,
        dict: lambda x: {**x, **{"newkey": None}}
    }

    with open("data7.json", encoding="utf-8") as input_file, \
            open("updated_data.json", "w", encoding="utf-8") as output_file:
        data = json.load(input_file)
        res = [actions[type(x)](x) for x in data if x is not None]
        json.dump(res, output_file, indent=3)


def task8():
    with open("data1_8.json", encoding="utf-8") as json_input1, \
            open("data2_8.json", encoding="utf-8") as json_input2, \
            open("data_merge.json", "w", encoding="utf-8") as json_output:
        json1, json2 = json.load(json_input1), json.load(json_input2)

        result = {
            key: json2.get(key)
            if json2.get(key) else json1.get(key)
            for key in set(json1.keys() | json2.keys())}

        json.dump(result, json_output, indent=3, sort_keys=True)


def task9():
    with open("people.json", encoding="utf-8") as input_file, \
            open("updated_people.json", "w", encoding="utf-8") as output_file:
        data = json.load(input_file)
        common_keys = set()

        for json_object in data:
            for key in json_object.keys():
                common_keys.add(key)
        else:
            dict_to_join = dict.fromkeys(common_keys)

        for json_object in data:
            for key in common_keys:
                json_object.setdefault(key, None)

        json.dump(data, output_file, indent=3)

        # with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
        #     people = json.load(fi)
        #     d = {k: None for i in people for k in i.keys()}
        #     json.dump([d | i for i in people], fo)


def task10():
    with open("countries.json", encoding="utf-8") as input_file, \
            open("religion.json", "w", encoding="utf-8") as output_file:
        data, result = json.load(input_file), {}

        for d in data:
            result.setdefault(d["religion"], []).append(d.get("country"))

        json.dump(result, output_file, indent=3)


def task11():
    with open("playgrounds.csv", encoding="utf-8") as input_file, \
            open("addresses.json", "w", encoding="utf-8") as output_file:
        data = csv.DictReader(input_file, delimiter=";")
        result = {}

        for curr_dict in data:
            result.setdefault(curr_dict["AdmArea"], dict())
            result[curr_dict["AdmArea"]].setdefault(curr_dict["District"], []).append(curr_dict["Address"])
        else:
            json.dump(result, output_file, ensure_ascii=False, indent=3)


def task12():
    with open("students.json", encoding="utf-8") as input_file, \
            open("data12.csv", "w", encoding="utf-8", newline="") as output_file:
        data = json.load(input_file)
        res = [{"name": d["name"], "phone": d["phone"]} for d in data if
               int(d["age"]) >= 18 and int(d["progress"]) >= 75]
        res.sort(key=lambda x: x["name"])
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res)


def task13():
    with open("pools.json", encoding="utf-8") as input_file:
        pattern = "%H:%M"
        start_time = datetime.strptime("10:00", pattern)
        end_time = datetime.strptime("12:00", pattern)
        data = json.load(input_file)

        res = []
        for curr_dict in data:
            start_curr, end_curr = curr_dict["WorkingHoursSummer"]["Понедельник"].split("-")
            start_curr, end_curr = datetime.strptime(start_curr, pattern), datetime.strptime(end_curr, pattern)
            if start_curr <= start_time and end_curr >= end_time:
                res.append(
                    (
                        curr_dict.get("DimensionsSummer").get("Length"),
                        curr_dict.get("DimensionsSummer").get("Width"),
                        curr_dict.get("Address")))
        else:
            pool = max(res, key=lambda x: (int(x[0]), int(x[1])))
            print(f"{pool[0]}x{pool[1]}\n{pool[2]}")

    # def best_pool(data: dict):
    #     monday_time = data["WorkingHoursSummer"]["Понедельник"].split("-")
    #     start, finish = [int(time.split(":")[0]) for time in monday_time]
    #     time = True if start <= 10 and finish >= 12 else False
    #     dimensions = data["DimensionsSummer"]
    #
    #     return (time, dimensions["Length"], dimensions["Width"])
    #
    # with open("pools.json", "r", encoding="utf-8") as input_file:
    #     input_data = json.load(input_file)
    #
    #     choice = max(input_data, key=best_pool)
    #     print(f'{choice["DimensionsSummer"]["Length"]}x{choice["DimensionsSummer"]["Width"]}')
    #     print(choice["Address"])


def task14():
    with open("exam_results.csv", encoding="utf-8") as input_file, \
            open("best_scores.json", "w", encoding="utf-8") as output_file:
        reader = csv.DictReader(input_file)
        result = {}

        for line in reader:
            curr_dict = {"best_score" if k == "score" else k: v for k, v in line.items()}
            curr_dict["best_score"] = int(curr_dict["best_score"])
            result.setdefault(curr_dict.get("email"), curr_dict)

            if curr_dict["best_score"] >= result[curr_dict["email"]]["best_score"] \
                    and curr_dict["date_and_time"] > result[curr_dict["email"]]["date_and_time"]:
                result[curr_dict["email"]].update(curr_dict)

        else:
            json.dump(sorted(result.values(), key=lambda x: x.get("email")), output_file, indent=3)

        # result = {}
        # with open('exam_results.csv', encoding='utf-8') as ex_r:
        #     rows = csv.DictReader(ex_r)  # 1
        #     for row in rows:
        #         row['best_score'] = int(row.pop('score'))  # 2
        #         r = result.get(row['email'], row)  # 3
        #         best_row = max(r, row, key=lambda item: (
        #               item['best_score'], datetime.fromisoformat(item['date_and_time'])))  # 4
        #         result[row['email']] = best_row  # 5
        #
        # with open('best_scores.json', 'w', encoding='utf-8') as bs:
        #     out = sorted(result.values(), key=lambda item: item['email'])  # 6
        #     json.dump(out, bs, indent=3)  # 7


def task15(filename):
    with open(filename, encoding="utf-8") as input_file:
        data, districts, nets = json.load(input_file), {}, {}

        for curr_dict in data:
            districts[curr_dict["District"]] = districts.get(curr_dict["District"], 0) + 1
            if curr_dict["IsNetObject"] == "да":
                nets[curr_dict["OperatingCompany"]] = nets.get(curr_dict["OperatingCompany"], 0) + 1
        else:
            district = max(districts, key=districts.get)
            company = max(nets, key=nets.get)

        return f"{district}: {districts[district]}", f"{company}: {nets[company]}"


def task16():
    with open("food_services.json", encoding="utf-8") as input_file:
        data = json.load(input_file)
        result = {}

        for curr_dict in data:
            result.setdefault(
                curr_dict["TypeObject"],
                (curr_dict["Name"], curr_dict["SeatsCount"])
            )

            result[curr_dict["TypeObject"]] = max(
                result.get(curr_dict["TypeObject"]),
                (curr_dict["Name"], curr_dict["SeatsCount"]),
                key=lambda x: x[1]
            )
        else:
            for key, value in sorted(result.items(), key=lambda x: x[0]):
                print(f"{key}: {value[0]}, {value[1]}")

    # with open('food_services.json', 'r', encoding='utf-8') as f1:
    # data = json.load(f1)
    # d = {i['TypeObject']: f"{i['Name']}, {i['SeatsCount']}" for i
    #      in sorted(data, key=lambda x:(x['TypeObject'], x['SeatsCount']))}
    # for item in d.items():
    #     print(f'{item[0]}: {item[1]}')


if __name__ == "__main__":
    print(task1())
    print(task2())
    print(task3())
    print(task4())
    print(is_correct_json('number = 17'))
    print(task6())
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
    task13()
    task14()
    print(*task15(), sep='\n')
    task16()
