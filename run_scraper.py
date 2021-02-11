import requests
import shutil
import os
from bs4 import BeautifulSoup

RESOURCES_DIR = 'files'
URL = 'https://www.italianpod101.com/italian-word-lists'
FILE_PREFIX = 'Italian_Core'
CARDS_FILE = 'cards.txt'

def download_resource(url, filename):
    # Open the url, set stream to True, this will return the
    # stream content.
    r = requests.get(url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded file's
        # size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('File sucessfully Downloaded: ', filename)
    else:
        print('File Couldn\'t be retreived')

def write_to_file(arr):
    with open(CARDS_FILE, 'w') as f:
        for item in arr:
            f.write('__'.join(item) + '\n')

cards = []
index = 1

for p in range(1, 6):
    page = requests.get('{}/?page={}'.format(URL, p))
    soup = BeautifulSoup(page.content, 'html.parser')
    elems = soup.find_all('div', class_ = 'wlv-item__box')

    for elem in elems:
        imgSrc = elem.find('img', class_ = 'wlv-item__image')['src']
        audioWordSrc = elem.find('div', class_ = 'wlv-item__audio-box').find('audio')['src']
        word = elem.find('span', class_ = 'wlv-item__word').text
        wordEn = elem.find('span', class_ = 'wlv-item__english').text

        exampleBox = elem.find('div', class_ = 'wlv-item__sample')
        audioExampleSrc = example = exampleEn = ''
        if exampleBox:
            audioExampleSrc = exampleBox.find('audio')['src']
            example = exampleBox.find('span', class_ = 'wlv-item__word').text
            exampleEn = exampleBox.find('span', class_ = 'wlv-item__english').text

        os.chdir(RESOURCES_DIR)
        download_resource(imgSrc, '{}_{:02d}.jpg'.format(FILE_PREFIX, index))
        download_resource(audioWordSrc, '{}_{:02d}.mp3'.format(FILE_PREFIX, index))
        if bool(audioExampleSrc):
            download_resource(audioExampleSrc, '{}_{:02d}-example.mp3'.format(FILE_PREFIX, index))
        os.chdir('../')

        cards.append(['{:02d}'.format(index), word, example, wordEn, exampleEn, audioExampleSrc])
        index += 1

write_to_file(cards)
