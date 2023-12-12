
import os.path

print(os.path.abspath('best_scores.json'))                            # абсолютный путь

print(os.path.basename(os.path.abspath('best_scores.json')))          # имя файла

print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))             # общий подпуть

print(os.path.dirname(os.path.abspath('best_scores.json')))           # имя каталога в пути

print(os.path.exists('D:\py_learning\py_programs'))                   # проверка существования пути

print(os.path.getsize('D:\py_learning\py_programs\os\\best_scores.json')) # размер файла в байтах

print(os.path.join('home', 'User', 'Desktop', 'file.txt'))            # конкатенация пути

#print(os.path.normcase('C:\User\admin\Documents'))                   # нормализация пути
#print(os.path.normcase('/hoMe/UseR/'))
print(os.path.normpath('/home/./Documents'))

print(os.path.split('/home/User/Desktop/file.txt'))                   # выделение пути и названия файла 

print(os.path.splitext('/home/User/Desktop/file.txt'))                # выделение разрешения файла                  
