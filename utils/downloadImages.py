from configparser import ConfigParser
import requests
import os

config = ConfigParser()
readKey = config.read('apidata.config')

key = readKey["UNSPLASH"]["KEY"]

def download_unsplash_image(keyword, full_path, limit=5):
  response = requests.get(f'https://api.unsplash.com/search/photos/?query={keyword}&limit={limit}&orientation=landscape&client_id={key}', stream=True)

  print(keyword + ":", response.status_code)
  json = response.json()

  for i in range(limit):
    print(json['results'][i]['urls']['raw'])
    download_image(json['results'][i]['urls']['raw'], os.path.join(full_path, str(i) + ".jpg"))

def download_image(url, filename):
  response = requests.get(url, stream=True)

  print(response.status_code)

  if response.status_code == 200:
    with open(filename, 'wb') as file:
      for chunk in response.iter_content(1024):
        file.write(chunk)
  else:
    print(f"Unable to download image. HTTP response code: {response.status_code}")

  
if __name__ == "__main__":
  download_unsplash_image("cat", "out", 5)