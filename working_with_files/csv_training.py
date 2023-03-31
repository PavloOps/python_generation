import csv
from collections import Counter


def task_3():
    with open("sales.csv", encoding="UTF-8") as file:
        rows = csv.DictReader(file, delimiter=";")
        for d in filter(lambda x: int(x["old_price"]) > int(x["new_price"]), rows):
            print(d["name"])


def task_4():
    mean_dict = {}

    with open("salary_data.csv", encoding="UTF-8") as file:
        rows = csv.DictReader(file, delimiter=";")
        for row in rows:
            company_name, salary = row.values()
            mean_dict.setdefault(company_name, [0, 0])
            mean_dict[company_name][0] += float(salary)
            mean_dict[company_name][1] += 1
        else:
            res = map(lambda x: (x[0], x[1][0] / x[1][1]), mean_dict.items())
        for tup in sorted(res, key=lambda x: (x[1], x[0])):
            print(tup[0])


def task_5():
    with open("deniro.csv", encoding="UTF-8") as file:
        index = 0
        table = list(csv.reader(file))
        table.sort(key=lambda x: int(x[index]) if x[index].isdigit() else x[index])
        for tup in table:
            print(",".join(tup))


def csv_columns(filename):  # 6
    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))

        return {key: value for key, *value in zip(*rows)}


def task_7():
    with open("data.csv", encoding="UTF-8") as input_file, open(
        "domain_usage.csv", "w", encoding="UTF-8", newline=""
    ) as output_file:
        data = csv.reader(input_file)  # iterator
        next(data)  # drop headers
        domains = [tup for tup in zip(*data)][-1]  # next lays of iterator
        count_domains = Counter(
            [text.split("@")[-1] for text in domains]
        )  # dict with counts
        res = sorted(
            count_domains.items(), key=lambda x: (x[1], x[0])
        )  # sorted list to write

        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(["domain", "count"])
        writer.writerows(res)


def task_8():
    with open("wifi.csv", encoding="UTF-8") as input_file:
        res = dict()
        rows = csv.reader(input_file, delimiter=";")
        next(rows)

        for row in rows:
            adm_area, district, location, points = row
            res[district] = res.get(district, 0) + int(points)
        else:
            for key, value in sorted(res.items(), key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")


def task_9():
    with open("titanic.csv", encoding="UTF-8") as file:
        data = csv.reader(file, delimiter=";")
        next(data)

        res = ((name, gender) for survived, name, gender, age in data if int(survived) and float(age) < 18)
        print(*map(lambda x: x[0], sorted(res, key=lambda x: x[1], reverse=True)), sep='\n')


if __name__ == "__main__":
    print(task_3())
    print(task_4())
    print(task_5())
    print(csv_columns("grades_test.csv"))
    print(task_7())
    print(task_8())
    print(task_9())
