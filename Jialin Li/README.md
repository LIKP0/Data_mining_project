### 结果

网上示例：bmap_Beijing_bus_routines.html

自己制作：

bmap_ShenZhen_bus_routines.html (1/5版本，视觉效果好) 

bmap_ShenZhen_bus_routines_full.html (文件太大浏览器比较卡)

bmap_ShenZhen_taxi_routines.html (每辆车50%轨迹采样率，1/30车辆数，结果相对好看)

出租车原数据量太大，每辆车轨迹坐标测绘非常频繁，而且轨迹有往复，还有一些错误数据(直接导致了一些谜之直线)

出租车数据问题比较大，暂时没法解决。公交车数据很好。

### 数据

原始数据：

ShenZhen_busline.csv https://opendata.sz.gov.cn/data/dataSet/toDataDetails/29200_00403600 深圳公交路线（2019）

sample_taxi.csv  BB上面下载的深圳一日出租车数据

bus1.csv taxi1.csv 原数据处理出的csv

bus1.json taxi1.json 由csv得到的json文件用于绘图

bus2.json taxi2.json 是1.json的子集（每辆车轨迹间隔采样+总数随机抽取），真正生成html文件

### 其它

DataProcess.py 以及DataProcess2.py 分步骤做了数据处理和绘图

bmap_ShenZhen_bus_routines.py文件负责读取json绘图，基本不需要修改（我也没找到对应API）

需要权衡采样率和抽取率，防止生成html文件太大（浏览器开150M文件就会很卡，150M以上可能根本打不开）

2.json文件和它生成的html文件大小基本在1：5

### 问题

1. taxi绘图可以再调调参数，需要注意提高采样率可以让轨迹更精细，提高车辆数会让图变得拥挤。。。提高二者太多会出现谜之放射线。。。如果可以解决斜线的问题会好很多，这是与数据有关的。
2. 我想给出租车的所有可能坐标做个聚类，求出聚类中心再分析应该可以得到比较好的数据，再去画图可能好看很多。但是我懒得。。。
3. 参考北京公交路线，可以发现颜色越向中心越深，是由它本身数据决定的。我的数据里面的颜色是由他平均分配的。。。希望也可以做到线条越密集颜色越深
4. 分析还没做。观察他们的路线可以很容易发现热门目的地。
