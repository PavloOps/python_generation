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


def task_10():
    with open("name_log.csv", encoding="utf-8") as file_in, \
            open("new_name_log.csv", "w", encoding="UTF-8", newline="") as file_out:
        rows = csv.reader(file_in)
        writer = csv.writer(file_out)

        headers = next(rows)
        writer.writerow(headers)

        log_info = dict()
        for username, email, dtime in rows:
            log_info[email] = log_info.get(email, [username, email, ""])
            log_info[email] = max(log_info[email], (username, email, dtime), key=lambda x: x[-1])
        else:
            writer.writerows(sorted(log_info.values(), key=lambda x: x[1]))


def condense_csv(filename: str, id_name: str):
    with open(filename, encoding="utf-8-sig") as input_file, \
            open("condensed.csv", "w", encoding="utf-8", newline="") as output_file:
        data, data_dict = csv.reader(input_file), dict()
        writer = csv.writer(output_file)

        for obj, feature, value in data:
            data_dict.setdefault(obj, {}).update({feature: value})
        else:
            headers = [id_name, *data_dict[next(iter(data_dict))].keys()]

        writer.writerow(headers)
        for key in data_dict.keys():
            writer.writerow([key, *data_dict[key].values()])


def task_12():
    with open("student_counts.csv", encoding="utf-8") as input_file, \
            open("sorted_student_counts.csv", "w", encoding="utf-8-sig", newline="") as output_file:
        reader = csv.DictReader(input_file)
        headers = reader.fieldnames
        sorted_headers = [headers[0]] + sorted(headers[1:], key=lambda x: (len(x), x))

        writer = csv.DictWriter(output_file, fieldnames=sorted_headers)
        writer.writeheader()
        writer.writerows(reader)


def task_13(filename):
    with open(filename,
              encoding="utf-8") as csvfile:
        dict_reader = csv.DictReader(csvfile, delimiter=";")
        result = []

        for dictionary in dict_reader:
            temp = min(list(dictionary.items())[1:], key=lambda x: (int(x[1]), x))
            result.append((*temp, dictionary["Магазин"]))
        else:
            cheapest_item = min(result, key=lambda x: (int(x[1]), x[0], x[2]))

        return f"{cheapest_item[0]}: {cheapest_item[2]}"


if __name__ == "__main__":
    print(task_3())
    print(task_4())
    print(task_5())
    print(csv_columns("grades_test.csv"))
    print(task_7())
    print(task_8())
    print(task_9())
    task_10()
    condense_csv("test_easier_seems.csv", "ID")
    task_12()
    task_13()
