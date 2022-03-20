from table import *

def set_column_types(types_dict, by_number, filename):
    table = load_table(filename)
    if by_number:
        for row in table:
            w=table.index(row)
            for cell in row:
                try:
                    i = row.index(cell)+1
                    cell_type=types_dict[i]
                    if cell_type=='str':
                        row[i-1]=str(cell)
                    elif cell_type=='int':
                        row[i-1]=int(cell)
                    elif cell_type=='float':
                        row[i-1]=float(cell)
                    elif cell_type=='bool':
                        row[i-1] = bool(cell)
                except ValueError:
                    print("Невозможно изменить тип данных ячейки ["+ str(w+1)+"]["+str(i)+"]")
    else:
        list_column=[]
        for cell in table[0]:
            list_column.append(cell)
        table.pop(0)
        for row in table:
            w=table.index(row)
            for cell in row:
                y=row.index(cell)
                i=list_column[y]
                cell_type = types_dict[i]
                try:
                    if cell_type == 'str':
                        row[y] = str(cell)
                    elif cell_type == 'int':
                        row[y] = int(cell)
                    elif cell_type == 'float':
                        row[y] = float(cell)
                    elif cell_type == 'bool':
                        row[y] = bool(cell)
                except ValueError:
                    print("Невозможно изменить тип данных ячейки ["+ str(w+1)+"]["+str(y)+"]")
    return table

def set_values(*arg):
    if len(arg)==3:
        values=arg[0]
        column=arg[1]-1
        filename=arg[2]
    else:
        values=arg[0]
        column=0
        filename=arg[1]
    table_s=load_table(filename)
    cell_type=type(values[0])
    W=True
    for cell in values:
        c_type=type(cell)
        if c_type!=cell_type:
            W=False
    if W:
        for row in table_s:
            d_row=table_s.index(row)
            row[column]=values[d_row]
        return table_s
    else:
        print("Передан неверный список")
        return table_s

def set_value(*arg):
    if len(arg)==3:
        value=arg[0]
        column=arg[1]-1
        filename=arg[2]
    else:
        value=arg[0]
        column=0
        filename=arg[1]
    table=load_table(filename)
    if type(value)==type(table[0][column]):
        table[0][column] = value
        return table
    else:
        print("Передан неверный список")
        return table