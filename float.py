import time
from time import time
import math

def main(event, context):
  start=time()
#   n = int(event['data'])
  n = int(sys.argv[1])
  for i in range(0, n):
          sin_i = math.sin(i)
          cos_i = math.cos(i)
          sqrt_i = math.sqrt(i)
  latency = time()-start
  return str(latency)
