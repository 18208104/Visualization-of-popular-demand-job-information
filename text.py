import pandas as pd
import jieba
import jieba.analyse
from pyecharts import options as opts
from pyecharts.charts import Pie, WordCloud
from pyecharts.globals import  SymbolType,ThemeType

#融资饼图
def setrose():
    df = pd.read_csv('金融阶段.csv')
    # 除去无用数据
    df = df[~df['financeStage'].str.contains('financeStage')]

    result = pd.value_counts(df['financeStage'])
    resulted = dict(result)
    ed = list(resulted.keys())
    edvalues = list(resulted.values())
    edvaluesint = []
    for i in edvalues:
        edvaluesint.append(int(i))

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add(
            "",
            [list(z) for z in zip(ed, edvaluesint)],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            rosetype="area",  # 选择南丁格尔图类型，area：所有扇区圆心角相同，仅通过半径展现数据大小
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="金融阶段饼图"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_left="80%", orient="vertical", pos_top="5%"
            ),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render('financeStage.html')
    c.render_notebook()

#技能词云
def setword1():
    df = pd.read_csv('要求技能.csv')
    needs = []
    for i in df['thirdType']:
        needs.append(i)

    set_need = str(needs).replace('|', " ")

    # 设置停止词，删除无关的词
    stopwords = [ '内容', '销售', '助理', '其他', '商务', '产品', '经理', '售后', '职能', '职位', '视觉', '主管', '管理', '项目',
                 '运营','广告投放','广告','编辑','顾问','客服','视频','保险','业务','清算','音频','电话','大客户','代表','网店','抖音','主播',
                 '行政','专员','看看','技术','总监','前台','用户','普工','操作工','企业','理财','软件','全栈','招聘','在线','新媒体','媒体','审核'
                  ,'出纳','市场推广','拓展','文案','市场','营销','推广','售前','人事','技术支持','渠道','市场营销','项目管理','项目经理','媒介','客户'
                  ,'财务','客户经理','培训']
    jieba_need = jieba.analyse.extract_tags(set_need, topK=80, withWeight=True)
    jieba_result = []
    for i in jieba_need:
        if i[0] not in stopwords:
            jieba_result.append(i)

    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", jieba_result, word_size_range=[20, 100], shape=SymbolType.RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="技能词云"))
    )
    c.render('skill.html')
    c.render_notebook()



#福利词云
def setword2():
    df = pd.read_csv('福利待遇.csv')
    needs = []
    for i in df['positionAdvantage']:
        needs.append(i)

    set_need = str(needs).replace(',', " ").replace('、', " ").replace('/', " ").replace('"'," ")\
        .replace(';', " ").replace('&amp', " ").replace('n', " ").replace('ice', "nice")

    # 设置停止词，删除无关的词
    stopwords = ['互联网', '大型', '公司的', '+', '综合', '管理', '行业', '提供', '统招', '提供', '来一起玩吗', '独角兽', '补充', '无责', '想搞钱的你就来', '世界',
                 '看看' ]
    jieba_need = jieba.analyse.extract_tags(set_need, topK=80, withWeight=True)
    jieba_result = []
    for i in jieba_need:
        if i[0] not in stopwords:
            jieba_result.append(i)

    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", jieba_result, word_size_range=[20, 100], shape=SymbolType.RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="福利待遇词云"))
    )
    c.render('positionAdvantage.html')
    c.render_notebook()

if __name__ == '__main__':
    setword1()
    setword2()
    setrose()

