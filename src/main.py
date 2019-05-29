# imports required modules
import requests
import pyperclip
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', help="Directory of the image to upload.")
    args = parser.parse_args()

    if args.directory == None:  # If no directory is passed as argument calls the func
        args.directory = prompt_user()

    image = read_file(args.directory)
    link = upload_image(image)
    pyperclip.copy(link)  # copies the link in the clipboard
    print(f"Upload complete.\nLink: {link}\nLink copied to clipboard.")


def prompt_user():
    """asks the user for a directory"""
    print('Please insert image direcory:')
    inpt = input('> ')
    return inpt


def read_file(dir):
    """opens the file in binary mode and return the result"""
    file = open(dir, 'rb')
    return file.read()


def upload_image(i):
    """sends the request to the imgur api and returns the link of the uploaded image
    accepts the image as an argoument"""
    print("Uploading...")

    url = 'https://api.imgur.com/3/image'
    payload = {'image': i}
    headers = {
        # The Client ID is bound to your application. You can create one at:
        # https://api.imgur.com/oauth2/addclient
        'Authorization': 'Client-ID ec61be071b16841'
    }

    response = requests.request('POST', url, headers=headers, data=payload)
    return response.json()['data']['link']


if __name__ == '__main__':
    """Works only if this isn't imported"""
    main()
