from mongodb import mongodb
from graph import graph

class word_rel:

    __db = 'pkulaw'
    __col = 'dept_detail'
    __sets = None
    __realSets = None
    __mongodb = None
    __indexs = None

    def __init__(self):
        self.__mongodb = mongodb()
        self.__sets = list()
        self.__realSets = list()
        self.__indexs = list()

    def setSets(self):
        for eles in self.__mongodb.find_all(self.__db, self.__col):
            for ele in eles['dept']:
                if ele not in self.__sets:
                    self.__sets.append(ele)
                    self.__realSets.append({
                        'word' : ele,
                        'rel' : [{
                            'to' : -1,
                            'num' : -1
                        }]
                    })
        return self

    def getSets(self):
        return self.__sets

    def getRealSets(self):
        return self.__realSets

    def setIndex(self):
        for eles in self.__mongodb.find_all(self.__db, self.__col):
            index = []
            for ele in eles['dept']:
                index.append(self.__sets.index(ele))
            self.__indexs.append(index)
        return self

    def getIndexs(self):
        return self.__indexs

    def setRels(self):
        for eles in self.__indexs:
            for ele in eles:
                temp = self.deepCopy(eles)
                for ele1 in temp:
                    num = 1
                    for e in self.__realSets[ele]['rel']:
                        if e['to'] == ele1:
                            num = e['num'] + 1
                            self.__realSets[ele]['rel'].remove(e)
                            break
                    self.__realSets[ele]['rel'].append({
                        'to' : ele1,
                        'num' : num
                    });
        for ele in self.__realSets:
            ele['rel'].pop(0)
        for ele in self.__realSets:
            for e in ele['rel']:
                e['to'] = self.__sets[e['to']]

    def map(self):
        for ele in self.__realSets:
            line = ele['word']
            for e in ele['rel']:
                line += ', {to = ' + self.__sets[e['to']] + ', num = ' + str(e['num']) + '}'
            print(line)
            line = ''


    def deepCopy(self, lst):
        target = list()
        for ele in lst:
            target.append(ele)
        return target


rel = word_rel()
rel.setSets().setIndex()
#print(rel.getSets())
rel.setRels()
print(rel.getSets())
for ele in rel.getRealSets():
    print(ele)

rel = word_rel()
rel.setSets().setIndex().setRels()
graph = graph()
size = []
for ele in rel.getRealSets():
    for e in ele['rel']:
        if e['to'] == ele['word']:
            size.append(e['num'] * 100)
print(size)
graph.add_nodes(rel.getSets())
graph.add_edges(rel.getRealSets())
graph.drawAndShow(size)


