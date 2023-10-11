from my_utils import (
    get_column,
    calculate_mean,
    calculate_median,
    calculate_std_dev)
import argparse
import sys


# This function makes a total count  in
# the total_fires variable of the elements in the fires array.
def count_fires(fires):
    total_fires = 0
    for i in range(len(fires)):
        total_fires += fires[i]
    return total_fires


def change_to_int(array):
    int_array = []
    for i in range(len(array)):
        new_int = float(array[i])
        int_array.append(int(new_int))
    return int_array


# This ensures that if there is no value given for operation,
# the code still runs, as it is given a default value.
def do_operation(operation=1):
    state = 1
    if operation == 2:
        state = 2
    elif operation == 3:
        state = 3
    elif operation == 4:
        state = 4
    return state


def main():
    operation_type = 'Sum'
    # Argparse helps handle input parameters,
    # showing an error if a critical input is missing.
    parser = argparse.ArgumentParser(
                description='Use with CSV file.',
                prog='print_fires.py')

    parser.add_argument('--country',
                        type=str,
                        help='Country of interest',
                        required=True)

    parser.add_argument('--country_column',
                        type=int,
                        help='Column corresponding to the country',
                        required=True)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Column of interest',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help="Name of the file",
                        required=True)

    parser.add_argument('--operation',
                        type=int,
                        help="Operation to perform with array",
                        required=False)

    args = parser.parse_args()
    new_int = 0.0
    total_count = 0

    # The arguments used as inputs are then used in the script,
    # they are renamed to ease their use.
    country = args.country
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name
    operation = args.operation

    # An exception is made in case the file can't be read due
    # to file or permission errors.

    try:
        fires = get_column(file_name,
                           country_column,
                           country,
                           fires_column)
        int_array = change_to_int(fires)
        num_fires = count_fires(int_array)

    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
        # This stops the script when encountering the error.

    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    except ValueError:
        print('Could not convert value to an integer')
        sys.exit(1)

    state = do_operation(operation)

    result_array = num_fires

    if state == 2:
        result_array = calculate_mean(int_array)
        operation_type = 'Mean'
    elif state == 3:
        result_array = calculate_median(int_array)
        operation_type = 'Median'
    elif state == 4:
        result_array = int(calculate_std_dev(int_array))
        operation_type = 'Standard deviation'

    print("Fires array: ", int_array)
    print(operation_type, ': ', result_array)


if __name__ == "__main__":
    main()
