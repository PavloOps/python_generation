import csv
from collections import namedtuple
from datetime import datetime


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

