import urllib.request

def image(event, context):  
  image = str(event['data'])
  imgURL = "https://raw.githubusercontent.com/AnupamaMampage/images/main/" + image + ".jpg"
  urllib.request.urlretrieve(imgURL,"http://45.113.232.219/data" + image+ ".jpg")
  
  return "Image " + image + ".jpg saved"
  
