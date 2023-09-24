import sys

def get_column(file_name, 
               query_column, 
               query_value, 
               result_column=1):
    
    result = []
    
    with open(file_name,'r') as f:
        for line in f:
            #The file is processed line by line, it is split into arrays.
            items = line.strip().split(',')
            if items[query_column] == query_value:
                #This exception stops the script if the values in the array could not convert to int.
                try:
                    new_int=float(items[result_column])
                    result.append(int(new_int))
                except ValueError:
                    print('Could not convert "', items[query_column],'" value to an integer')
                    sys.exit(1)
                    
    return result