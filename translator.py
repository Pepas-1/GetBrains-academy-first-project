import requests
from bs4 import BeautifulSoup
import argparse
import sys

source_lang=sys.argv[1].lower()
targ_lang=sys.argv[2].lower()
word=sys.argv[3].lower()

langs=['arabic','german','english','spanish','french','hebrew','japanese','dutch','polish','portuguese','romanian','russian','turkish']
target_lang=targ_lang if targ_lang in langs else langs[7]
req='https://context.reverso.net/translation/'+source_lang+'-'+target_lang
req+='/'+word.lower()
translate=requests.get(req, headers = {'User-Agent': 'Mozilla/5.0'})
soup=BeautifulSoup(translate.content,'html.parser')
checker=soup.find('span',{"class":"wide-container message no-iframe"})

if source_lang.lower() not in langs:
    print(f'Sorry, the program doesn\'t support {source_lang.lower()}')
elif targ_lang.lower() not in langs and not targ_lang=='all':
    print(f'Sorry, the program doesn\'t support {targ_lang.lower()}')
elif not checker == None:
    print(f'Sorry, unable to find {word}')
elif not translate.status_code==200:
    print('Something wrong with your internet connection')

else:
    #//////////
    file=open(f'{word}.txt','w')
    file.write('')
    file.close()
    #//////////
    if not targ_lang=='all':

        content=soup.find('div',{'id':'translations-content'})

        ans1=content.text.split()

        content=soup.find('section',{'id':'examples-content'})
        ans2=content.find_all('span',{'class':'text'})
        ans2=[i.text.strip() for i in ans2]
        # //////////
        file=open(f'{word}.txt','ab+')
        a=str('\n'+targ_lang.capitalize()+' Translations:')
        file.write((a+'\n').encode('utf-8'))
        # //////////
        for i in range(5):
            file.write((ans1[i]+'\n').encode('utf-8'))
        # //////////
        file.write(('\n'+targ_lang.capitalize()+' Examples:\n').encode())
        # //////////
        for i in range(0,10,2):
            file.write((ans2[i]+'\n'+ans2[i+1]+'\n').encode())
        # //////////
    else:
        langs.pop(langs.index(source_lang))
        # //////////
        for i in range(12):
            req = 'https://context.reverso.net/translation/' + source_lang + '-' + langs[i]
            req += '/' + word.lower()
            translate = requests.get(req, headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(translate.content, 'html.parser')
            content=soup.find('div',{'id':'translations-content'})
            ans_transl=content.find_next('a').text.strip().encode()
            ans1=content.text.split()
            content=soup.find('section',{'id':'examples-content'})
            ans2=content.find_all('span',{'class':'text'})
            ans2=[i.text.strip() for i in ans2]


            file = open(f'{word}.txt', 'ab+')
            file.write((('\n'+langs[i].capitalize()+' Translations:') + '\n').encode('utf-8'))
            file.write(ans_transl)
            file.write('\n'.encode('utf-8'))
            # //////////
            file.write(('\n' + langs[i].capitalize() + ' Example:\n').encode())
            file.write(ans2[0].encode('utf-8') + ':\n'.encode() + ans2[1].encode('utf-8') + '\n'.encode())
            # //////////
        file.close()


    file=open(f'{word}.txt','rb')
    for i in file:print(i.decode('utf-8').rstrip())