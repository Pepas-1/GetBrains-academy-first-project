import requests
from bs4 import BeautifulSoup
import re
import os
page_n=int(input())
page_types=input()
ans_list=[]
url='https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=1'
for i in range(page_n):
    dir_name='page_'+str(i+1)
    os.mkdir(dir_name)
    url=url[0:-1]+str(i+1)
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html.parser')
    spans = soup.find_all('span', string=page_types)
    articles = [i.find_parent('article') for i in spans]
    links = [link.find('a').get('href') for link in articles]
    names = [j.find('h3', {'itemprop': "name headline"}) for j in articles]
    os.chdir(os.path.join(os.getcwd(),dir_name))

    for j in range(len(names)):
        file_name = names[j].text.strip().replace(' ', '_')
        file_name = re.sub((r'[!-.,:?]'), '', file_name)
        file_name = file_name+'.txt'
        file = open(file_name, 'wb')
        page_req = requests.get('https://www.nature.com' + links[j])
        soup1 = BeautifulSoup(page_req.content, 'html.parser')
        dirty_text = (soup1.find('div', {'class': 'c-article-body u-clearfix'}))
        clean_text = dirty_text.text
        file.write(clean_text.encode())
        file.close()
        ans_list.append(file_name)
    os.chdir(os.path.dirname(os.getcwd()))
