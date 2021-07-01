import speedtest

# def main(event, context):
#   s = speedtest.Speedtest()
# #   print(dir(speedtest))
#   return (str(s.download()))

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def speed(event,context):
    # write to csv

    for i in range(3):
        print('Making test #{}'.format(i+1))
        d, u, p = test()
        print("Download: ",d)
        print("Upload: ", d)
        print("Ping: ", d)
        
     return str(d)



  

