from collections import namedtuple
import random
import queue as Queue
Bag = namedtuple("Bag", ['id', 'value', 'weight', 'mq', 'crop'])

Kind = namedtuple("Kind", ['id', 'value_mq', 'weight_mq', 'crop'])

MAX_KIND = 3
MAX_BAGS_PER_KIND = 10
MAX_VALUE_MQ = 15
MAX_WEIGHT_MQ = 7
MAX_MQ = 250
MIN_MQ = 50

kinds = []
bags = []

def gen_kinds(plants):
    dictKinds = {}
    for p in plants:
        dictKinds[p] = random.randint(1, MAX_KIND)

    
    for k in dictKinds:
        for i in range(dictKinds[k]):
            kinds.append(Kind(k+str(i), random.randint(7, MAX_VALUE_MQ), random.randint(1, MAX_WEIGHT_MQ), k))

def gen_Bags():
    for k in kinds:
        nbags= random.randint(10, MAX_BAGS_PER_KIND)
        for n in range(nbags):
            mq = random.randint(MIN_MQ, MAX_MQ)
            bags.append(Bag(k.id, (k.value_mq)*mq, (k.weight_mq)*mq, mq, k.crop))


class Node:
    def __init__(self, level, value, weight, bound, contains):
         self.level = level
         self.value = value
         self.weight = weight
         self.bound = bound
         self.contains = contains


def upper_bound(u, k, n, v, w):
        if u.weight > k:
            return 0
        else:
            bound = u.value
            wt = u.weight
            j = u.level 
            while j < n and wt + w[j] <= k:
                bound += v[j]
                wt += w[j]
                j += 1
            if j < n:
                bound += (k - wt) * float(v[j])/ w[j]
            return bound
        

def knapsack(items, capacity, terr):
        def mqCheck(n):
            app_terr = terr.copy()
            for c in n.contains:
                app_terr[items[c-1].crop]-=items[c-1].mq
                if app_terr[items[c-1].crop]<0:
                    return False
            return True
        def isGoal(n):
            goal=False
            if n.weight <= capacity and mqCheck(n):
                goal = True
            return goal

        item_count = len(items)
        v = [0]*item_count
        w = [0]*item_count
        # sort items by value to weight ratio
        items = sorted(items, key=lambda k: float(k.value)/k.weight, reverse = True)
        for i,item in enumerate(items, 0):
            v[i] = int(item.value)
            w[i] = int(item.weight)
        q = Queue.Queue()
        root = Node(0, 0, 0, 0.0,[])
        root.bound = upper_bound(root, capacity, item_count, v, w)
        q.put(root)
        value = 0
        taken = [0]*item_count
        best = set()
        while not q.empty():
            c = q.get()
            if c.bound > value:
                level = c.level+1
            left = Node(level,c.value + v[level-1], c.weight + w[level-1], 0.0, c.contains[:])
            left.bound = upper_bound(left, capacity, item_count, v, w)
            left.contains.append(level)
            if isGoal(left):
                if left.value > value:
                    value = left.value
                    best = set(left.contains)
                if left.bound > value:
                    q.put(left)
            right = Node(level,c.value, c.weight, 0.0, c.contains[:])
            right.bound = upper_bound(right, capacity, item_count, v, w)
            if isGoal(right):
                if right.value > value:
                    value = right.value
                    best = set(right.contains)
                if right.bound > value:
                    q.put(right)
        for b in best:
            taken[b-1] = 1
        value = sum([i*j for (i,j) in zip(v,taken)])
        weight = sum([i*j for (i,j) in zip(w,taken)])
        return value, weight, zip(items ,taken)


