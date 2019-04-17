#!/usr/bin/python3

import re
import requests
import sys
from getopt import getopt
from bs4 import BeautifulSoup as bs

def extract(url, *args):
    response = request.get(url)
    if response.status_code != 200:
        raise('Could not pull from URL. Status code: %s' % response.status_code)
    soup = bs(response.text, 'html.parser')
    extraction = []
    for arg in args:
        if isinstance(arg, list):
            extraction.append(soup.select(arg[0])[arg[1])
        elif isinstance(arg, str):
            extraction.append(soup.select(arg))
        else:
            raise('Selectors must be formatted as str(selector) OR [str(selector), str(attr)]')
    return extraction


def getNovel():
    # TODO: Parse sys.argv options using getopt
    # TODO: Use novel's main page URL to get the rest of the neccessary information: latestChapter, baseURL, novelName, 
    response = request.get(url)
    soup = bs(response.text, 'html.parser')

    # Get latest chapter number
    # latestChapterHREF = soup.select('div.chapter-list > div.row > span > a:first-child')['href']
    latestChapterHREF = extract(url, ['div.chapter-list > div.row > span > a:first-child', 'href'], 
    ptn = re.compile('.*_([0-9]*)$')
    latestChapter = re.findall(ptn, latestChapterHREF)
    novelRange = range(1, latestChapter+1)

    # Get base chapter URL
    ptn = re.compile('(.*_)[0-9]*$')
    baseURL = re.findall(ptn, latestChapterHREF)

    # Get name of novel
    ptn = re.compile('/novel/(.*)$')
    novelName = re.findall(ptn, url)

    # Create/Truncate document
    fname = '%s_ch1-%i.txt' % (novelName, latestChapter)
    with open(fname, 'w') as f:
        f.write('=====\n%s\n======\n=====\n\n' % (novelName))

    # Get all chapters
    for i in novelRange:
        response = requests.get(url + str(i))
        soup = bs(response.text, 'html.parser')
        
        chapterName = soup.select('div.rdfa-breadcrumb > div > p').text
        chapter = '\n%s\n=======\n' % (chapterName) 
        
        textBody = soup.select('div.vung_doc > p')
        content = '\n'.join([p.text for p in textBody])
        chapter += content.replace(chr(160), ' ') + '\n'
        print('%s processed.' % (chapter))
        f = open(fname, 'a+')
        f.write(chapter)
        f.close()
    print('Task completed.')

if __name__ == '__main__':
    getNovel(sys.argv[1:])
