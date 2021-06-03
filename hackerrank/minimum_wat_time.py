#!/bin/python3

import os
import sys
import heapq
from collections import defaultdict
#
# Complete the minimumAverage function below.
#
def minimumAverage(customers):
    arrival_dict = defaultdict(lambda:{'index':0,'time':[]})
    customers.sort()
    for i in customers:
        # arrival_dict[i[1]]['index'] = 0
        arrival_dict[i[1]]['time'].append(i[0])
    wait = 0
    time = 0
    idx = 0
    heap = []
    for i in range(n):
        while idx < n and customers[idx][0] <= time:
            heapq.heappush(heap, customers[idx][1])
            idx += 1
        if len(heap) == 0:
            heapq.heappush(heap, customers[idx][1])
            idx += 1
        p_time = heapq.heappop(heap)
        index = arrival_dict[p_time]['index']
        a_time = arrival_dict[p_time]['time'][index]
        arrival_dict[p_time]['index'] += 1
        # print(p_time, a_time)
        wait += max(time-a_time, 0) + p_time
        time += max(a_time-time, 0) + p_time
    return wait//n

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
