# coding=utf-8
__author__ = 'Андрей'

import time


def printTime(t1, t2):
    print 'Time: %s sec' % (t2 - t1)

t = 0
x = 0
time1 = time.clock()
X = [i for i in range(0, 100000)]
time2 = time.clock()
printTime(time1, time2)
while X:
    front, X = X[0], X[1:]
    if front % 1000 == 0:
        time1, time2 = time2, time.clock()
        printTime(time1, time2)
