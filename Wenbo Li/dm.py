import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

df = pd.read_csv("taxi2.csv")
print(len(df))
print(df.iloc[1])
i = 0
f = open('od.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(['taxi_id', 'origin_lon', 'origin_lat', 'destination_lon', 'destination_lat', 'origin_time', 'end_time'])
while i < len(df):
    if df.iloc[i].is_passenger == 0:
        i += 1
        continue
    else:
        cur_id = df.iloc[i].taxi_id
        ori_lon = df.iloc[i].lon
        ori_lat = df.iloc[i].lat
        ori_time = df.iloc[i].time
        flag = True
        i += 1
        while flag:
            if df.iloc[i].taxi_id == cur_id and df.iloc[i].is_passenger == 1:
                i += 1
            else:
                flag = False
                if df.iloc[i].taxi_id == cur_id:
                    writer.writerow([cur_id, ori_lon, ori_lat, df.iloc[i].lon, df.iloc[i].lat, ori_time, df.iloc[i].time])
                else:
                    writer.writerow([cur_id, ori_lon, ori_lat, df.iloc[i-1].lon, df.iloc[i-1].lat, ori_time, df.iloc[i-1].time])
f.close()