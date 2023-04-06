from zipfile import ZipFile
from datetime import datetime


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


if __name__ == "__main__":
    print(task1("test.zip"))
    print(task2("workbook.zip"))
    print(task3("workbook.zip"))
    print(*task4("workbook.zip"), sep='\n')
    task5()
