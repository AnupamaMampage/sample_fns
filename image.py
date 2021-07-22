from PIL import Image
import requests
from io import BytesIO
from time import time

def image(event, context):
  basewidth = 300
  url = 'https://raw.githubusercontent.com/AnupamaMampage/sample_fns/main/cat.jpg'
  start = time()
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  wpercent = (basewidth / float(img.size[0]))
  hsize = int((float(img.size[1]) * float(wpercent)))
  img = img.resize((basewidth, hsize), Image.ANTIALIAS)

  latency = time() - start
  
  return {"Latency: image: " latency}
