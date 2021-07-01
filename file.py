def file(event, context):
    f = open("demo1.txt", "w")
    for i in range(100000):
        line = "This is line %d \n" % i
        f.write(line)

    f.close()
    f = open("demo1.txt", "r")
    for i in range(100000):
        line = f.read()

    f.close()
   
    return "FILE OPERATION ENDs"
