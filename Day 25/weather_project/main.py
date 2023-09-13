import csv
import pandas

WEATHER_DATA_PATH = 'Day 25\\weather_project\\weather_data.csv'


# with open(WEATHER_DATA_PATH) as data_file:
#     data = csv.reader(data_file)
#     temparatures = []

#     for row in data:
#         if row[1] != "temp":
#             temparatures.append(int(row[1]))

# print(temparatures)

data = pandas.read_csv(WEATHER_DATA_PATH)
print(data)