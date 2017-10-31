
import numpy as np
import holoviews as hv
hv.extension("bokeh")



# hv.Points(tools=["box_select", "lasso_select"])
points = hv.Points(np.random.randn(1000, 2))

selection = hv.streams.Selection1D(source=points)


def selected_info(index):
    arr = points.array()[index]
    if index:
        label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
    else:
        label = 'No selection'
    return points.clone(arr, label=label)(style=dict(color='red'))


layout = points + hv.DynamicMap(selected_info, streams=[selection])
print(layout)
