import os, time
import pickle
import random
import string
from random import gauss

def main(event, context):

    ip_file_name = "testi.txt"
    op_file_name = "testo.txt"
    ip_path = "kubeless/" + ip_file_name
    op_path  = "kubeless/" + op_file_name
    if os.path.exists(ip_path):
        for i in range(300000):
            os.system('sudo time dd if=ip_path of=op_path bs=8k count=300000')
    else:
        fi = open(ip_path, "wb")
        for i in range(1000):
            a1 = [gauss(1.5, 2) for i in range(10000)]
            pickle.dump(a1, fi)

        fi.close()

    return "echo END"
