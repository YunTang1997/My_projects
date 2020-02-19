# import pyecharts
from pyecharts.charts import Bar  # 画柱状图
from pyecharts import options as opts  # 设置标题
from pyecharts.globals import ThemeType  # 设置主题
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
# from pyecharts.charts import Page  # 顺序多图
# from pyecharts.globals import SymbolType
# from pyecharts.charts import Page, WordCloud
# from pyecharts.render import make_snapshot
# from snapshot_selenium import snapshot  # 渲染图片


bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 设置主题
bar.add_xaxis(['衬衫', '羊毛衫', '学纺纱', '裤子', '高跟鞋', '袜子'])
bar.add_yaxis('商家A', [5, 20, 36, 10, 75, 90])
bar.add_yaxis('商家B', [15, 6, 45, 20, 35, 66])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题'),
                    toolbox_opts=opts.ToolboxOpts(is_show=True),
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    visualmap_opts=opts.VisualMapOpts(is_show=True),
                    datazoom_opts=opts.DataZoomOpts(is_show=True))
bar.render(path='C:\\Users\\tangyun\\Desktop\\生成图像\\figure1.html')
# make_snapshot(snapshot, bar.render(), 'bar.png')


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis('商家A', Faker.values())
        .add_yaxis('商家B', Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例', subtitle='副标题'),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


bar_base().render(path='C:\\Users\\tangyun\\Desktop\\生成图像\\figure2.html')


def bar_border_radius():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), category_gap="60%")
        .set_series_opts(itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0, 160, 221)',
            }})
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-渐变圆柱"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


bar_border_radius().render(path='C:\\Users\\tangyun\\Desktop\\生成图像\\figure3.html')


def bar_border_radius_new():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_series_opts(itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0, 160, 221)',
            }})
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-渐变圆柱"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


bar_border_radius_new().render(path='C:\\Users\\tangyun\\Desktop\\生成图像\\figure4.html')


def bar_base_with_aimation() -> Bar():
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="elasticOut"
                )
            )
        )
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-动画配置基本示例", subtitle="副标题"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


bar_base_with_aimation().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure5.html")


def bar_base_with_custom_background_image() -> Bar():
    c = (
        Bar(
            init_opts=opts.InitOpts(
                bg_color={
                    "type": "pattern",
                    "image": JsCode("img"),
                    "repeat": "no-repeat",
                }
            )
        )
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(
                title="Bar-背景图基本示例",
                subtitle="副标题",
                title_textstyle_opts=opts.TextStyleOpts(color="White")
            )
        )
    )
    c.add_js_funcs(
        """
        var img = new Image(); 
        img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';
        """
    )
    return c


bar_base_with_custom_background_image().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure6.html")


def bar_reversal_axis() -> Bar():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY轴"))
    )
    return c


bar_reversal_axis().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure7.html")


def bar_stack0() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), stack="stack1")
        .add_yaxis("商家B", Faker.values(), stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    )
    return c


bar_stack0().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure8.html")


def bar_markpoint_type() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    return c


bar_markpoint_type().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure9.html")


def bar_markpoint_custom():
    x, y = Faker.choose(), Faker.values()
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis(
            "商家A", y,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
            ),
        )
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


bar_markpoint_custom().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure10.html")


def bar_markline_type():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（指定类型）"),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值"),
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    return c


bar_markline_type().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure11.html")


def bar_datazoom_slider_vertical() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(orient="vertical"),
        )
    )
    return c


bar_datazoom_slider_vertical().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure12.html")


def bar_datazoom_inside() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
        )
    )
    return c


bar_datazoom_inside().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure13.html")


def bar_histogram_color():
    x = Faker.dogs + Faker.animal
    xlen = len(x)
    y = []
    for idx, item in enumerate(x):
        if idx <= xlen / 2:
            y.append(
                opts.BarItem(
                    name=item,
                    value=(idx + 1) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#749f83"),
                )
            )
        else:
            y.append(
                opts.BarItem(
                    name=item,
                    value=(xlen + 1 - idx) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#d48265"),
                )
            )

    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("series0", y, category_gap=0, color=Faker.rand_color())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图（颜色区分）"))
        )
    return c


bar_histogram_color().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure14.html")






















