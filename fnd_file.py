import os
import re
import csv
import time
print(os.getlogin())
print(os.getenv('temp'))

def walk_dir(start_file):
    start = time.perf_counter()
    #Получение имени файлов и пути к файлов и запись их в табличку
    #Запись заголовка таблицы

    # with open(f'data_{os.getlogin()}.csv', 'w', newline='') as t:
    #     writer = csv.writer(t)
    #     writer.writerow(('full filename', 'filename','directory', 'size'))
    #Запись имени файла и путь в таблицу (игнорируя ошибку)
    with open(f'data_{os.getlogin()}.csv', 'a', newline='') as t:
        for root, dirs, files in os.walk(start_file):
            for file in files:
                try:
                    print(os.path.join(root,file))
                    print(os.path.join(file))
                    #a='dwg'
                    #print(*re.findall(rf"(.+?\.{a})", file))
                    pattern = r'\.id.*'
                    filename = re.sub(pattern, '', file)
                    print(filename)
                    filepath = fr'{root+"/"+file}'
                    #print(filepath)
                    size=os.path.getsize(filepath)
                    writer =csv.writer(t)
                    writer.writerow((file, filename, root, size))
                    #writer.writerow((file,root))
                except:
                    print('error')


    finish = time.perf_counter()
    print('Время работы: ' + str(finish - start))

    start_file = input('Введите путь директории для сканирования или нажмитие Enter для завершения: ')
    if start_file == '':
        pass
    else:
        walk_dir(start_file)

def main():
    start_file=input('Введите путь директории для сканирования или нажмитие Enter для завершения: ')
    if start_file == '':
        pass
    else:
        with open(f'data_{os.getlogin()}.csv', 'w', newline='') as t:
            writer = csv.writer(t)
            writer.writerow(('full filename', 'filename', 'directory', 'size'))
        walk_dir(rf'{start_file}')

main()

# pyinstaller --onefile check_progress.py
