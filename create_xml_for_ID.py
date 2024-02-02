import sys
import re
import os
import glob
import logging

from functools import reduce
import csv
import xml.etree.ElementTree as xml

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

fragment_name = '-PRESTIG-MONTAG-710x600_VD_5000.xml'
count_maket = 12

def check_column_name(file_obj):
    name_standart =  ['num', 'pressrun', 'file', 'count']
    reader = csv.DictReader(file_obj, delimiter=';') 
    return name_standart == reader.fieldnames
            

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    dict = []
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        dict.append(line),
    return dict

def createXML(arr):
    """
    Задаем переменные
    """
    filename = f"{arr[0]["num"]}.xml"
    zakaz_number = arr[0]["num"]
    pressrun = arr[0]["pressrun"]
    count = 0
    path_image = 'file:///Volumes/data/%d0%a4%d0%98%d0%a0%d0%9c%d0%ab/PRESTIG/_PDF/'

    """
    Создаем XML файл.
    """
    root = xml.Element("Root")
    tiraj = xml.Element("tiraj")
    tiraj.text = pressrun
    root.append(tiraj)
    
    zakaz = xml.Element("zakaz")
    zakaz.text = zakaz_number
    root.append(zakaz)


    for item in arr:
        count += 1
        for j in range(int(item["count"])):
            count += j
            tag = f'image{count}'
            tag = xml.Element(tag, {'href': f'{path_image}{item["file"]}'})
            root.append(tag) 
    xml.dump(root)

    

    tree = xml.ElementTree(root)
    with open(filename, 'w') as out:
        tree.write(filename)
 
if __name__ == "__main__":
    start = False
    
    data = []
    zakaz = []
    with open("data.csv") as f_obj:
        start = check_column_name(f_obj)
    if start:
        try:
            with open("data.csv") as f_obj:
                data = csv_dict_reader(f_obj)
            for line in data:
                if line['num'] in zakaz:
                    continue
                zakaz.append(line['num'])
            for z_number in zakaz:
                temp_data = list(filter(lambda n: n['num'] == z_number, data))
                if reduce(lambda x,y: x + y, list(map(lambda item: int(item['count']), temp_data))) != count_maket:
                    error_num = reduce(lambda x,y: x + y, list(map(lambda item: int(item['count']), temp_data)))
                    logging.warning(f"в спуске номер {z_number} должно быть {count_maket} этикеток")
                createXML(temp_data)
                    
        except Exception as er:
            logging.error(er)
        

    else:
        print('ошибка')
   
