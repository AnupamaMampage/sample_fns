import math
import random
import sys
from time import time

def randomTable(n):
    return [[math.floor(random.random() * 100) for i in range(n)] for j in range(n)]


def matrix(event, context):
    n=int(event['data'])
    matrixA = randomTable(n)
    matrixB = randomTable(n)
    start= time()
    matrixMult = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, len(matrixA)):
        for j in range(0, len(matrixB)):
            sum = 0
            for k in range(0, len(matrixA)):
                sum += matrixA[i][k] * matrixB[k][j]
            matrixMult[i][j] = sum
            
    latency= time()- start
    print matrixMult
    
    return latency

