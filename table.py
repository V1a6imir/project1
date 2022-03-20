import pickle
import csv
from beautifultable import BeautifulTable

def load_table(filename):
    if "csv" in filename:
        list_table = []
        list_row = []
        with open(filename, encoding='1251') as r_file:
            file_reader = csv.reader(r_file, delimiter=';')
            for row in file_reader:
                for cell in row:
                    list_row.append(cell)
                list_table.append(list_row)
                list_row = []
    elif "pickle" in filename:
        list_table = []
        list_row = []
        with open(filename, 'rb') as f:
            file_reader = pickle.load(f)
        for row in file_reader:
            for cell in row:
                list_row.append(cell)
            list_table.append(list_row)
            list_row=[]
    else:
        print('Неверный формат файла')
    return(list_table)

def save_table(tablename, file_name):
    if 'csv' in file_name:
        with open(file_name, mode='w', encoding='1251') as w_file:
            file_writer = csv.writer(w_file, delimiter=';', lineterminator='\r')
            for row in tablename:
                file_writer.writerow(row)
    elif 'pickle' in file_name:
        with open(file_name, 'wb') as f:
            pickle.dump(tablename, f)
    elif 'txt' in file_name:
        table_print = BeautifulTable()
        for row in tablename:
            table_print.append_row(row)
        table_print.columns.width = 14
        with open(file_name, "a") as table_file:
            print(table_print, file=table_file)
    else:
        print('Неверный формат файла')

def print_table(tablename):
    check=[]
    if type(check)==type(tablename):
        table_print=BeautifulTable()
        for row in tablename:
            table_print.append_row(row)
        table_print.columns.width = 14
        print(table_print)
    else:
        print('Переданы неверные данные')