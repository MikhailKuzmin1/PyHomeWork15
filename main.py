# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит: 
    # ○ имя файла без расширения или название каталога, 
    # ○ расширение, если это файл, 
    # ○ флаг каталога, 
    # ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
from collections import namedtuple
import argparse
import logging

loger = logging.getLogger(__name__)
format = '{asctime:<20} - {levelname:<10} - {msg}'
logging.basicConfig(filename='my_log.log', filemode='w', encoding='UTF-8', level=logging.INFO, 
                    format=format, style='{')

def direct(path):
    list_files = []
    *_,parent_dir = path.split('\\')
    for i in os.listdir(path):
        list_files.append(i.split('.'))
    for i in list_files:
        if len(i) < 2:
            i.append('У дириктории нет  расширения!')
    for list in list_files:
        if len(list) == 2:
            list.append('False')
            list.append(parent_dir)
        else:
            list.append('True')
            list.append(parent_dir)
    return list_files

parser = argparse.ArgumentParser(description='parser')
parser.add_argument("path", help="directory path", type=str)
args = parser.parse_args()

list = direct(args.path)

Dir = namedtuple("Dir", ["name", "exp", "flag", "parent"])
for i in list:
    dirictory = Dir(i[0], i[1], i[2], i[3] )
    loger.info(msg=f'{dirictory}')
    print(dirictory)