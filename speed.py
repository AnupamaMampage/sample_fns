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
    d = res["download"]
    u = res["upload"]
    p = res["ping"]
    
    return "d: " + str(d) + "u: " + str(u) + "p: " + str(p)


def speed(event,context):
    # write to csv
    d, u, p = 0
    result = np.zeros(3)
    for i in range(3):
        print('Making test #{}'.format(i+1))
        result[i] = test()
        
        
    return result


  

