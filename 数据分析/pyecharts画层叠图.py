from pyecharts.charts import Bar  # 画柱状图
from pyecharts.charts import Line  # 画折线图
from pyecharts import options as opts  # 设置标题
from pyecharts.faker import Faker


def over_line_scatter():
    x = Faker.choose()
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="Overlap-line+scatter")
        )
    )
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
    )
    bar.overlap(line)
    return bar


over_line_scatter().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure30.html")


def overlap_bar_line():
    bar = (
        Bar()
        .add_xaxis(Faker.months)
        .add_yaxis("蒸发量", Faker.values())
        .add_yaxis("降水量", Faker.values())
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="Overlap-bar+line（双 Y 轴）"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} m1")
            ),
        )
    )
    line = (
        Line()
        .add_xaxis(Faker.months)
        .add_yaxis("平均温度", Faker.values(), yaxis_index=1)
        )
    bar.overlap(line)
    return bar


overlap_bar_line().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure31.html")