import speedtest

def main(event, context):
  s = speedtest.Speedtest()
  return('My download speed is:', s.download())
