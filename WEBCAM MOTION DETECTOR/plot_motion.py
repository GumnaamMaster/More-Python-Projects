# when jupyter script was copied and pasted showed same result with atom editor as does jupyter notebook.
from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_con"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_con"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

# no need of these anymore and showing a runtime error as well.
# start = list(df["Start"])
# end = list(df["End"])

p = figure(width = 500, height = 100, x_axis_type = "datetime", sizing_mode = 'scale_width', title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

# without @ it will just show the string after hovering.
hover = HoverTool(tooltips = [("Start ","@Start_con"),("End ","@End_con")])
p.add_tools(hover)

p.quad(top = 1, bottom = 0, left = "Start", right = "End", color = "#B3DE69", source = cds)

output_file("Graph.html")
show(p)
