from itertools import chain, combinations


def createRemovelist(elem, listIN):
    return tuple(filter(lambda x: x != elem, listIN))


class Endfromthrough:
    def __init__(self, name):
        self.name = name

    def addCost_Parent(self, cost, parent):
        self.cost = cost
        self.parent = parent


class Graph:
    allroute = {}

    def addElem(self, elem):
        if isinstance(elem, Endfromthrough) and elem.name not in self.allroute:
            self.allroute[elem.name] = elem

    def travelsales(self, start):
        d = len(self.tab)
        dlist = []
        for i in range(0, d):
            if i != start:
                dlist.append(i)

        dpowerset = powerset(dlist)

        combineSet = []
        for i in range(d-1):
            for j in range(len(dpowerset)):
                if dlist[i] not in dpowerset[j]:
                    combineSet.append([dlist[i], dpowerset[j]])
        combineSet.sort(key=lambda x: len(x[1]))
        for i in range(len(combineSet)):
            combineSetTuple = tuple(combineSet[i])
            self.allroute[combineSetTuple] = Endfromthrough(combineSetTuple)

        for key, value in self.allroute.items():
            if len(key[1]) == 0:
                value.cost = self.tab[start][key[0]]
                value.parent = start
            else:
                compareVal = []
                parentPrevious = []
                for i in range(len(key[1])):
                    for previousPoint in key[1]:
                        val = self.tab[previousPoint][key[0]]
                        at = tuple(
                            [previousPoint, createRemovelist(previousPoint, key[1])])
                        val += self.allroute[at].cost

                        compareVal.append(val)
                        parentPrevious.append(previousPoint)
                value.cost = min(compareVal)
                value.parent = parentPrevious[compareVal.index(value.cost)]

    def addMatrix(self, tab):
        self.tab = tab

    def check_print(self):
        print("\t", "cost", "parent")
        for key, val in self.allroute.items():
            print(key, val.cost, val.parent)


def powerset(iterate):
    s = list(iterate)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


tab = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10, 4, 8, 0]]


g = Graph()
g.addMatrix(tab)
g.travelsales(0)
g.check_print()
