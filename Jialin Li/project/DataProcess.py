import datetime
import os
import random
import pandas as pd
import json

# taxi: 3000
from interval import Interval

if __name__ == "__main__":
    # TODO: sort
    data = pd.read_csv("sample_taxi.csv")
    # data.drop(['is_passenger', 'speed'], axis=1, inplace=True)
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    data['time'] = pd.to_datetime(data['time'])
    data['time'] = data['time'].apply(lambda x: x.replace(year=2013, month=10, day=22))  # .dt.datetime
    data.sort_values(by=['taxi_id', 'time'], inplace=True)
    data = data.drop(
        labels=data.loc[(data['lon'] > 120) | (data['lon'] < 110) | (data['lat'] > 25) | (data['lat'] < 20)].index)
    last_no_move = {'id': -1, 'time': "", 'index': 0}
    for i in range(len(data)):
        datum = data.iloc[i]
        if datum['speed'] <= 1:
            if last_no_move['id'] != datum['taxi_id']:
                last_no_move['id'] = datum['taxi_id']
                last_no_move['time'] = Interval(datum['time'], datum['time'])
                last_no_move['index'] = datum.index
            else:
                last_no_move['time'] = Interval(datum['time'], datum['time'])
        else:
            if isinstance(last_no_move['time'], Interval):
                if (last_no_move['time'].upper_bound - last_no_move['time'].lower_bound).seconds > 1800:  # interval greater than half an hour
                    data.drop(labels=range(last_no_move['index'], datum.index - 1), inplace=True)
            last_no_move = {'id': -1, 'time': "", 'index': 0}
        # data.drop()
    # data = data.drop(['index'], axis=1)
    data.to_csv('taxi3.csv', index=False)

    # TODO: lon/lat fix
    # data = pd.read_csv("taxi1.csv")
    # data['lon'] = data['lon'] + 0.0125
    # data['lat'] = data['lat'] + 0.0077
    # data.to_csv('taxi1.csv', index=False)

    # TODO: lon/lat fix
    # data = pd.read_csv("taxi1.csv")
    # data['lon'] = data['lon'].apply(lambda x: round(x, 4))
    # data['lat'] = data['lat'].apply(lambda x: round(x, 4))
    # data.to_csv('taxi1.csv', index=False)

    # TODO: get color
    # js = pd.read_json('busRoutines.json')['lineStyle']
    # a = set()
    # color = []  # 301
    # for i in js:
    #     b = i['normal']['color']
    #     if b not in a:
    #         a.add(b)
    #         color.append(b)

    # TODO: create json
    # csv = pd.read_csv("taxi1.csv")
    # taxi_id = csv.drop_duplicates(subset=['taxi_id'])['taxi_id']
    # step = round(taxi_id.shape[0] / len(color))
    # result = []
    # i = 0
    # for item in set(csv['taxi_id']):
    #     dic = {}
    #     dic["coords"] = csv[csv['taxi_id'] == item].iloc[:, [2, 3]].values.tolist()
    #     dic["lineStyle"] = {"normal": {"color": color[int(i / step)]}}
    #     result.append(dic)
    #     i += 1
    #
    # with open('taxi1.json', 'w') as f:
    #     json.dump(result, f)
    # f.close()

    # TODO: subset json
    # js = pd.read_json('taxi1.json')
    # result = []
    # sample_rate = 2  # 更改采样率 1/2
    # for m in range(0, len(js['coords'])):
    #     sub = []
    #     dic = {}
    #     for n in range(0, len(js['coords'][m])):
    #         if n % sample_rate == 0:
    #             sub.append(js['coords'][m][n])
    #     dic["coords"] = sub
    #     dic["lineStyle"] = js['lineStyle'][m]
    #     result.append(dic)
    #
    # result = random.sample(result, int(len(result) / 30))  # 更改出租车数量 1/30
    # with open('taxi2.json', 'w') as f:
    #     json.dump(result, f)
    # f.close()
    # print(f'taxi_num: {len(result)}')
    # print(f'sample_rate: {1 / sample_rate * 100}%')
    #
    # os.system('python bmap_ShenZhen_taxi_routines.py')
