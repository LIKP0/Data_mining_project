import pandas as pd
import numpy as np
import datetime
from interval import Interval
import matplotlib.pyplot as plt

positions = {  # "SZX": (113.8108, 22.6394), "Shenzhen Railway Station": (114.1236, 22.5379),
    "Shenzhen North Railway Station": (114.0275, 22.6083)
    # "Futian District": (114.0598, 22.5289), 'Nanshan District': (113.9300, 22.5210)
}
places = [  # "SZX", "Shenzhen Railway Station",
    "Shenzhen North Railway Station"
    # , "Futian District", 'Nanshan District'
]
radius = 0.02
# time1 = Interval("2013-10-22 07:00:00", "2013-10-22 10:00:00")  # morning
# time2 = Interval("2013-10-22 17:00:00", "2013-10-22 20:00:00")  # evening
# hours = [i for i in range(24)]
intervals = []

if __name__ == "__main__":
    data = pd.read_csv("taxi3.csv")
    data['time'] = pd.to_datetime(data['time'])
    data['time'] = data['time'].apply(lambda x: x.replace(year=2013, month=10, day=22))

    for i in range(24):
        for j in range(20, 61, 20):
            intervals.append("{:0>2d}:{:0>2d}".format(i, j - 20))

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
        # print(len(intervals))
        passenger_nums = np.zeros(len(intervals))
        speed_avgs = np.zeros(len(intervals))
        record_nums = np.zeros(len(intervals))
        for j in range(1, len(data_place)):
            hour = data_place.iloc[j]['time'].hour
            minute = data_place.iloc[j]['time'].minute
            # print(minute)
            idx = hour * 3 + minute // 20
            if data_place.iloc[j - 1]['taxi_id'] == data_place.iloc[j]['taxi_id'] and \
                    data_place.iloc[j - 1]['is_passenger'] == 0 and data_place.iloc[j]['is_passenger'] == 1:
                passenger_nums[idx] += 1
            speed_avgs[idx] += float(data_place.iloc[j]['speed'])
            record_nums[idx] += 1

        for j in range(len(intervals)):
            speed_avgs[j] /= record_nums[j]

        fig, ax = plt.subplots()
        plt.title("{} Number of times that carries passengers - time".format(i))
        plt.plot(intervals, passenger_nums)
        plt.xlabel('time')
        plt.ylabel('times that carries passengers')
        count = 0
        for label in ax.xaxis.get_ticklabels():
            if count % 6 != 0:
                label.set_visible(False)
            label.set_rotation(45)
            # label.set_alignment('right')
            count += 1
        plt.savefig("{0} Number of times that carries passengers.jpg".format(i))
        plt.show()

        fig, ax = plt.subplots()
        plt.title("{} average speed - time".format(i))
        plt.plot(intervals, speed_avgs)
        plt.xlabel("time")
        plt.ylabel("Average speed")
        count = 0
        for label in ax.xaxis.get_ticklabels():
            if count % 6 != 0:
                label.set_visible(False)
            label.set_rotation(45)
            # label.set_alignment('right')
            count += 1
        plt.savefig('{0} average speed.jpg'.format(i))
        plt.show()

    # calculate the avg speed of all cars
    # passenger_nums = np.zeros(len(intervals))
    # speed_avgs = np.zeros(len(intervals))
    # record_nums = np.zeros(len(intervals))
    # for j in range(1, len(data)):
    #     hour = data.iloc[j]['time'].hour
    #     minute = data.iloc[j]['time'].minute
    #     idx = hour * 3 + minute // 20
    #     if data.iloc[j - 1]['taxi_id'] == data.iloc[j]['taxi_id'] and \
    #             data.iloc[j - 1]['is_passenger'] == 0 and data.iloc[j]['is_passenger'] == 1:
    #         passenger_nums[idx] += 1
    #     speed_avgs[idx] += float(data.iloc[j]['speed'])
    #     record_nums[idx] += 1
    #
    # for j in range(len(speed_avgs)):
    #     speed_avgs[j] /= record_nums[j]
    #
    # fig, ax = plt.subplots()
    # plt.title("Shenzhen - Number of times that carries passengers - time")
    # plt.plot(intervals, passenger_nums)
    # plt.xlabel('time')
    # plt.ylabel('times that carries passengers')
    # count = 0
    # for label in ax.xaxis.get_ticklabels():
    #     if count % 6 != 0:
    #         label.set_visible(False)
    #     label.set_rotation(45)
    #     # label.set_alignment('right')
    #     count += 1
    # plt.savefig("Shenzhen Number of times that carries passengers.jpg")
    # plt.show()
    #
    # fig, ax = plt.subplots()
    # plt.title("Shenzhen average speed speed - time")
    # plt.plot(intervals, speed_avgs)
    # plt.xlabel("time (hour)")
    # plt.ylabel("Average speed")
    # count = 0
    # for label in ax.xaxis.get_ticklabels():
    #     if count % 6 != 0:
    #         label.set_visible(False)
    #     label.set_rotation(45)
    #     # label.set_alignment('right')
    #     count += 1
    # plt.savefig('Shenzhen average speed.jpg')
    # plt.show()
