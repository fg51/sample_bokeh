import numpy as np
import holoviews as hv
import holoviews.plotting.bokeh
from bokeh.io import show

hv.extension("bokeh")

# # Declare some points
# points = hv.Points(np.random.randn(1000, 2))

# # Declare points as source of selection stream
# selection = hv.streams.Selection1D(source=points)


# def selected_info(index):
#     # Write function that uses the selection indices to slice points and compute stats
#     arr = points.array()[index]
#     label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0)) if index else 'No selection'
#     return points.clone(arr, label=label)(style=dict(color='red'))

# # Combine points and DynamicMap


# layout = points + hv.DynamicMap(selected_info, streams=[selection])
# layout

# renderer = hv.renderer("bokeh")  # type: hv.BokehRendere
# renderer = renderer.instance(mode="server")  # type: hv.BokehRendere

# hvplot = renderer.get_plot(layout)  # type: hv.LayoutPlot

# html = renderer.figure_data(hvplot)


layout = hv.Points(np.random.randn(1000, 2))
show(layout, notebook_url="localhost:8888")

html = hv.renderer("bokeh").server_doc(layout)
show(html, notebook_url="localhost:8888")
