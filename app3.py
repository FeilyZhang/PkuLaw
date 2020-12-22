# coding:utf-8
import jieba.analyse
from mongodb.mongodb import mongodb
from graph_rel.graph import graph
from graph_rel.word_rel import word_rel
from pyecharts import options as opts
from pyecharts.charts import Line, WordCloud
from pyecharts.globals import SymbolType

'''
解析HTML文本
'''
def getContent(str):
    num = 0
    rst = ''
    for e in str:
        if e == '<':
            num += 1
        elif e == '>':
            num -= 1
        elif num == 0:
            rst += e
    return rst

'''
读取本级目录下新冠肺炎词库
'''
def readCSV(file):
    with open(file, 'r', encoding='UTF-8') as f:
        return f.read()


ret = readCSV('dict.txt')
s = []
for ele in ret.split('\n'):
    s.append(ele)

'''
抽取并按月份合并关键词
'''
cols = ['law_detail', 'justice_detail', 'rule_detail', 'dept_detail', 'industry_detail', 'party_detail']
rst = [[], [], [], [], [], [], [], [], [], [], [], []]
dic = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
for i in range(0, len(cols)):
    for ele in mongodb().find_all('pkulaw', cols[i]):
        # 以下循环用于简化12个条件分支
        for j in range(0, 12):
            if ele['pub_date'] != '' and int(ele['pub_date'].split('.')[1]) > j  and int(ele['pub_date'].split('.')[1]) < j + 2 and int(ele['pub_date'].split('.')[2]) < 50:
                for e in jieba.analyse.extract_tags(getContent(str(ele['content'][0])) , topK=30, withWeight=False, allowPOS=()):
                    if e in s:
                        rst[j].append(e)
'''
按月份统计词频
'''
for i in range(0, len(rst)):
    for e in rst[i]:
        if e not in dic[i].keys():
            dic[i][e] = 1
        else:
            dic[i][e] += 1
'''
按月份输出词频
'''
for i in range(0, len(dic)):
    print(str(i + 1) + '月份' + str(sorted(dic[i].items(),key=lambda x:x[1],reverse=True)))


'''
绘制词云图
'''
size = []
for d in range(0, len(dic)):
    r = []
    for ele in dic[d].keys():
        r.append((ele, dic[d][ele]))
    c = (
        WordCloud()
        .add("", r, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title=str(int(d + 1)) + "月关键词"))
        .render('templates/' + str(int(d + 1)) + ".html")
    )
    size.append(len(r))

'''
绘制折线图
'''
attr =["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月"]
c = (
    Line()
    .add_xaxis(attr)
    .add_yaxis("关键词", size[0 : len(size) - 1], is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="2020年1月 - 11月COVID-19官方文本关键词统计", subtitle="算法：TF-IDF / 词库：COVID-19自定义词库"))
    .render("templates/line.html")
)