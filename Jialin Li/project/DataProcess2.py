import os
import pandas as pd
import json
import random

# 3600 bus

if __name__ == "__main__":
    # TODO: sort
    # data = pd.read_csv("ShenZhen_busline.csv")
    # line_id = data['line_id']
    # lon = data['lon']
    # data.drop(['id', 'create_date', 'modify_date', 'line_id', 'lon'], axis=1, inplace=True)
    # data.insert(0, 'line_id', line_id)
    # data.insert(1, 'lon', lon)
    # data.dropna(inplace=True)
    # data.drop_duplicates(inplace=True)
    # data.sort_values(by=['line_id', 'point_order'], inplace=True)
    # data.to_csv('bus1.csv', index=False)

    # TODO: lon/lat fix
    # data = pd.read_csv("taxi1.csv")
    # data['lon'] = data['lon'] + 0.0125
    # data['lat'] = data['lat'] + 0.0077
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
    # csv = pd.read_csv("bus1.csv")
    # bus_id = set(csv['line_id'])
    # step = int(len(bus_id) / len(color)) + 1
    # result = []
    # i = 0
    # for item in set(csv['line_id']):
    #     dic = {}
    #     dic["coords"] = csv[csv['line_id'] == item].iloc[:, [1, 2]].values.tolist()
    #     dic["lineStyle"] = {"normal": {"color": color[int(i / step)]}}
    #     result.append(dic)
    #     i += 1
    #
    # with open('bus1.json', 'w') as f:
    #     json.dump(result, f)
    # f.close()

    # TODO: subset json
    js = pd.read_json('bus1.json')
    result = []
    for m in range(0, len(js['coords'])):
        sub = []
        dic = {}
        for n in range(0, len(js['coords'][m])):
            sub.append(js['coords'][m][n])
        dic["coords"] = sub
        dic["lineStyle"] = js['lineStyle'][m]
        result.append(dic)

    result = random.sample(result, int(len(result) / 5))
    with open('bus2.json', 'w') as f:
        json.dump(result, f)
    f.close()
    print(f'bus_num: {len(result)}')
    print(f'sample_rate: {100}%')

    os.system('python bmap_ShenZhen_bus_routines.py')
