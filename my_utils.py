def get_column(file_name, 
               query_column, 
               query_value, 
               result_column=1):
    
    result = []
    
    with open(file_name,'r') as f:
        for line in f:
            items = line.strip().split(',')
            if items[query_column] == query_value:
                result.append(items[result_column])

    return result