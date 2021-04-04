
import csv

with open("weather_data_csv.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
    print('ok')