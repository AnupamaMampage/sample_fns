import speedtest
import speedtest-cli

def main(event, context):
  s = speedtest.Speedtest()
#   print(dir(speedtest))
  return (s.download())
  

