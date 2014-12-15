import urllib2
from bs4 import BeautifulSoup
for i in range(65):
    year=i+1950
    print 'Year data in process: '+str(year)
    year_check=int(year)
    request=urllib2.Request('http://www.formula1.com/results/driver/'+str(year))
    opener=urllib2.build_opener()
    source=opener.open(request)
    data=source.read()
    soup=BeautifulSoup(data)
    soup.prettify()
    table=soup.find('table')
    fout=open('F1 '+str(year)+' Driver points.txt','w')
    col=0
    if(table['class'][0]=='raceResults'):
        header=table.find_all('th')
        for head in header:
            fout.write(head.text)
            col=col+1
            if (col==5):
                break
            fout.write(',')
        fout.write('\n')
        info=table.find_all('td')
        count=0
        for inf in info:
            output=(inf.text).encode('UTF-8')
            fout.write(output)
            count=count+1
            if (count==col):
                fout.write('\n')
                count=0
                continue
            fout.write(',')        
    fout.close()
