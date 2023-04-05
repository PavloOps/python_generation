from zipfile import ZipFile


# lecture

with ZipFile("test.zip") as zip_file:
    zip_file.printdir()

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[6].file_size)                # размер начального файла в байтах
    print(info[6].compress_size)            # размер сжатого файла в байтах
    print(info[6].filename)                 # имя файла
    print(info[6].date_time)                # дата изменения файла

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[0].is_dir())
    print(info[6].is_dir())

with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()
    print(*info, sep='\n')

