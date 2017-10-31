#coding: utf-8

from bokeh.plotting import figure, output_file, show

xs = [1, 2, 3, 4, 5]
ys = [6, 7, 2, 4, 5]


output_file("01_plot.html")
p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
p.line(xs, ys, legend="temp.", line_width=2)

# NOTE: show graph. and save html.
show(p)
