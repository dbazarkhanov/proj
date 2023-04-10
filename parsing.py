import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


class parse:
    def __init__(self, url_temp, tag, cls):
        self.tag = tag
        self.class_ = cls
        self.response = requests.get(url_temp)
        self.soup = bs(self.response.text, 'html.parser')

    def find(self, atr):
        if atr != '':
            return [url + i[atr] for i in self.soup.find_all(self.tag, class_=self.class_)]
        else:
            for i in self.soup.find_all(self.tag, class_=self.class_):
                return i.text


url = 'https://krisha.kz/'
city = 'prodazha/kvartiry/' + (input('City: ')).lower() + '/?page=' + input('Page: ')
links = pars(url + city, 'a', 'a-card__title').find('href')

descriptions = [pars(links[i], 'div', 'a-text a-text-white-spaces').find('') for i in range(len(links))]
# pd.set_option('display.max_colwidth', None)
df = pd.DataFrame({'links': links, 'description': descriptions})
print(df)
