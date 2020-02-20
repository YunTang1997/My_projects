import random
import math
from pyecharts.charts import Bar3D
from pyecharts.charts import Line3D
from pyecharts.charts import Scatter3D
from pyecharts.charts import Surface3D
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar3d_base():
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            visualmap_opts=opts.VisualMapOpts(max_=20),
            title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
        )
    )
    return c


bar3d_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure41.html")

def generate_date():
    data = [[j, k, random.randint(0, 9) * 2 + 4] for j in range(10) for k in range(10)]
    return data

def bar3d_stack():
    x_data = y_data = list(range(10))
    bar3d = Bar3D()
    for _ in range(10):
        bar3d.add(
            "",
            generate_date(),
            shading="lambert",
            xaxis3d_opts=opts.Axis3DOpts(data=x_data, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(data=y_data, type_="value"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
    bar3d.set_global_opts(title_opts=opts.TitleOpts("Bar3D-堆叠柱状图示例"))
    bar3d.set_series_opts(**{"stack": "stack"})
    return bar3d

bar3d_stack().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure42.html")


def line3d_base():
    data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        data.append([x, y, z])
    c = (
        Line3D()
        .add(
            "",
            data,
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
            grid3d_opts=opts.Grid3DOpts(
                width=100, height=100, depth=100, rotate_speed=150, is_rotate=True
            ),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=30, min_=0, range_color=Faker.visual_color
            ),
            title_opts=opts.TitleOpts(title="Line3D-旋转的弹簧"),
        )
    )
    return c


line3d_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure43.html")


def scatter3d_base():
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            title_opts=opts.TitleOpts("Scatter3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color),
        )
    )
    return c


scatter3d_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure44.html")


def surface3d_base():
    def surface3d_data():
        for t0 in range(-60, 60, 1):
            y = t0 / 60
            for t1 in range(-60, 60, 1):
                x = t1 / 60
                if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                    z = "-"
                else:
                    z = math.sin(x * math.pi) * math.sin(y * math.pi)
                yield [x, y, z]

    c = (
        Surface3D()
        .add(
            "",
            list(surface3d_data()),
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Surface3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(
                max_=3, min_=-3, range_color=Faker.visual_color
            ),
        )
    )
    return c


surface3d_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure45.html")


def surface3d_flower():
    def surface3d_data():
        for t0 in range(-30, 30, 1):
            y = t0 / 10
            for t1 in range(-30, 30, 1):
                x = t1 / 10
                z = math.sin(x * x + y * y) * x / 3.14
                yield [x, y, z]

    c = (
        Surface3D()
        .add(
            "",
            list(surface3d_data()),
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Surface3D-曲面波图"),
            visualmap_opts=opts.VisualMapOpts(
                max_=1, min_=-1, range_color=Faker.visual_color
            ),
        )
    )
    return c


surface3d_flower().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure46.html")