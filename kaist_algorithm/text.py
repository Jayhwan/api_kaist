import json, pandas as pd

with open("./data/20220529_20220531_forecast.json", 'r') as file:
    data = json.load(file)

print(data)

f = pd.read_excel('./data/20220529_20220531_forecast.xlsx')
print(f)
print(f.get(['ttime', 'SKY']))
print(f.iloc[5:10])