from random import gauss

def file(event, context):
    f = open("kubeless/demo1.txt", "w")
    for i in range(10000):
        a1 = [gauss(1.5, 2) for i in range(1000000)]
        f.write(str(a1)+"\n")

    f.close()
    f = open("kubeless/demo1.txt", "r")
    for i in range(10000):
        a2 = f.read()

    f.close()
   
    return "FILE OPERATION ENDs"
