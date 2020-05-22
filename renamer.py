import os

path = r"E:\Viktor\Proj\ViktoriaPlus\cubercat\cybercat\Assets\Resources\Sprites\ui\Helmet\bg"

#i = 1

for file_name in os.listdir(path):
    # Имя файла и его формат
    base_name, ext = os.path.splitext(file_name)

    print("hi "+file_name)
    print(base_name[:5])
    print(ext)

    # Полный путь к текущему файлу
    abs_file_name = os.path.join(path, file_name)

##    if base_name[:5] == 'House':
##    	continue

    #переименовать файлы c вхождением:
    renamePart = 'planeSize'
    renameTo = 'bg'
    if base_name[:len(renamePart)] == renamePart:
      new_abs_file_name = os.path.join(path, renameTo + base_name[len(renamePart):] + ext)
      os.rename(abs_file_name, new_abs_file_name)

    #удалить все файлв формата:
    ##if ext.lower() in ['.meta', '.mp3']:
    ##    os.remove(abs_file_name)


    #переименовать все файлы, если пустые:
    ##if ext == '':
        ##new_abs_file_name = os.path.join(path, base_name + '.mp3')
        ##os.rename(abs_file_name, new_abs_file_name)

    #i += 1