[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Python Refresher Assignments 2 and 3
## The following shows assignments 2 and 3 for SWE4S. 
**This script takes a CSV file and displays data of interest. In this specific case, a column in the CSV file contains the number of fires during a period of time. Another column specifies the country this took place in. By using this script, you can display each fire that took place in a country of interest, as well as the total number of fires during the period of time that encapsulates the CSV file.**

* To use this file, you must download the Agrofood_co2_eission.csv file available in the following [link](https://drive.google.com/file/d/1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr/view?usp=drive_link)




The following is the workflow used in both assignments:


- Homework 2:

Added a default value of 1 to the result_column variable in the get_column() function of my_utils.py.

Modified the get_column function in the my_utils.py file. It now stores the values of the result column when a column of interest equals a wanted value.

Added a for loop to add all the values in fires and printed it on screen. 

Added shell script run.sh to run print_fires.py.



- Homework 3:

Made count_fires function in print_fires.py instead of running it as part of the main.

Added argparse to handle input parameters in the print_fires.py file.

The file now takes command-line arguments for country, country_column, fires_column and file_name.

Changed my_utils.py file, it used to return an array of strings, it now returns an array of integers.

Added command-line arguments to run.sh shell file.

Added exceptions in print_fires.py when reading the file.

Added exceptions in my_utils.py when converting data into an integer.

Added comments to the files.

Updated README.md with best practices in mind

Changed my_utils.py and print_fires.py to have all exceptions take place within the main code.



- Homework 4:

Added calculate_mean, calculate_median and calculate_std_dev to the my_utils.py

To use the functions, add the command line argument --operation 2,3, or 4. 
2 for mean, 3 for median and 4 for standard deviation, any other number or no argument shows the sum of the array.

Added the test_my_utils.py unit test file. To run the tests, you must do the following (outdated, not needed anymore):
Write in the terminal: export MY_UTILS_PATH=/.../...  ----> path to the directory where you are storing my_utils.py

Added src and test directories. Accidentaly added .git and .ipynb_checkpoints, attempting to clean up.

Changed the test_my_utils.py unit test to use the relative path of my_utils instead of setting up an environment.