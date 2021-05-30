import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans

df = pd.read_csv("od.csv")
print(len(df))
print(df['origin_lon'])
print(df['origin_lat'])
plt.axis([113.7, 114.4, 22.45, 22.85])
plt.scatter(df['origin_lon'].values, df['origin_lat'].values, s=0.08, color='blue')

plt.show()

print(df['destination_lon'])
print(df['destination_lat'])
plt.axis([113.7, 114.4, 22.45, 22.85])
plt.scatter(df['destination_lon'].values, df['destination_lat'].values, s=0.08, color='green')

plt.show()

estimator = KMeans(n_clusters=8)
df = df.drop(df[df['origin_lon'] < 113.7].index)
df = df.drop(df[df['origin_lon'] > 114.4].index)
df = df.drop(df[df['origin_lat'] > 22.85].index)
df = df.drop(df[df['origin_lat'] < 22.45].index)
data = np.vstack((np.array(df['origin_lon']), df['origin_lat'])).T
label = estimator.fit_predict(data)
print(label)
centroids = estimator.cluster_centers_
inertia = estimator.inertia_
colors = ['red', 'black', 'green', 'teal', 'blue', 'brown', 'purple', 'salmon']

j = 0
plt.axis([113.7, 114.4, 22.45, 22.85])
for i in np.unique(label):
    plt.scatter([data[label == i, 0]], [data[label == i, 1]], label=i, color=colors[i], s=0.08)
    j += 1
plt.show()
dfz = df.drop(df[df['origin_time'] > '10:00:00'].index)
dfz = dfz.drop(df[df['origin_time'] < '07:00:00'].index)
dataz = np.vstack((np.array(dfz['destination_lon']), dfz['destination_lat'])).T
estimator = KMeans(n_clusters=8)
label = estimator.fit_predict(dataz)
j = 0
plt.axis([113.7, 114.4, 22.45, 22.85])
for i in np.unique(label):
    plt.scatter([dataz[label == i, 0]], [dataz[label == i, 1]], label=i, color=colors[i], s=0.08)
    j += 1
plt.show()

dfw = df.drop(df[df['origin_time'] > '24:00:00'].index)
dfw = dfw.drop(df[df['origin_time'] < '21:00:00'].index)
dataw = np.vstack((np.array(dfw['destination_lon']), dfw['destination_lat'])).T
estimator = KMeans(n_clusters=8)
label = estimator.fit_predict(dataw)
j = 0
plt.axis([113.7, 114.4, 22.45, 22.85])
for i in np.unique(label):
    plt.scatter([dataw[label == i, 0]], [dataw[label == i, 1]], label=i, color=colors[i], s=0.08)
    j += 1
plt.show()

