import os
import sys
import struct

CHUNK = 4096

def Create(packing_file: str, folder_path: str):
    if os.path.isdir(folder_path): #массив с всеми файлами папки
        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        #основная часть создания файла
        with open(packing_file, 'wb') as file_to_archive:
            file_to_archive.write(struct.pack('<8s I', b'ABOBAHEH', len(files))) 
            for i in files: 
                file_path = os.path.join(folder_path, i)
                size = os.path.getsize(file_path)
                name = i.encode('utf-8')
                #информация для работы с данными
                file_to_archive.write(struct.pack('<Q', size))
                file_to_archive.write(struct.pack('<H', len(name)))
                file_to_archive.write(name) #запись файла
                with open(file_path, 'rb') as input_file:
                    while True: 
                        chunk = input_file.read(CHUNK)
                        if not chunk:
                            break
                        file_to_archive.write(chunk)
    else:
        print("error, unknown folder")
        sys.exit(1)
'''
мы получаем "имя" "куда распаковывать" "откуда брать"
мы вытаскиваем из архива файл 
'''

def Unpack(packing_file: str, path: str):
    pass

def AddFile(adding_file: str, path: str):
    pass

def Remove(removing_file: str, path: str):
    pass
    
        