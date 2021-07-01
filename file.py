def file(event, context):
    f = open("kubeless/demo1.txt", "w")
    for i in range(1000000):
        line = "This is line %d \n" % i
        f.write(line)

    f.close()
    f = open("kubeless/demo1.txt", "r")
    for i in range(1000000):
        line = f.read()

    f.close()
   
    return "FILE OPERATION ENDs"
