import sys
import deflate


args = sys.argv[1:]
folder_for_packing = ""
archive_for_unpackage = ""
file_to_add = ""
file_to_rm = ""
path = ""

# Ошибки
if len(args) < 3 or len(args) > 3:
    sys.exit("Error: incorrect number of parameters entered")
if not args[2].startswith('\\'):
    sys.exit("Error: incorrect input")


# создание архива
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "create":
        folder_for_packing = args[elems_of_input+1] 
        with open() as archiver:

# распаковка архива
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "unpack" and args[elems_of_input+2].startswith('\\'):
        archive_for_unpackage = args[elems_of_input+1]
        path = args[elems_of_input + 2]
        with open(f"{path}", 'r') as archiver:
            Unpack(args[elems_of_input+1], path)
        break
    else:
        sys.exit("Error: incorrect input")

# добавление файла в архив
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "add":
        with open() as archiver:

# удаление файла из архива
for elems_of_input in range(len(args)-2):
    if args[elems_of_input] == "rm":
        with open() as archiver:

'''
библиотеку архивирования + добавление
библиотеку разархивирования + удаление

'''