import speedtest

def main(event, context):
  s = speedtest.Speedtest()
#   print(dir(speedtest))
  return (s.download())
  

