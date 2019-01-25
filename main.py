for i in novelRange:
    f = open('World Teacher (Prologue-Chapter 130)', 'a+')
    response = requests.get(url + str(i))
    soup = bs(response.text, 'html.parser')
    ch = soup.select('span["itemprop"="title"]')[-1].text
    novel = '\n%s\n=======\n' % (ch) 
    vung_doc_p = soup.select('div.vung_doc > p')
    content = '\n'.join([p.text for p in vung_doc_p])
    novel += content.replace(chr(160), ' ') + '\n'
    print('Chapter %s processed.' % (str(i)))
    f.write(novel)
    f.close()

