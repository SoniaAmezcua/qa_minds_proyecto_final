def get_data(filename):
    data = []
    with open(filename,'r') as file:
        lines = file.readlines()
        for row in lines:
            if '\n' in row:
                row = row[:-1] 
            list_row = row.split(',')
            if len(list_row) == 1:
                data.append(list_row[0])
            else:
                data.append(list_row) 
    return data

