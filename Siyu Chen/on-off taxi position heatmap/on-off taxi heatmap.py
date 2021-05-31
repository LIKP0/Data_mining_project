from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


data_pair = list()
for i in range(1,111004):
    data_pair.append((str(i),1))


# visualize on_off taxi data
on_taxi = (
    Geo()
    .add_schema(maptype="深圳")
    .add_coordinate_json('on_taxi.json')
    .add("boarding point",data_pair,symbol_size=2)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Taxi boarding points in Shenzhen on 2013-10-22", pos_left='center'),
        legend_opts=opts.LegendOpts(pos_left='left',pos_top='middle')
    )
)
on_taxi.render('on taxi positions.html')
make_snapshot(snapshot, on_taxi.render(), "on taxi positions.png")

off_taxi = (
    Geo()
    .add_schema(maptype="深圳")
    .add_coordinate_json('off_taxi.json')
    .add("drop off point",data_pair,symbol_size=2)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Taxi drop off points in Shenzhen on 2013-10-22", pos_left='center'),
        legend_opts=opts.LegendOpts(pos_left='left',pos_top='middle')
    )
)
off_taxi.render('off taxi positions.html')
make_snapshot(snapshot, off_taxi.render(), "off taxi positions.png")
