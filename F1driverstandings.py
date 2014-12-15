import urllib2,sys
from bs4 import BeautifulSoup
year=raw_input('Enter the year to get driver standings (1950-2014): ')
year_check=int(year)
if(year_check>2014)or(year_check<1950):
    print 'Kindly enter the year within the specified range\nThe program is now exiting'
    sys.exit()
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
