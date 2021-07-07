from random import gauss
import pickle
import os
import random
import string

def file(event, context):
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(10))
    path = "kubeless/"+ file_name
    fi = open(path, "wb")
    for i in range(1000):
        a1 = [gauss(1.5, 2) for i in range(7500)]
        pickle.dump(a1, fi)

#     fi.close()
#     fo = open(path, "rb")
#     for i in range(750):
#         a2 = pickle.load(fo)

    fo.close()
    if os.path.exists(path):
        os.remove(path)    
   
    return "FILE OPERATION ENDs"
