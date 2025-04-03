# with open("./day25/weather_data.csv") as file:
#     data = file.readlines()

# print(data)

import pandas as pd

data = pd.read_csv("./day25/weather_data.csv")
print(data)
