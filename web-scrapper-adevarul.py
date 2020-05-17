#adevarul scrapping de articole
import unidecode
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urlparse
import dateFix


data_inceput='2020-3-16'
data_sfarsit='2020-5-14'
url = 'https://adevarul.ro'
cuvinteCheieLista = ['scoala','scoli','scolile','scolilor']

def queryListCreator():
    queryList = []
    for cuvatCheie in cuvinteCheieLista:
        #pentru fiecare cuvant de cautare imi creez 
        query = url + '/cauta/?terms=' + cuvatCheie + '&fromDate=' + data_inceput + '&toDate=' + data_sfarsit + '&tab=mrarticle&page=1'
        paginaWebCautari = requests.get(query)
        soupPaginaWebCautari = BeautifulSoup(paginaWebCautari.text, "html.parser")
        nr_pagini_ul = soupPaginaWebCautari.find("ul",class_='page-no')
        if nr_pagini_ul is None:
            queryList.append(query)
            break
        nr_pagini = int(nr_pagini_ul.find_all("a")[-1].text)
        for pagina in range(nr_pagini):
            queryList.append(query[:-1] + str(pagina+1))
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
        writer = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
        listaRand = ["nr. crt.","data","link","titlu","articol"]
        writer.writerow(listaRand)
        for query in queryList:
            paginaWebCautari = requests.get(query)
            soupPaginaWebCautari = BeautifulSoup(paginaWebCautari.text, "html.parser")
            listaArticole = soupPaginaWebCautari.find("ul",class_='article-list')
            for listaElemente in listaArticole.find_all('li'):
                linkArticol = listaElemente.find('a', href=True)
                if not linkArticol:
                    break
                paginaWebURL = url + linkArticol['href']
                paginaWebArticol = requests.get(paginaWebURL)
                if not paginaWebArticol:
                    break
                soupPaginaWebArticol = BeautifulSoup(paginaWebArticol.text, "html.parser")
                continutArticol = soupPaginaWebArticol.find("div",class_='article-content')
                if not continutArticol:
                    break
                
                titlu = resultToStr(linkArticol)
                titlu = ' '.join(titlu.split())
                ziLunaAn = resultToStr(listaElemente.find("span",class_='time'))
                data = ' '.join(re.findall(r"\d+:\d+|\w+",ziLunaAn))
                    
                data = dateFix.convertesteLuna(data)
                if not data:
                    break
                    
                lead = resultToStr(continutArticol.find("h2",class_='articleOpening'))
                body = resultToStr(continutArticol.find("div",class_='article-body'))
                # scoate: space, tab, newline, return, formfeed si apoi le uneste folosind cate un spatiu
                lead = ' '.join(lead.split())
                body = ' '.join(body.split())
                
                if paginaWebURL in articoleGasite:
                    break
                articoleGasite.add(paginaWebURL)
                
                articol = lead + body
                index = index + 1
                
                titlu = unidecode.unidecode(titlu)
                articol = unidecode.unidecode(articol)
                
                titlu = titlu.replace(',,', '\"')
                articol = articol.replace(',,', '\"')
                
                print(titlu)
                listaRand = [index,data,paginaWebURL,titlu,articol]
                print(index)

                writer.writerow(listaRand)


if __name__ == '__main__':
    queryList = queryListCreator()
    #for q in queryList:
    #    print(q)
    cauta(queryList)
    exit()