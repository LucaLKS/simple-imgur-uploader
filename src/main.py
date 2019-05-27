# imports required modules
import requests
import pyperclip

# asks the user for a directory, then opens the file
# in binary mode and return the result
def read_file():
    print('Please insert image direcory:')
    dir = input('> ')

    file = open(dir, 'rb')
    return file.read()

# sends the request to the imgur api and returns the link of the uploaded image
# Accepts the image as an argoument
def upload_image(i):
    print("Uploading...")

    url = 'https://api.imgur.com/3/image'
    payload = {'image': i}
    headers = {
    #The Client ID is bound to your application. You can create one at: https://api.imgur.com/oauth2/addclient
      'Authorization': 'Client-ID ec61be071b16841'
    }

    response = requests.request('POST', url, headers = headers, data = payload)
    return response.json()['data']['link']


image = read_file()
link = upload_image(image)
#copies the link in the clipboard
pyperclip.copy(link)
print(f"Upload complete.\nLink: {link}\nLink copied to clipboard.")
