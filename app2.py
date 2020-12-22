from graph_rel.graph import graph
from graph_rel.word_rel import word_rel

# 需要绘图的数据集合
cols = ['law_details', 'justice_details', 'rule_details', 'dept_details', 'industry_details', 'party_details']
rel = word_rel(cols)
# 填充set并设置元素之间关系
rel.setSets().setIndex().setRels()
graph = graph()
size = []
# 该循环用于放大节点
for ele in rel.getRealSets():
    for e in ele['rel']:
        if e['to'] == ele['word']:
            size.append(e['num'] * 100)
# print(size)
# 设置节点
graph.add_nodes(rel.getSets())
# 设置边
graph.add_edges(rel.getRealSets())
# 绘图
graph.drawAndShow(size)