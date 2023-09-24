from my_utils import get_column
import argparse
import sys

#This function makes a total count  in the total_fires variable of the elements in the fires array.
def count_fires(fires):
    total_fires = 0
    for i in range(len(fires)):
        total_fires += fires[i]
    return total_fires


def main():
    #Argparse helps handle input parameters, showing an error if a critical input is missing.
    parser = argparse.ArgumentParser(
                description= 'Use this program to survey data from a CSV file.',
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
    
    args = parser.parse_args()
    
    #The arguments used as inputs are then used in the script, they are renamed to ease their use.
    country = args.country
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name
    
    #An exception is made in case the file can't be read due to file or permission errors.
    
    try:    
        fires = get_column(file_name, 
                           country_column, 
                           country, 
                           fires_column)
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
        #This stops the script when encountering the error.
        
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)
    
    
    #The count_fires function is used with the fires array as an argument.
    num_fires = count_fires(fires)
    

    print("Fires array: ", fires)
    print("Sum of all fires in", country,": ", num_fires)
    
    
    
if __name__ == "__main__":
    main()
    