import os
import sys
import struct

CHUNK = 4096
HEADER = b'ABOBAHEH'

def Create(packing_file: str, folder_path: str):
    if os.path.isdir(folder_path): #массив с всеми файлами папки
        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        #основная часть создания файла
        with open(packing_file, 'wb') as file_to_archive:
            file_to_archive.write(struct.pack('<8s I', HEADER, len(files))) 
            
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

def UnpackArchive(packing_file: str, path: str):
    pass

def AddFile(archive_path: str, path: str):
    if not os.path.exists(path):
        print("incorret path")
        sys.exit(1)
    if not os.path.isfile(archive_path):
        print("uknown file")
        sys.exit(1)
    
    file_name = os.path.basename(path)
    bytes_of_file_name = file_name.encode('utf-8')
    size_of_file = os.path.getsize(path)

    tpm_archive = archive_path + ".tpm"

    with open(archive_path, 'rb') as our_archive:
        header = our_archive.read(struct.calcsize(HEADER))
        counter = struct.unpack(HEADER, header)

        with open(tpm_archive, 'wb') as tpm_archive:
            for i in range(counter): 
                file_format = struct.calcsize('<H')
                name_data = our_archive.read(file_format)
                len_of_name = struct.pack('<H', name_data)[0]
                bytes_of_name = our_archive.read(len_of_name)
                
                format = struct.calcsize('<Q')
                size_data = our_archive.read(format)
                our_archive_size = struct.unpack('<Q', size_data)[0]

                if bytes_of_name != bytes_of_file_name:
                    print("ahhaha")


            with open(path, 'rb') as input_file:
                while True: 
                    chunk = input_file.read(CHUNK)
                    if not chunk:
                        break
                    tpm_archive.write(chunk)
            

def Remove(removing_file: str, path: str):
    pass
    
        