import pandas as pd
import os
import re
import shutil
import time
import tqdm

print(os.path.basename(__file__))
exe_dir = os.path.dirname(os.path.abspath(__file__))
program_path = os.path.join(exe_dir, os.path.basename(__file__))
print("Запущен файл, расположенный: ", program_path)
dir_encrypted=input('Введите директорию в которой расположены дата сеты: ')
file_encrypted=input('Введите имя нешифрованного датасета: ')
df1=pd.read_csv(dir_encrypted+'//'+file_encrypted, encoding='cp1251')
# Датафрейм в котором шифрованные файлы и структура
# Путь абсолютный для запуска из .exe
df2=pd.read_csv(dir_encrypted+'//'+input("Введите название датасета ШИФРОВАННОГО: "), encoding='cp1251')
def temp_file(second, first):
    if second['filename'] in first['full filename'].values:
        if second['filename'][-3:] in collections or second['filename'] in collections:
            pass
        else:
            q = first[first['full filename'] == second['filename']]
            for j in range(len(q)):
                if size == q.iloc[j]['size'] or size-427 == q.iloc[j]['size']:
                    new = os.getlogin() + second['directory'][2:] + "\\"
                    copy(second, q.iloc[j], new)
                else:
                    pass
            else:
                pass
    return


def copy(second, third, new):
    global count,vol
    orig = third['directory'] + "\\" + second['filename']
    if os.path.isdir(new) == False:
        os.makedirs(new)
        new += second['filename']
        shutil.copy2(f'{orig}', f'{new}')
        count += 1
        vol += second['size']
        print('Файл скопирован: ', os.path.dirname(os.path.abspath(__file__))+new)
    else:
        new += second['filename']
        shutil.copy2(f'{orig}', f'{new}')
        count += 1
        vol += second['size']
        print('Файл скопирован: ', os.path.dirname(os.path.abspath(__file__))+new)

progress_bar = tqdm.trange(len(df2), desc='Searchng', unit= 'files')
count=0
vol=0
collections = ['log', 'Thumbs.db', 'err']
temp_dir=['AppData\\Local\\Temp']
for i in progress_bar:
    #Имя первого файла, размер
    size = df2.iloc[i]['size']
    #Проверка папки Temp в Local
    if df2.iloc[i]['filename'][:9] in df1['full filename'].values and temp_dir[0] in df1['directory']:
        temp_file(df2.iloc[i],df1)
        continue


    #Проверк есть ли такое имя в структуре
    if df2.iloc[i]['filename'] in df1['full filename'].values:
        #if df2.iloc[i]['filename'][-3:] =='log' or df2.iloc[i]['filename']=="Thumbs.db":
        if df2.iloc[i]['filename'][-3:] in collections or df2.iloc[i]['filename'] in collections:
            pass
        else:
            # print('Файл есть в оригинале. Найдено совпадений:', df1['full filename'].str.contains(df2.iloc[i][
            #Создание нового датафрейма с подходящим условием по имени файла
            q=df1[df1['full filename'] == df2.iloc[i]['filename']]
            #Работаем с новым датафреймом
            for j in range(len(q)):
                #Проверка оригинального размера файла и файла в новом датафрейме. Ищем совпадения
                if size == q.iloc[j]['size'] or size-427 == q.iloc[j]['size']:
                    # Печать значения, что найден файл с именем, расположением, размером оригинала и найденным размером
                    # Задание пути куда будет все копироваться Путь текущая папка плюс имя пользователя текущего и путь
                    new = os.getlogin() + df2.iloc[i]['directory'][2:] + "\\"
                    #абсолютный путь
                    copy(df2.iloc[i], q.iloc[j], new)

                else:
                    pass
                    # print('Файл не подходит:', df2.iloc[i]['filename'], 'размер оригинальный:', \
                    #       size, "размер найденного файла:", q.iloc[j]['size'])
            else:
                pass
            progress_bar.write("")
print(f'Было найдено и скопировано файлов: {count}', f'\nОбщий объем найденной информации составляет:{str(vol)}Байт',
      f'\nИли объем найденной информации  составляет: {str(vol/1073741824)[:4]}Гб',f'\nИли объем найденной '
                                                                                     f'информации составляет: {str(vol/1048576)[:6]}Мб')
print('Для завершения нажмитие клавишу Enter')
input()

# pyinstaller --onefile check_progress_v1_2.py
# pyinstaller --onefile fnd_file.py






