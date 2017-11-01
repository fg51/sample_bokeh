# -*- coding: utf-8 -*-
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool


def main():
    output_file("toolbar.html")
    source = ColumnDataSource(data=dict(
        x=[1, 2, 3, 4, 5],
        y=[2, 5, 8, 2, 7],
        desc=["A", "b", "C", "d", "E"],
    ))

    """\
    $: special
    @: ColumnDataSource key name
    """
    hover = HoverTool(tooltips=[
        ("index", "$index"),
        ("(x,y)", "(@x, @y)"),
        ("desc", "@desc"),
    ])

    p = figure(
        title="Mouse over the dots",
        plot_width=400,
        plot_height=400,
        tools=["pan", hover, "save", "wheel_zoom", "reset"],
        active_scroll = "wheel_zoom",
        active_drag = "pan"
    )
    p.circle("x", "y", size=20, source=source)

    show(p)


if __name__ == '__main__':
    main()
