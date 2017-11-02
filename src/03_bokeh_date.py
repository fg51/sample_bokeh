# -*- coding: utf-8 -*-
import datetime

from bokeh.plotting import figure, output_file, show


def main():
    data = sorted(
        ((str_to_date(i["date"]), i["sn"], i) for i in gen_data()),
        key = lambda x: (x[0], x[1]))


    output_file("date.html")
    p = figure(
        title="date sample",
        x_axis_type="datetime",
        # plot_width=400,
        # plot_height=400,
        # tools=["pan", hover, "save", "wheel_zoom", "reset"],
        active_scroll = "wheel_zoom",
        active_drag = "pan"
    )
    p.circle(
        [i[0] for i in data],
        [i[2]["x"] for i in data]
    )

    show(p)


def str_to_date(x):
    y = datetime.datetime.strptime(x, "%Y/%m/%d")
    return datetime.date(y.year, y.month, y.day)


def gen_data():
    yield {"date": "2017/05/01", "sn": 4, "x": 9, }
    yield {"date": "2017/05/01", "sn": 3, "x": 8, }
    yield {"date": "2017/10/01", "sn": 2, "x": 7, }
    yield {"date": "2017/01/01", "sn": 1, "x": 6, }


if __name__ == '__main__':
    main()
