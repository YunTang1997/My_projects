from pyecharts.charts import EffectScatter  # 画涟漪特效散点图
from pyecharts import options as opts  # 设置标题
from pyecharts.globals import SymbolType
from pyecharts.faker import Faker


def effectscatter_base():
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
    return c


effectscatter_base().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure15.html")


def effectscatter_symbol():
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values(), symbol=SymbolType.ARROW)
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol"),
        )
    )
    return c


effectscatter_symbol().render(path="C:\\Users\\tangyun\\Desktop\\生成图像\\figure16.html")