from table import *

def get_rows_by_number(*arg):
    start=arg[0]
    stop=""
    if type(arg[1])==int:
        stop=arg[1]
        copy_table=arg[2]
        file_name=arg[3]
    else:
        copy_table=arg[1]
        file_name = arg[2]

    table=load_table(file_name)
    test=len(table)
    if stop>=test or start>=test or start>=stop:
        print("Ошибка")
    else:
        new_table = []
        if stop == "":
            new_table.append(table[start - 1])
        else:
            for i in range(start - 1, stop):
                new_table.append(table[i])
        if copy_table:
            return new_table
        else:
            save_table(new_table, file_name)
            return new_table

def get_rows_by_index(*arg):
    arg=list(arg)
    file_name=arg[-1]
    arg.pop(-1)
    copy_table=arg[-1]
    arg.pop(-1)

    table = load_table(file_name)
    new_table=[]
    for row in table:
        if row[0] in arg:
            new_table.append(row)
    if new_table!=[]:
        if copy_table:
            return new_table
        else:
            save_table(new_table, file_name)
            return new_table
    else:
        print("Не найдены строки с такими параметрами")

def get_column_types(by_number, filename):
    if type(by_number)!=bool:
        print("Ошибка")
    else:
        table = load_table(filename)
        dic_table={}
        for cell in table[0]:
            i = table[0].index(cell)
            if by_number:
                c_ind="["+str(i)+"]"
            else:
                c_ind=cell
                type_cell=type(cell)
                dic_table[str(c_ind)] = type_cell
        return dic_table

def get_values(*arg):
    if len(arg)==2:
        column=arg[0]
        filename=arg[1]
    else:
        column=0
        filename=arg[0]
    table = load_table(filename)
    list_table=[]
    if type(column)!=int:
        column = table[0].index(column)
        table.pop(0)
    else:
        column=column-1
    cell_type=str(type(table[0][column]))
    for row in table:
        w=table.index(row)
        A=row[column]
        try:
            if 'str' in cell_type:
                A = str(A)
            elif 'int' in cell_type:
                A = int(A)
            elif 'float' in cell_type:
                A = float(A)
            elif 'bool' in cell_type:
                A = bool(A)
        except ValueError:
            print("Невозможно изменить тип данных ячейки [" + str(w + 1) + "][" + str(column+1) + "]")
        list_table.append(A)
    return list_table


def get_value(*arg):
    if len(arg)>2:
        print("Неверное количество параметров")
    else:
        if len(arg) == 2:
            column = arg[0]
            filename = arg[1]
        else:
            column = 0
            filename = arg[0]
        if type(column) != int:
            column = table[0].index(column)
            table.pop(0)
        else:
            column = column - 1
        for row in table:
            list_table.append(row[column])
        if len(list_table) == 1:
            return list_table[0]
        else:
            return list_table