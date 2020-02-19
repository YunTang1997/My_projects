from pyecharts.charts import Line  # 画折线图
from pyecharts import options as opts  # 设置标题
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode


def line_base():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="Line-基本示例"))

    )
    return c


line_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure17.html")


def line_xaxis_type():
    c = (
        Line()
        .add_xaxis(Faker.values())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="Line-数值 X 轴"),
                         xaxis_opts=opts.AxisOpts(type_="value"))
    )
    return c


line_xaxis_type().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure18.html")


def line_connect_null():
    y = Faker.values()
    y[3], y[5] = None, None
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", y, is_connect_nones=True)
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="Line-连接空数据"))
    )
    return c


line_connect_null().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure19.html")


def line_smooth():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_smooth=True)
        .add_yaxis("商家B", Faker.values(), is_smooth=True)
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="Line-smooth"))
    )
    return c


line_smooth().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure20.html")


def line_areastyle():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        )
        .add_yaxis(
            "商家B", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        )
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="Line-面积图"))
    )
    return c


line_areastyle().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure21.html")


def line_areastyle_boundary_gap():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_smooth=True)
        .add_yaxis("商家B", Faker.values(), is_smooth=True)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return c


line_areastyle_boundary_gap().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure22.html")


def line_yaxis_log():
    c = (
        Line()
        .add_xaxis(xaxis_data=["一", "二", "三", "四", "五", "六", "七", "八", "九"])
        .add_yaxis(
            "2 的指数",
            y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
        .add_yaxis(
            "3 的指数",
            y_axis=[1, 3, 9, 27, 81, 247, 741, 2223, 6669],
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                type_="log",
                name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,
            ),
            title_opts=opts.TitleOpts(title="Line-对数轴示例"),
        )
    )
    return c


line_yaxis_log().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure23.html")


def line_markpoint_markline():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max")]),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max")]),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Mark-Line-MarkPoint"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


line_markpoint_markline().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure24.html")


def line_itemstyle():
    c = (
        Line()
        .add_xaxis(xaxis_data=Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            symbol="triangle",
            symbol_size=20,
            linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=3, border_color="yellow", color="blue"
            ),
        )
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="Line-ItemStyle"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c


line_itemstyle().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure25.html")


def line_color_with_js_func():
    x_data = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    y_data = [393, 438, 485, 631, 689, 824, 987, 1000, 1100, 1200]

    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )

    c = (
        Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="注册总量",
            y_axis=y_data,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#fff", border_width=3
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(
                             title="OCTOBER 2015",
                             pos_bottom="5%",
                             pos_left="center",
                             title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
                         ),
                         xaxis_opts=opts.AxisOpts(
                             type_="category",
                             boundary_gap=False,
                             axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                             axisline_opts=opts.AxisLineOpts(is_show=False),
                             axistick_opts=opts.AxisTickOpts(
                                 is_show=True,
                                 length=25,
                                 linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                             ),
                             splitline_opts=opts.SplitLineOpts(
                                 is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                             ),
                         ),
                         yaxis_opts=opts.AxisOpts(
                             type_="value",
                             position="right",
                             axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                             axisline_opts=opts.AxisLineOpts(
                                 linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                             ),
                             axistick_opts=opts.AxisTickOpts(
                                 is_show=True,
                                 length=15,
                                 linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                             ),
                             splitline_opts=opts.SplitLineOpts(
                                 is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                             ),
                         ),
                         legend_opts=opts.LegendOpts(is_show=False),
            )

    )
    return c


line_color_with_js_func().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure26.html")