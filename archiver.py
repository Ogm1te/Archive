import sys
from commands import *

args = sys.argv[1:]
folder_for_packing = ""
archive_for_unpackage = ""
file_to_add = ""
file_to_rm = ""
path = ""

# Ошибки
if len(args) < 3 or len(args) > 3:
    print("Error: incorrect number of parameters entered")
    sys.exit(1)
if (args[2][1:2] != ":"):
    print("Error: incorrect input")
    sys.exit(1)


# создание архива
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "create":
        folder_for_packing = args[elems_of_input+1] 


# распаковка архива
if args[0] == "unpack":
    archive_for_unpackage = args[1]
    path = args[2]
    with open(f"{path}", 'rb') as archiver:
        Unpack(archive_for_unpackage, path) #куда распаковываем, какой файл
else:
    print("Error: incorrect input")
    sys.exit(1)

# добавление файла в архив
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "add":
        break

# удаление файла из архива
for elems_of_input in range(len(args)-2):
    break
'''
библиотеку архивирования + добавление
библиотеку разархивирования + удаление
'''