from random import gauss

def file(event, context):
    fi = open("kubeless/demo1.txt", "wb")
    for i in range(1000):
        a1 = [gauss(1.5, 2) for i in range(10000)]
        pickle.dump(a1, fi)

    fi.close()
    fo = open("kubeless/demo1.txt", "rb")
    for i in range(1000):
        a2 = pickle.load(fo)

    fo.close()
   
    return "FILE OPERATION ENDs"
