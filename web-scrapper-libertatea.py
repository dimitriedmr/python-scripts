#adevarul scrapping de articole
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urlparse

data_inceput='2020-3-16'
data_sfarsit='2020-5-14'
url = 'https://www.libertatea.ro'
cuvinteCheieLista = ['scoala','scoli','scolile','scolilor']

def queryListCreator():
    queryList = []
    for cuvatCheie in cuvinteCheieLista:
        #pentru fiecare cuvant de cautare imi creez 
        query = url + '/totul-despre/page/1?s=' + cuvatCheie
        paginaWebCautari = requests.get(query)
        soupPaginaWebCautari = BeautifulSoup(paginaWebCautari.text, "html.parser")
        nr_pagini_ul = soupPaginaWebCautari.find("ul",class_='pagination')
        if nr_pagini_ul is None:
            queryList.append(query)
            break
        nr_pagini = 3#int(nr_pagini_ul.find_all("span")[-1].text)
        for pagina in range(nr_pagini):
            queryList.append(url + '/totul-despre/page/' + str(pagina) + '?s=' + cuvatCheie)
            queryList.append(url + '/subiect/'+cuvatCheie+'/page/' + str(pagina))
    return queryList

def resultToStr(result):
    ret = ""
    if result:
        ret = result.text
    return ret

articoleGasite = set()

def cauta(queryList):
    index = 0
    numeFisier = urlparse(url).netloc[:-3] + '_' + cuvinteCheieLista[0] + '.csv'
    with open(numeFisier,'w', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        for query in queryList:
            paginaWebCautari = requests.get(query)
            soupPaginaWebCautari = BeautifulSoup(paginaWebCautari.text, "html.parser")
            listaArticole = soupPaginaWebCautari.find("ul",class_='articles-results-area')
            if listaArticole is not None:
                for linkArticol in listaArticole.find_all('a',class_="news-item", href=True):
                    paginaWebArticol = requests.get(linkArticol['href'])
                    if not paginaWebArticol:
                        break
                    soupPaginaWebArticol = BeautifulSoup(paginaWebArticol.text, "html.parser")
                    titluArticol = soupPaginaWebArticol.find('div',class_='title-container')
                    if not titluArticol:
                        break
                    titluArticol = titluArticol.find('h1')
                    titlu = resultToStr(titluArticol)
                    titlu = ' '.join(titlu.split())
                    
                    ziLunaAn = soupPaginaWebArticol.find("time",id='itemprop-datePublished')
                    ziLunaAn = ziLunaAn.contents[0]
                    data = ' '.join(ziLunaAn.split(', ')[1:])
                    lead = resultToStr(soupPaginaWebArticol.find("p",class_='intro'))
                    body = soupPaginaWebArticol.find("div",class_='article-body')
                    body = body.find_all("p")
                    continut = ""
                    for paragraph in body:
                        continut = continut + resultToStr(paragraph)
                    # scoate: space, tab, newline, return, formfeed si apoi le uneste folosind cate un spatiu
                    lead = ' '.join(lead.split())
                    continut = ' '.join(continut.split())

                    print(titlu)
                    if data in articoleGasite:
                        break
                    articoleGasite.add(data)

                    articol = lead + continut
                    index = index + 1
                    listaRand = [index,data,titlu,articol]
                    print(index)
                    writer.writerow(listaRand)

if __name__ == '__main__':
    queryList = queryListCreator()
    #for q in queryList:
    #    print(q)
    cauta(queryList)
    exit()