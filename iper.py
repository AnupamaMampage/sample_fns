import os
import numpy as np
import time
import iperf3
from time import time



def iper(event, context):
    # write to csv
    start = time()
    print ("Here")
    os.system('iperf3 -c 45.113.232.219')

    latency = time() - start
    return "iperf3: " + str(latency)
