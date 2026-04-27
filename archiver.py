import sys
from commands import *

args = sys.argv[1:]
folder_for_packing = ""
archive_for_unpackage = ""
file_to_add = ""
file_to_rm = ""
path = ""

# Ошибки
if len(args) != 3:
    print("Error: incorrect number of parameters entered")
    sys.exit(1)


# создание архива
if args[0] == "create":
    archive_for_package = args[1]
    path = args[2]
    Create(archive_for_unpackage, path) #куда упаковываем, какой файл
# распаковка архива
elif args[0] == "unpack":
    folder_for_packing = args[1]
    path = args[2]
    with open(f"{path}", 'rb') as archiver:
        Unpack(archive_for_unpackage, path) #куда распаковываем, какой файл
# добавление файла в архив
elif args[0] == "add":
    archive_for_package = args[1]
    path = args[2]
    Create(archive_for_unpackage, path) 

# удаление файла из архива
elif args[0] == "remove":
    archive_for_package = args[1]
    path = args[2]
    Add(file_to_add, path) 
else:
    print("Error: incorrect input")
    sys.exit(1)

'''
библиотеку архивирования + добавление
библиотеку разархивирования + удаление
'''