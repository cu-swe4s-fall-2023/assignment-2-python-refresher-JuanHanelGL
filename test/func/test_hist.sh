test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

script_path="../../src/hist.py"

if [ -f "Afghanistan.png" ]; then
    rm Afghanistan.jpg
fi

run get_data_test python $script_path --file_name "Afghanistan.txt" --out_file "Afghanistan.png" --title "Food Data" --x "Food_household_consumption" --y "Year"


assert_equal $"Afghanistan.png" $(ls $"Afghanistan.png")