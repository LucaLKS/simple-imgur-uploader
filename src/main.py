import requests
from random import randint
import pyperclip

def read_file():
    print('Please insert image direcory:')
    dir = input('> ')

    file = open(dir, 'rb')
    return file.read()

def upload_image(i):
    print("Uploading...")

    url = 'https://api.imgur.com/3/image'
    payload = {'image': i}
    files = {}
    headers = {
      'Authorization': 'Client-ID ec61be071b16841'
    }

    response = requests.request('POST', url, headers = headers, data = payload, files = files)
    return response.json()['data']['link']

image = read_file()
link = upload_image(image)
pyperclip.copy(link)
print(f"Upload complete.\nLink: {link}\nLink copied to clipboard.")
