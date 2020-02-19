from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


words = [
    ("宝宝", 10000),
    ("我爱你哟", 6181),
    ("宝器", 4386),
    ("赖皮狗儿", 4055),
    ("要抱抱", 2467),
    ("I Love you", 2244),
    ("王莉琴", 1868),
    ("我的野蛮女友", 1484),
    ("蒙眼睛", 1112),
    ("八年", 865),
    ("好哄", 847),
    ("可爱", 582),
    ("宝藏女孩", 555),
    ("转转功", 550),
    ("乖", 462),
    ("王琴", 366),
    ("宝宝, 你摸, 这儿是空的", 360),
    ("爱撒娇", 282),
    ("转转洗鼻涕", 273),
    ("画个圈圈", 265),
    ("我有点疲倦", 233)
]

def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ARROW)
        .set_global_opts(title_opts=opts.TitleOpts(title="A gift for you!"),
                         toolbox_opts=opts.ToolboxOpts())
    )
    return c


wordcloud_base().render(path="C:\\Users\\tangyun\\Desktop\\figure.html")