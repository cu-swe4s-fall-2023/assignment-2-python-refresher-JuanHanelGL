test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

script_path="../../src/get_data.py"

if [ -f "Afghanistan.txt" ]; then
    rm Afghanistan.txt
fi

run get_data_test python $script_path --file_name "test_data2.csv" --country "Afghanistan" --out_file "Afghanistan.txt"
assert_equal $"Afghanistan.txt" $(ls $"Afghanistan.txt")

expected_data_file="Expected_Afghanistan_data.txt"
run check_file_content diff "$expected_data_file" "Afghanistan.txt"
assert_exit_code 0