
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

script_path="../../src/print_fires.py"

run mean_test python $script_path --country "United States of America" --country_column 0 --fires_column 4 --file_name "test_data.csv" --operation 2
assert_in_stdout 22679.533333333333
assert_exit_code 0


run median_test python $script_path --country "United States of America" --country_column 0 --fires_column 4 --file_name "test_data.csv" --operation 3
assert_in_stdout 22203
assert_exit_code 0


run std_dev_test python $script_path --country "United States of America" --country_column 0 --fires_column 4 --file_name "test_data.csv" --operation 4
assert_in_stdout 2972.362177722553
assert_in_stdout 2972.3621777225526
assert_exit_code 0


run sum_test python $script_path --country "United States of America" --country_column 0 --fires_column 4 --file_name "test_data.csv" --operation 1
assert_in_stdout 680386
assert_exit_code 0