#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed


#This runs, prints the mean of the array
python print_fires.py --country "United States of America" --country_column 0 --fires_column 4 --file_name "Agrofood_co2_emission.csv" --operation 2

#This runs, prints the sum of the array
python print_fires.py --country "United States of America" --country_column 0 --fires_column 4 --file_name "Agrofood_co2_emission.csv"

#This does not run -file reading error
set +e  #Continue on error
python print_fires.py --country "United States of America" --country_column 0 --fires_column 4 --file_name "Agrofood_co2_eission.csv"

#This does not run -error converting valie
python print_fires.py --country "United States of America" --country_column 0 --fires_column 0 --file_name "Agrofood_co2_emission.csv"
set -e #Stop on error