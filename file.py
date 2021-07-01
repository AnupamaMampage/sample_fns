def file(event, context):
    f = open("demo1.txt", "w")
    for i in range(100):
        f.write("This is line ", i)

    f.close()
    f = open("demo1.txt", "r")
    for i in range(100):
        line = f.read()
    
    f.close()
    return "FILE OPERATION ENDs"
