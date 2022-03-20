def get_size(table: list) -> int:
    nrows = len(table)
    if nrows == 0:
        raise ValueError("Пустой список")

    ncols = []
    for row in table:
        ncols.append(len(row))

    if max(ncols) != min(ncols):
        raise IndexError('Строки одной таблицы должны быть одной длинны')
        # способ удостовериться, что строки одной длины, нет такого
        # что одна строка содержит бОльшее количество колонок,
        # чем другая

    return nrows 

def merge_tables(table_1: list, table_2: list, how: str = 'left',
                copy: bool = True,
                by_number: bool = True,
                fill_none: bool = False) -> list:

    if type(table_1) != list or type(table_2) != list:
        raise TypeError('Таблицы должны иметь тип list')
    
    size_1 = get_size(table_1)
    size_2 = get_size(table_2)

    if copy:
        table_1 = table_1[:]

    if by_number:

        if size_1 != size_2:
            
            if not fill_none:
                raise IndexError('Таблицы имеют разный размер, merge невозможен')

            if size_1 < size_2:
                table_1, table_2 = table_2, table_1

                for i in range(len(table_1)):
                    for j in range(len(table_2[0])):
                        try:
                            table_1[i].append(table_2[i][j])
                        except IndexError:
                            table_1[i].append(None)
        else:
            for i in range(len(table_1)):
                for j in range(len(table_2[i])):
                    table_1[i].append(table_2[i][j])

        return table_1

    else:
        keys_indexes_1 = {key: i for i, key in enumerate([row[0] for row in table_1])}
        keys_indexes_2 = {key: i for i, key in enumerate([row[0] for row in table_2])}

        if how == 'left':
            result_table = table_1
            joining_table = table_2
            if copy:
                result_table = result_table[:]
            for key in keys_indexes_1.keys():
                row_index = keys_indexes_1[key] # находим строку по айдишнику в левой таблице
                try:
                    # находим строку по айди в правой таблице
                    joining_row = joining_table[keys_indexes_2[key]] # строка КОТОРУЮ джойним (что присоединяем)
                except KeyError: # если такого айди нету
                    joining_row = [None] * len(table_2[0]) # добавляем None создается список [None, None, ..., None]
                for i in range(1, len(table_2[0])):
                    # добавляем к строке в левой таблице строку в правой, без 1ого элемента (индекса)
                    result_table[row_index].append(joining_row[i]) # строка К КОТОРОЙ джойним (куда присоединяем)

        elif how == 'right':
            result_table = table_2
            joining_table = table_1
            if copy:
                result_table = result_table[:]
            for key in keys_indexes_2.keys():
                row_index = keys_indexes_2[key]
                try:
                    joining_row = joining_table[keys_indexes_1[key]]
                except KeyError:
                    joining_row = [None] * len(table_1[0]) 
                for i in range(1, len(table_1[0])):
                    result_table[row_index].append(joining_row[i])

        elif how == 'inner':
            intersection_keys = set(keys_indexes_1.keys()) & set(keys_indexes_2.keys())
            # множеством, чтобы выполнить функицю пересечения
            
            result_table = []
            for key in intersection_keys:
                result_table.append([])
                row1_index = keys_indexes_1[key]
                row2_index = keys_indexes_2[key]
                row1 = table_1[row1_index]
                row2 = table_2[row2_index]

                for col_index in range(0, len(table_1[0])):
                    result_table[-1].append(row1[col_index])

                for col_index in range(1, len(table_2[0])):
                    result_table[-1].append(row2[col_index])           

        
    return result_table