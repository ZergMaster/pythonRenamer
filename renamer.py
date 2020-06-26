import os

path = r"D:\Proj\ViktoriaPlus\cubercat\cybercat\Assets\Resources\Sprites\ui\Helmet\Icons\big"
    
	
#добавить в нечало имени файлов строку
def addStringToFronName(addit):
    for file_name in os.listdir(path):
	    # Имя файла и его формат
        base_name, ext = os.path.splitext(file_name)
        print("hi "+str(file_name))
		
		# Полный путь к текущему файлу
        abs_file_name = os.path.join(path, file_name)

        new_abs_file_name = os.path.join(path, addit + base_name)
		
        print('old name = '+base_name)
        print('new name = '+new_abs_file_name)

        os.rename(abs_file_name, new_abs_file_name)


#переименовать файлы c вхождением:
def renameFilesFromTo(renamePart, renameTo):
    for file_name in os.listdir(path):
        # Имя файла и его формат
        base_name, ext = os.path.splitext(file_name)

        print("hi "+file_name)
        print(ext)

        # Полный путь к текущему файлу
        abs_file_name = os.path.join(path, file_name)
        
        if base_name[:len(renamePart)] == renamePart:
            new_abs_file_name = os.path.join(path, renameTo + base_name[len(renamePart):] + ext)
            os.rename(abs_file_name, new_abs_file_name)

    

##  #Изменить нумерацию с 1-n на 0-n до сотен  
def changeNumeration():
    for file_name in os.listdir(path):
        # Имя файла и его формат
        
        base_name, ext = os.path.splitext(file_name)

        print("hi "+file_name)
        print(ext)

        # Полный путь к текущему файлу
        abs_file_name = os.path.join(path, file_name)
    
        print('changeNumeration')
        fileNum = file_name.split('.')[0][-2:]
        fileName = file_name.split('.')[0][:-2]
        intFileNum = 0
    
        try:
            intFileNum = int(fileNum)
        except:
            fileNum = file_name.split('.')[0][-1:]
            fileName = file_name.split('.')[0][:-1]
            intFileNum = int(fileNum)
        
        print(intFileNum)
        if intFileNum>0:
            intFileNum -= 1
            print('new file name is: '+fileName+str(intFileNum)+ext)
            new_abs_file_name = os.path.join(path, '___'+fileName + str(intFileNum) + ext)
            os.rename(abs_file_name, new_abs_file_name)
            
            
            
    for file_name in os.listdir(path):
        base_name, ext = os.path.splitext(file_name)
        abs_file_name = os.path.join(path, file_name)
        print(file_name[:3])
        if file_name[:3] == '___':
            print(file_name[3:])
            print('new file name is: '+file_name[3:])
            new_abs_file_name = os.path.join(path, file_name[3:])
            os.rename(abs_file_name, new_abs_file_name)
        
    
#удалить все файлв форматов:    
def deleFilesFormats(formats):
    for file_name in os.listdir(path):
        base_name, ext = os.path.splitext(file_name)
        print("hi "+file_name)
        print(ext)
        abs_file_name = os.path.join(path, file_name)
        
        if ext.lower() in ['.meta', '.mp3']:
            os.remove(abs_file_name)
        

#добавить формат ко всем файлам без формата
def addFormat(f):
    for file_name in os.listdir(path):
        base_name, ext = os.path.splitext(file_name)
        print("hi "+file_name)
        print(ext)
        abs_file_name = os.path.join(path, file_name)
        
        if ext == '':
            new_abs_file_name = os.path.join(path, base_name + f)
            os.rename(abs_file_name, new_abs_file_name)

    
##addStringToFronName('Helmet')
##changeNumeration()
##renameFilesFromTo('No_act_helmet', 'Helmet')
##deleteFilesFormats(['.meta', '.mp3'])
##addFormat('.png')