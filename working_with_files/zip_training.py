import json
import os.path
from zipfile import ZipFile
from datetime import datetime
from working_with_files.json_training import is_correct_json
from math import floor, log

# lecture

# with ZipFile("test.zip") as zip_file:
#     zip_file.printdir()
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(type(info[6].file_size))
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)                # дата изменения файла
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(len(info))
#     print(info[0].is_dir())
#     print(info[6].is_dir())
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(len(info))
#     print(*info, sep='\n')


def task1(filename):
    with ZipFile(filename) as zip_file:
        files_info = zip_file.infolist()
        res = [item for item in files_info if item.file_size]
        # res = [item for item in files_info if not item.is_dir()]

        return len(res)


def task2(filename):
    with ZipFile(filename) as zip_file:
        files_info = zip_file.infolist()
        sum_initial_size = sum(item.file_size for item in files_info)
        sum_compress_size = sum(item.compress_size for item in files_info)
        return f"""Объем исходных файлов: {sum_initial_size} байт(а)
Объем сжатых файлов: {sum_compress_size} байт(а)"""


def task3(filename):
    with ZipFile(filename) as zip_file:
        files_info = zip_file.infolist()
        coef_compress = (((item.compress_size / item.file_size) * 100, item.filename)
                         for item in files_info if not item.is_dir())
        result = min(coef_compress, key=lambda x: x[0])[1]
        return result.rsplit("/", 1)[-1]


def task4(filename):
    with ZipFile(filename) as zipfile:
        files_info = zipfile.infolist()
        pattern = "%Y-%m-%d %H:%M:%S"
        checkpoint = datetime.strptime("2021-11-30 14:22:00", pattern)
        res = (
            f.filename.rsplit("/", 1)[-1]
            for f in files_info
            if datetime(*f.date_time) > checkpoint and not f.is_dir()
        )
        return sorted(res)


def task5():
    with ZipFile("workbook.zip") as zip_file:
        files_info = zip_file.infolist()
        files = (
            (
                item.filename.rsplit("/", 1)[-1],
                datetime(*item.date_time).strftime("%Y-%m-%d %H:%M:%S"),
                item.file_size,
                item.compress_size
            )
            for item in files_info if not item.is_dir()
        )
        for file in sorted(files, key=lambda x: x[0]):
            print(f"""{file[0]}
      Дата модификации файла: {file[1]}
      Объем исходного файла: {file[2]} байт(а)
      Объем сжатого файла: {file[3]} байт(а)\n""")


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        zip_file.extractall(members=args if args else None)


def task9():
    with ZipFile('data.zip') as zip_file:
        result = []
        for item in zip_file.infolist():
            if not item.is_dir():
                try:
                    with zip_file.open(item.filename) as file:
                        data = file.read().decode("utf-8")
                        if is_correct_json(data):
                            curr_dict = json.loads(data)
                            team = curr_dict.get("team")
                            if team and team == "Arsenal":
                                result.append((curr_dict.get("first_name"), curr_dict.get("last_name")))
                except UnicodeDecodeError:
                    continue
        else:
            for player in sorted(result):
                print(*player)


def get_unit_name(size: int) -> str:
    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')
    pwr = floor(log(size, 1024))
    return f'{size / 1024 ** pwr:.0f} {unit_names[pwr]}'


def get_unit_name(size: int) -> str:
    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')
    pwr = floor(log(size, 1024))
    return f'{size / 1024 ** pwr:.0f} {unit_names[pwr]}'


def task10():
    with ZipFile("desktop.zip") as zip_file:
        for item in zip_file.infolist():
            path_structure = item.filename.strip("/").split("/")
            indent = (len(path_structure)-1)*2

            if item.is_dir():
                print(" "*indent + path_structure[-1])
            else:
                title, init_size = os.path.basename(item.filename), get_unit_name(item.file_size)
                print(' '*indent + title, init_size)


if __name__ == "__main__":
    print(task1("test.zip"))
    print(task2("workbook.zip"))
    print(task3("workbook.zip"))
    print(*task4("workbook.zip"), sep='\n')
    task5()
    print(task9())
    print(task10())