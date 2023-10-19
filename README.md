[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Python Refresher Assignments 2 and 3
## The following shows assignments 2 and 3 for SWE4S. 
**This script takes a CSV file and displays data of interest. In this specific case, a column in the CSV file contains the number of fires during a period of time. Another column specifies the country this took place in. By using this script, you can display each fire that took place in a country of interest, as well as the total number of fires during the period of time that encapsulates the CSV file.

* To use this file, you must download the Agrofood_co2_eission.csv file available in the following [link](https://drive.google.com/file/d/1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr/view?usp=drive_link) and put it in the src directory.


**To run the main program files, switch directory to src. To run tests, switch directory to test/func or test/unit to run unit and functional tests.

* To run the test of this file, you must have pycodestyle installed.




**With this file, you can also analyze the food consumption trends in households in different countries. Default countries are the United States of America, Mexico, Canada and Japan. To change the countries, modify countries.txt inside the src folder. To run that functionality, move to the src directory and run snakemake by writing the following in the terminal:

# @_snakemake -c {x}_ where {x} is the number of cores you want to use to run the script.

**Be aware that running snakemake automatically downloads the Agrofood_co2_emission.csv file. 

This is the data you obtain by running the snakefile:
![Canada Food](doc/Canada.png?raw=true "Canada Food Consumption")
![Mexico Food](doc/Mexico.png?raw=true "Mexico Food Consumption")
![Japan Food](doc/Japan.png?raw=true "Japan Food Consumption")
![USA Food](doc/United%States%of%America.png?raw=true "US Food Consumption")




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

Changed other style errors in print_fires.py and in test_my_utils.py.

Changed more other style errors in print_fires.py and in test_my_utils.py, also changed the order of two lines in test_print_fires to ensure it runs.

Unit and func tests jobs are completed, style_check still doesn't complete, changed test_my_utils to try to fix that.

Changed test_my_utils.py, tried an except block to add the path of my_utils.py after importing the file.

Changed test_my_utils.py, it had a E302 error when running pycodestyle.

Removed run_all_tests test from yml file.

Added environment.yml and modified unit_test.yml to use an environment instead of installing pycodestyle.

Re-added run_all tests test to unit_test.yml.

Changed std dev to an int so run_all_tests and func test give the same result.

Changed miniconda to micromamba in style_check test in unit_test.yml file to make the execution of the test faster.


- Homework 6:

Added snakefile, hist.py, get_data.py, and countries.txt, moved them to src folder.

Changed get_data so that it retrieves data relating to food consumption per household from Agrofood_co2_emission.csv file.

Changed hist.py to make a plot instead of a histogram, showing the year as the x axis and the quantity of food consumption as the y axis. This graph shows how food consumption has changed in a country between 1990 and 2020. The countries.txt currently has United States of America, Mexico, Canada and Japan. Each plot shows the different rates of food consumption in the countries.

Added funtional tests for hist.py and get_data.py.

Changed yml test to incorporate new func tests.