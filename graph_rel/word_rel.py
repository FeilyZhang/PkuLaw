from mongodb.mongodb import mongodb

class word_rel:

    __db = 'pkulaw'
    __cols = None
    __sets = None
    __realSets = None
    __mongodb = None
    __indexs = None

    def __init__(self, cols):
        self.__mongodb = mongodb()
        self.__sets = list()
        self.__realSets = list()
        self.__indexs = list()
        self.__cols = cols

    def setSets(self):
        for col in self.__cols:
            for eles in self.__mongodb.find_all(self.__db, col):
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
        for col in self.__cols:
            for eles in self.__mongodb.find_all(self.__db, col):
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


