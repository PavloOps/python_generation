import csv
import json
from collections import namedtuple
from datetime import datetime
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap


def task4_namedtuple():
    User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

    status = ["Gold", "Silver", "Bronze", "Basic"]

    res = []
    for user in sorted(users, key=lambda x: (status.index(x.plan), x.email)):
        res.append(f"{user.name} {user.surname}\n  Email: {user.email}\n  Plan: {user.plan}\n")
    return res


def task5_namedtuple():
    with open("meetings.csv", encoding="utf-8") as file:
        data = csv.reader(file)
        next(data)
        Person = namedtuple("Person", ["name", "surname", "date"])
        day_pattern = "%d.%m.%Y %H:%M"

        friends = [
            Person(surname, name, datetime.strptime(f"{day} {time}", day_pattern))
            for name, surname, day, time in data
        ]

        for friend in sorted(friends, key=lambda x: (x.date)):
            print(friend.surname, friend.name)


def task1_defaultdict():
    data = [
        ('Books', 1343),
        ('Books', 1166),
        ('Merch', 616),
        ('Courses', 966),
        ('Merch', 1145),
        ('Courses', 1061),
        ('Books', 848),
        ('Courses', 964),
        ('Tutorials', 832),
        ('Merch', 642),
        ('Books', 815),
        ('Tutorials', 1041),
        ('Books', 1218),
        ('Tutorials', 880),
        ('Books', 1003),
        ('Merch', 951),
        ('Books', 920),
        ('Merch', 729),
        ('Tutorials', 977),
        ('Books', 656)]

    result_dict = defaultdict(int)
    for name, value in data:
        result_dict[name] += value

    for key in sorted(result_dict):
        print(f"{key}: ${result_dict[key]}")


def task2_defaultdict():
    staff = [
        ('Sales', 'Robert Barnes'),
        ('Developing', 'Thomas Porter'),
        ('Accounting', 'James Wilkins'),
        ('Sales', 'Connie Reid'),
        ('Accounting', 'Brenda Davis'),
        ('Developing', 'Miguel Norris'),
        ('Accounting', 'Linda Hudson'),
        ('Developing', 'Deborah George'),
        ('Developing', 'Nicole Watts'),
        ('Marketing', 'Billy Lloyd'),
        ('Sales', 'Charlotte Cox'),
        ('Marketing', 'Bernice Ramos'),
        ('Sales', 'Jose Taylor'),
        ('Sales', 'Katie Warner'),
        ('Accounting', 'Steven Diaz'),
        ('Accounting', 'Kimberly Reynolds'),
        ('Accounting', 'John Watts'),
        ('Accounting', 'Dale Houston'),
        ('Developing', 'Arlene Gibson'),
        ('Marketing', 'Joyce Lawrence'),
        ('Accounting', 'Rosemary Garcia'),
        ('Marketing', 'Ralph Morgan'),
        ('Marketing', 'Sam Davis'),
        ('Marketing', 'Gail Hill'),
        ('Accounting', 'Michelle Wright'),
        ('Accounting', 'Casey Jenkins'),
        ('Sales', 'Evelyn Martin'),
        ('Accounting', 'Aaron Ferguson'),
        ('Marketing', 'Andrew Clark'),
        ('Marketing', 'John Gonzalez'),
        ('Developing', 'Wilma Woods'),
        ('Sales', 'Marie Cooper'),
        ('Accounting', 'Kay Scott'),
        ('Sales', 'Gladys Taylor'),
        ('Accounting', 'Ann Bell'),
        ('Accounting', 'Craig Wood'),
        ('Accounting', 'Gloria Higgins'),
        ('Marketing', 'Mario Reynolds'),
        ('Marketing', 'Helen Taylor'),
        ('Marketing', 'Mary King'),
        ('Accounting', 'Jane Jackson'),
        ('Marketing', 'Carol Peters'),
        ('Sales', 'Alicia Mendoza'),
        ('Accounting', 'Edna Cunningham'),
        ('Developing', 'Joyce Rivera'),
        ('Sales', 'Joseph Lee'),
        ('Sales', 'John White'),
        ('Marketing', 'Charles Bailey'),
        ('Sales', 'Chester Fernandez'),
        ('Sales', 'John Washington')
    ]

    count_dict = defaultdict(list)
    for department, employee in staff:
        count_dict[department].append(employee)

    for department in sorted(count_dict):
        print(f"{department}: {len(count_dict[department])}")


def task3_defaultdict():
    staff_broken = [
        ('Developing', 'Miguel Norris'),
        ('Sales', 'Connie Reid'),
        ('Sales', 'Joseph Lee'),
        ('Marketing', 'Carol Peters'),
        ('Accounting', 'Linda Hudson'),
        ('Accounting', 'Ann Bell'),
        ('Marketing', 'Ralph Morgan'),
        ('Accounting', 'Gloria Higgins'),
        ('Developing', 'Wilma Woods'),
        ('Developing', 'Wilma Woods'),
        ('Marketing', 'Bernice Ramos'),
        ('Marketing', 'Joyce Lawrence'),
        ('Accounting', 'Craig Wood'),
        ('Developing', 'Nicole Watts'),
        ('Sales', 'Jose Taylor'),
        ('Accounting', 'Linda Hudson'),
        ('Accounting', 'Edna Cunningham'),
        ('Sales', 'Jose Taylor'),
        ('Marketing', 'Helen Taylor'),
        ('Accounting', 'Kimberly Reynolds'),
        ('Marketing', 'Mary King'),
        ('Sales', 'Joseph Lee'),
        ('Accounting', 'Gloria Higgins'),
        ('Marketing', 'Andrew Clark'),
        ('Accounting', 'John Watts'),
        ('Accounting', 'Rosemary Garcia'),
        ('Accounting', 'Steven Diaz'),
        ('Marketing', 'Mary King'),
        ('Sales', 'Gladys Taylor'),
        ('Developing', 'Thomas Porter'),
        ('Accounting', 'Brenda Davis'),
        ('Sales', 'Connie Reid'),
        ('Sales', 'Alicia Mendoza'),
        ('Marketing', 'Mario Reynolds'),
        ('Sales', 'John White'),
        ('Developing', 'Joyce Rivera'),
        ('Accounting', 'Steven Diaz'),
        ('Developing', 'Arlene Gibson'),
        ('Sales', 'Robert Barnes'),
        ('Sales', 'Charlotte Cox'),
        ('Accounting', 'Craig Wood'),
        ('Marketing', 'Carol Peters'),
        ('Marketing', 'Ralph Morgan'),
        ('Accounting', 'Kay Scott'),
        ('Sales', 'Evelyn Martin'),
        ('Marketing', 'Billy Lloyd'),
        ('Sales', 'Gladys Taylor'),
        ('Developing', 'Deborah George'),
        ('Sales', 'Charlotte Cox'),
        ('Marketing', 'Sam Davis'),
        ('Sales', 'John White'),
        ('Sales', 'Marie Cooper'),
        ('Marketing', 'John Gonzalez'),
        ('Sales', 'John Washington'),
        ('Sales', 'Chester Fernandez'),
        ('Sales', 'Alicia Mendoza'),
        ('Sales', 'Katie Warner'),
        ('Accounting', 'Jane Jackson'),
        ('Sales', 'Chester Fernandez'),
        ('Marketing', 'Charles Bailey'),
        ('Marketing', 'Gail Hill'),
        ('Accounting', 'Casey Jenkins'),
        ('Accounting', 'James Wilkins'),
        ('Accounting', 'Casey Jenkins'),
        ('Marketing', 'Mario Reynolds'),
        ('Accounting', 'Aaron Ferguson'),
        ('Accounting', 'Kimberly Reynolds'),
        ('Sales', 'Robert Barnes'),
        ('Accounting', 'Aaron Ferguson'),
        ('Accounting', 'Jane Jackson'),
        ('Developing', 'Deborah George'),
        ('Accounting', 'Michelle Wright'),
        ('Accounting', 'Dale Houston')
    ]

    count_dict = defaultdict(set)
    for department, employee in staff_broken:
        count_dict[department].add(employee)

    for department in sorted(count_dict):
        print(f"{department}:", end=' ')
        print(*sorted(count_dict[department]), sep=', ')


def wins(pairs):
    result_dict = defaultdict(set)

    for winner, loser in pairs:
        result_dict[winner].add(loser)

    return result_dict


def flip_dict(dict_of_lists: dict):
    result_dict = defaultdict(list)

    for dict_key, value_list in dict_of_lists.items():
        for list_item in value_list:
            result_dict[list_item].append(dict_key)

    return result_dict


def best_sender(messages: list, senders: list) -> str:
    resulst_dict = defaultdict(int)
    for message, sender in zip(messages, senders):
        resulst_dict[sender] += len(message.split())

    return max(resulst_dict, key=lambda x: (resulst_dict[x], x))


def task2_ordered_dict(data: OrderedDict):
    new_dict = OrderedDict()

    for rule in range(len(data.keys())):
        key, value = data.popitem(last=rule%2)
        new_dict[key] = value

    return new_dict


data = OrderedDict(
    {
        'Law & Order': 1990,
        'The Practice': 1997,
        'Six Feet Under': 2001,
        'Joan of Arcadia': 2003,
        'The West Wing': 1999,
        'Deadwood': 2004,
        'The Sopranos': 1999,
        'Boston Legal': 2004,
        'ER': 1994,
        'Friday Night Lights': 2006,
        '24': 2001, 'Heroes': 2006,
        'Lost': 2004, 'Dexter': 2006,
        'Damages': 2007,
        'Big Love': 2006,
        'House': 2004,
        'Downton Abbey': 2010,
        "Grey's Anatomy": 2005,
        'Homeland': 2011,
        'Breaking Bad': 2008,
        'Game of Thrones': 2011,
        'CSI: Crime Scene Investigations': 2000,
        'Boardwalk Empire': 2010,
        'True Blood': 2008,
        'House of Cards': 2013,
        'True Detective': 2014
    }
)


def task3_ordered_dict(data: OrderedDict):
    data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
    data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)


def custom_sort(ordered_dict: OrderedDict, by_values=False) -> OrderedDict:
    for key, value in sorted(ordered_dict.items(), key=lambda x: x[by_values]):
        ordered_dict.move_to_end(key)


def task1_counter():
    files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
             'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
             'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
             'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
             'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
             'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
             'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
             'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
             'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
             'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
             'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
             'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
             'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

    result = Counter(file.rsplit(".", 1)[-1] for file in files)
    for key in sorted(result):
        print(f"{key}: {result[key]}")


def count_occurences(word: str, words: str) -> int:
    result = Counter(words.lower().split())
    return result[word.lower()]


def task3_counter():
    data = "рубашка,футболка,футболка,брюки,футболка,рубашка,носки,рубашка"
    for good, count in sorted(Counter(data.split(',')).items(), key=lambda x: x[0]):
        print(f"{good}: {count}")


def task4_counter():
    goods = "рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка"
    count_dict = Counter(goods.split(','))
    ident = len(max(count_dict, key=len))

    for key in sorted(count_dict):
        price, amount = sum(map(ord, "".join(key.split()))), count_dict[key]
        print(f"{key.ljust(ident)}: {price} UC x {amount} = {price*amount} UC")


def task5_counter():
    count_dict = Counter()
    with open("../working_with_files/pythonzen.txt", encoding="utf-8") as txt_file:
        for line in txt_file.readlines():
            count_dict.update(filter(str.isalpha, line.lower()))
        else:
            [print(f"{key}: {count_dict[key]}") for key in sorted(count_dict) if key]


def task1_counter2():
    data = "Арбуз Малина малина Арбуз клубника АрбуЗ Банан Малина вишня Черешня Вишня арбуз"
    result = Counter(data.lower().split())
    print(result.most_common()[0][0])


def task2_counter2():
    data = "Арбуз Малина Малина Арбуз Клубника арбуз банан малина вишня черешня вишня арбуЗ"
    counter = Counter(data.lower().split())
    minimum = min(counter.values())
    print(", ".join(item[0] for item in sorted(filter(lambda x: x[1] == minimum, counter.items()))))


def task3_counter2():
    data = "малина малина клубника арбуз банан малина черешня вишня арбуз клубника банан малина"
    counter = Counter(data.lower().split())
    result = max(counter.items(), key=lambda x: (x[1], x[0]))
    print(result[0])


def task4_counter2(data: str):
    counter = Counter(map(len, data.lower().split()))
    result = [f"Слов длины {key}: {value}" for key, value in sorted(counter.items(), key=lambda x: x[1])]
    return "\n".join(result)


def task6_counter2():
    data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
    data.__dict__["min_values"] = lambda: [item for item in sorted(filter(lambda x: x[1] == min(data.values()), data.items()))]
    data.max_values = lambda: [item for item in sorted(filter(lambda x: x[1] == max(data.values()), data.items()))]
    print(data.max_values())


def task7_counter2():
    counter = Counter()
    with open("../working_with_files/name_log2.csv", encoding="utf-8") as csv_file:
        for user in csv.DictReader(csv_file):
            counter.update({user['email']})
    for key, value in sorted(counter.items(), key=lambda x: x):
        print(f"{key}: {value}")


def scrabble(symbols: str, word: str) -> bool:
    return Counter(symbols) >= Counter(word)


def print_bar_chart(data: str | list[str], mark: str):
    counter = Counter(data)
    ident = len(max(data, key=len)) if isinstance(data, list) else 1

    for key, value in sorted(counter.items(), key=lambda x: -x[1]):
        print(f"{key.ljust(ident)}|{mark*value}")


def task10_counter2():
    counter = Counter()
    with open("prices.json", encoding="utf-8") as json_file:
        prices = json.load(json_file)

        for i in range(1, 5):
            with open(f"quarter{i}.csv", encoding="utf-8") as csv_file:
                _, *rows = csv.reader(csv_file)

                for name, *counts in rows:
                    counter.update({name: sum(map(int, counts))*prices[name]})
    print(counter.total())


def task1_chainmap():
    with open("zoo.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
        common_dict = ChainMap(*data)
        print(sum(common_dict.values()))


def task2_chainmap():
    bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
    meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
    sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
    vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
    toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

    ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
    input_string = "сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр,сыр"

    order = Counter(input_string.split(","))
    ident, dot_line, total = len(max(order, key=len)), 0, 0

    for ingredient in sorted(order):
        amount = order[ingredient]
        line = f"{ingredient.ljust(ident)} x {amount}"
        dot_line = max(dot_line, len(line))
        total += amount*ingredients[ingredient]
        print(line)
    else:
        line = f"ИТОГ: {total}р"
        dot_line = max(dot_line, len(line))
        print(dot_line*"-")
        print(line)


def deep_update(chainmap: ChainMap, key: str, value: str):
    if key in chainmap.keys():
        for inner_dict in chainmap.maps:
            if key in inner_dict:
                inner_dict[key] = value
    else:
        chainmap.maps[0][key] = value


def get_value(chainmap: ChainMap, key: str, from_left=True) -> str | None:
    if from_left:
        return chainmap.get(key)
    else:
        chainmap.maps.reverse()
        result = chainmap.get(key)
        return result


def main():
    pass


if __name__ == "main":
    main()
