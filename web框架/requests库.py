import requests
url='https://zhengxin-pub.cdn.bcebos.com/mark/09f76c1c4588640d61f1b3c4686c257d_fullsize.jpeg'
response = requests.get(url)
if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print('Image saved successfully.')
else:
    print('Failed to download image.')