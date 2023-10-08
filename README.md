[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Python Refresher Assignments 2 and 3
## The following shows assignments 2 and 3 for SWE4S. 
**This script takes a CSV file and displays data of interest. In this specific case, a column in the CSV file contains the number of fires during a period of time. Another column specifies the country this took place in. By using this script, you can display each fire that took place in a country of interest, as well as the total number of fires during the period of time that encapsulates the CSV file.

* To use this file, you must download the Agrofood_co2_eission.csv file available in the following [link] (https://drive.google.com/file/d/1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr/view?usp=drive_link) and put it in the src directory.


**To run the main program files, switch directory to src. To run tests, switch directory to test/func or test/unit to run unit and functional tests.

**To run the test of this file, you must have pycodestyle installed.




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

Reverted to version 3.2, I had added the csv file and did not know how to remove it. There were also other unwanted files.
Added unit test and directories.

Cleaned the repo up, removed .ipynb_checkpoints folders and added to .gitignore as best as I could.
Added func test, first in python, but then removed it and added in bash. Functional test doesn't yet have a working code.
Reverting to version 3.2 was not the best idea, it would have been better to remove the additional files/ directories, as I had to do it that way anyways.

Added functionality to func test. It now tests mean, median, standard deviation and sum of the print_fires.py file.


- Homework 5:

Added unit_test.yml to run continuous integration tests. Added test for unit tests, functional tests and style checks. 
Added lines to install pycodestyle before running the style check.
Fixed identation in yml script.
Changed style errors in print_fires.py and my_utils.py files.