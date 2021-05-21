import pandas as pd
import numpy as np
import datetime
from interval import Interval
import matplotlib.pyplot as plt

positions = {"SZX": (113.8108, 22.6394), "Shenzhen Railway Station": (114.1236, 22.5379),
             "Futian District": (114.0598, 22.5289), 'Nanshan District': (113.9300, 22.5210)}
places = ["SZX", "Shenzhen Railway Station", "Futian District", 'Nanshan District']
radius = 0.02
# time1 = Interval("2013-10-22 07:00:00", "2013-10-22 10:00:00")  # morning
# time2 = Interval("2013-10-22 17:00:00", "2013-10-22 20:00:00")  # evening
hours = [i for i in range(24)]

if __name__ == "__main__":
    data = pd.read_csv("taxi2.csv")
    data['time'] = pd.to_datetime(data['time'])
    data['time'] = data['time'].apply(lambda x: x.replace(year=2013, month=10, day=22))

    # for i in range(24):
    #     hours.append(Interval("2013-10-22 {:0>2d}:00:00".format(i), "2013-10-22 {:0>2d}:00:00".format(i+1)))

    for i in places:
        if i.endswith('District'):
            radius = 0.04
        else:
            radius = 0.02
        data_place = data[(positions[i][0] - radius <= data['lon']) & (data['lon'] <= positions[i][0] + radius) &
                          (positions[i][1] - radius <= data['lat']) & (data['lat'] <= positions[i][1] + radius)]

        # data_time1 = data_place[data_place['time'] in time1]
        # data_time2 = data_place[data_place['time'] in time2]
        # get passengers and speed
        passenger_nums = np.zeros(24)
        speed_avgs = np.zeros(24)
        record_nums = np.zeros(24)
        for j in range(1, len(data_place)):
            hour = data_place.iloc[j]['time'].hour
            if data_place.iloc[j-1]['taxi_id'] == data_place.iloc[j]['taxi_id'] and \
                    data_place.iloc[j-1]['is_passenger'] == 0 and data_place.iloc[j]['is_passenger'] == 1:
                passenger_nums[hour] += 1
            speed_avgs[hour] += float(data_place.iloc[j]['speed'])
            record_nums[hour] += 1

        for j in range(24):
            speed_avgs[j] /= record_nums[j]

        plt.title("{} Number of times that carries passengers - time".format(i))
        plt.plot(hours, passenger_nums)
        plt.xlabel('time (hour)')
        plt.ylabel('times that carries passengers')
        plt.savefig("{0} Number of times that carries passengers.jpg".format(i))
        plt.show()

        plt.title("{} average speed - time".format(i))
        plt.plot(hours, speed_avgs)
        plt.xlabel("time (hour)")
        plt.ylabel("Average speed")
        plt.savefig('{0} average speed.jpg'.format(i))
        plt.show()
