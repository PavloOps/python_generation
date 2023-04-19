import csv
from collections import namedtuple
from datetime import datetime
from collections import defaultdict
from collections import OrderedDict


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
