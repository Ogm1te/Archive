import os
import sys
import struct

CHUNK = 4096
SIGNA = b'ABOBAHEH'

def Create(packing_file: str, folder_path: str):
    if os.path.isdir(folder_path): #массив со всеми файлами папки
        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

        with open(packing_file, 'wb') as file_to_archive:
            file_to_archive.write(struct.pack('<8s I', SIGNA, len(files))) 
            #записываем каждый файл в архив
            for elem in files: 
                file_path = os.path.join(folder_path, elem)
                size = os.path.getsize(file_path)
                name = elem.encode('utf-8')

                file_to_archive.write(struct.pack('<Q', size))
                file_to_archive.write(struct.pack('<H', len(name)))
                file_to_archive.write(name)

                with open(file_path, 'rb') as input_file:
                    while True: 
                        chunk = input_file.read(CHUNK)
                        if not chunk:
                            break
                        file_to_archive.write(chunk)
    else:
        print("error, unknown folder")
        sys.exit(1)

# Не рабочая функция
'''
def UnpackArchive(archive_path, dest_folder): 
    #"Распаковать все файлы из архива в указанную папку."
    os.makedirs(dest_folder,exist_ok=True)
    with open(archive_path, 'rb') as arc:
        header_data = arc.read(struct.calcsize(HEADER_FORMAT))

    sig, count = struct.unpack(HEADER_FORMAT, header_data)

    for_in range(count):
        name_len_data = arc.read(struct.calcsize(FILE_ENTRY_FORMAT)) 

        filename = name_bytes.decode('utf-8')
'''

def AddFile(archive_path: str, path: str):
    if not os.path.exists(archive_path):
        print("incorret path")
        sys.exit(1)

    if not os.path.isfile(path):
        print("uknown file")
        sys.exit(1)
    
    file_name = os.path.basename(path)
    bytes_of_file_name = file_name.encode('utf-8')

    tpm_archive = archive_path + ".tpm"

    with open(archive_path, 'rb') as our_archive:
        header = our_archive.read(struct.calcsize('<8s I'))
        counter = struct.unpack('<8s I', header)[1]


        with open(tpm_archive, 'wb') as tpm_arch:
            new_archive_counter = 0

            header_position = tpm_arch.tell()

            for i in range(counter): 
                name_data = our_archive.read(struct.calcsize('<H'))
                len_of_name = struct.unpack('<H', name_data)[0]
                bytes_of_name = our_archive.read(len_of_name)
                
                format = struct.calcsize('<Q')
                size_data = our_archive.read(format)

                if bytes_of_name != bytes_of_file_name:
                    tpm_arch.write(name_data)
                    tpm_arch.write(bytes_of_name)
                    tpm_arch.write(size_data)
                    
                    with open(path, 'rb') as input_file:
                        while True: 
                            chunk = input_file.read(CHUNK)
                            if not chunk:
                                break
                            tpm_arch.write(chunk)
                    new_archive_counter += 1

            tpm_arch.seek(header_position)
            tpm_arch.write(struct.pack('<8s I', SIGNA, new_archive_counter))

    os.replace(tpm_archive, archive_path)


def Remove(removing_file: str, path: str):
    pass
