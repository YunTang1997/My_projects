from pyecharts.charts import Scatter  # 画散点图
from pyecharts import options as opts  # 设置标题
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode


def scatter_base():
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            title_opts=opts.TitleOpts(title="Scatter-基本示例"),
            visualmap_opts=opts.VisualMapOpts(max_=150),
        )
    )
    return c


scatter_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure27.html")


def scatter_visualmap_color():
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
        )
    )
    return c


scatter_visualmap_color().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure28.html")



def scatter_muti_diemnsion_data():
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            [list(z) for z in zip(Faker.values(), Faker.choose())],
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    "function (params) {return params.value[1] +' : '+ params.value[2];}"
                )
            ),
        )
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function (params) {return params.name +' : ' +params.value[2];}"
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                type_="color", max_=150, min_=20, dimension=1
            ),
        )
    )
    return c


scatter_muti_diemnsion_data().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure29.html")