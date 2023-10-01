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


def calculate_mean(array):
    return sum(array) / len(array)


def calculate_median(array):
    array.sort()
    length = len(array)
    if length % 2 == 0:
        return (array[length // 2 - 1] + array[length // 2]) / 2
    else:
        return array[length // 2]

    
def calculate_std_dev(array):
    mean = sum(array) / len(array)
    variance = sum((x - mean) ** 2 for x in array) / len(array)
    return variance ** 0.5
