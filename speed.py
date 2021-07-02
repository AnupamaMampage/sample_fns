import speedtest
import numpy as  np

# def main(event, context):
#   s = speedtest.Speedtest()
# #   print(dir(speedtest))
#   return (str(s.download()))

def test():
    s = speedtest.Speedtest()
#     s.get_servers()
#     s.get_best_server()
#     s.download()
#     s.upload()
#     res = s.results.dict()
#     d = res["download"]
#     u = res["upload"]
#     p = res["ping"]
    
    return (str(s.download()))

def speed(event,context):
    # write to csv
    
    result = np.zeros(3)
    for i in range(3):
        print('Making test #{}'.format(i+1))
        result[i] = test()
        print(result[i])
        
        
    return "Test Completed"


  

