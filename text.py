import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType


df = pd.read_excel('lagou_sj0624_113314.xlsx')
result=pd.value_counts(df['education'])
resulted=dict(result)
ed = list(resulted.keys())
edvalues = list(resulted.values())
edvaluesint=[]
for i in edvalues:
    edvaluesint.append(int(i))

result = pd.value_counts(df['education'])
resulted = dict(result)
ed = list(resulted.keys())
edvalues = list(resulted.values())
edvaluesint = []
for i in edvalues:
    edvaluesint.append(int(i))

from pyecharts import options as opts
from pyecharts.charts import Pie

c4 = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
        "",
        [list(z) for z in zip(ed, edvaluesint)],
        radius=["30%", "75%"],
        # 饼图的半径，数组的第一项是内半径，第二项是外半径
        center=["25%", "50%"],
        # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
        rosetype="radius",
        # 选择南丁格尔图类型，radius：扇区圆心角展现数据的百分比，半径展现数据的大小
        label_opts=opts.LabelOpts(is_show=False),
    )
        .add(
        "",
        [list(z) for z in zip(ed, edvaluesint)],
        radius=["30%", "75%"],
        center=["75%", "50%"],
        rosetype="area",  # 选择南丁格尔图类型，area：所有扇区圆心角相同，仅通过半径展现数据大小
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="学历要求"))
)
c4.render('学历饼图.html')
c4.render_notebook()