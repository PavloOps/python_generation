from zipfile import ZipFile


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

        return len(res)


if __name__ == "__main__":
    print(task1("test.zip"))
