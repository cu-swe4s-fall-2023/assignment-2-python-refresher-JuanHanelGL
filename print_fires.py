from my_utils import get_column

total_fires = 0
country='United States of America'
county_column = 0
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name, county_column, country, fires_column)

for i in range(len(fires)):
    fire = float(fires[i])
    total_fires = total_fires + fire
    
print(fires)
print("Sum of all fires in", country,": ", total_fires)