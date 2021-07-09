import os
import numpy as np
import time
import iperf3
from time import time



def iperf3(event, context):
    # write to csv
    start = time()
    os.system('sudo iperf3 -c 45.113.232.219')

    latency = time() - start
    return "iperf3: " + str(latency)
