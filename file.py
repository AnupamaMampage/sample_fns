import numpy as np
from random import gauss

def file(event, context):
    a1 = [gauss(1.5, 2) for i in range(10000000)]
    import pickle
    pkl_file = open("serialized_data3.pkl", 'wb')

    pickle.dump(a1, pkl_file)
    return "FILE OPERATION ENDs"
