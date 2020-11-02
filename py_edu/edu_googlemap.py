#%%
from bokeh.io import output_file, show
from bokeh.plotting import gmap
from bokeh.models import ColumnDataSource, GMapOptions

output_file("googlemapkey.html")

map_options = GMapOptions(lat=37.251675, lng=127.071319, map_type="roadmap", zoom=17)

p = gmap("AIzaSyCJgzh39iHJI-3PFCCEEsjjVuAzmJGFfdw", map_options= map_options, title ="dd")

source = ColumnDataSource(
    data = dict(lat =[37.251638, 37.251914, 37.251128],
                lon = [127.071844, 127.070546, 127.070621]))
p.circle(x = "lon", y = "lat", size = 30, fill_color ="blue", fill_alpha = 0.4, source = source)

show(p)

# %%
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=30.29, lng=-97.73, map_type="roadmap", zoom=11)

plot = GMapPlot( x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Austin")

source = ColumnDataSource(
    data=dict(
        lat=[30.29, 30.20, 30.29],
        lon=[-97.70, -97.74, -97.78],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)
# %%
