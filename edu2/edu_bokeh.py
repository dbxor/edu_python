#%%
#pip3 install bokeh
#bokeh.sampledata.download()

from bokeh.plotting import figure
from bokeh.io import show, push_notebook, output_notebook, output_file
from bokeh.resources import INLINE

import numpy as np

output_notebook(resources=INLINE)

p = figure(plot_width = 800,
            plot_height = 600,
            title ="bokeh sample",
            x_axis_label = "X",
            y_axis_label = "Y")

rec_x = [1,2,3,4,5]
rec_y = [6,7,8,9,10]
cir_x = [1,2,4,8,6]
cir_y = [3,9,6,8,10]

x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)*2

p.line(x, y, legend_label = "Value", line_width = 3)
p.square(rec_x, rec_y, size = 12, color = "green", alpha = 0.6)

p.circle(cir_x, cir_y, size = 12, color = "red")
#output_notebook()#
output_file("output.html")

show(p)
#%%
