import requests
from bs4 import BeautifulSoup
#import urllib
import urllib.request

def main(first_image, final_image):
    print('opteniendo url...')
    page_url = 'https://xkcd.com/'
    print('Descargando Imagenes desde la {}, hasta la {}...'.format(first_image, final_image))
    for idxImages in range(first_image, final_image):
        reponse = requests.get('{}{}/'.format(page_url, idxImages))
        soup = BeautifulSoup(reponse.content, 'html.parser')
        image_container = soup.find(id='comic')
        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('\t>>Descargando la imagen: {}.'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == '__main__':
    print('Inicializando Web Scraping...')
    first_image = 725
    final_image =736
    main(first_image, final_image)
