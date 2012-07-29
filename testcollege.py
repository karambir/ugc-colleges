import sys
import re

"""
This file is tested with test-page.html

"""


"""Key for searching:

for college name: 

search for            006699
after that is the college name. 
Stop at               font>


for college address:

collegename end + 5
after that is college location
Stop at                <b

for college year:

college add end +16
after that is college year
stop at              college add end +20  

"""
cname='some'
f = open(sys.argv[1] , 'rU')
html = str(f.read())
f.close()
cnames = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for num in range(100):
    namestart =  html.find('006699')
    nameend = html.find('font>', namestart)
    cname = html[namestart+7:nameend-2]
    print cname
    cnames[num].append(cname)
    
    #now search for college address
    addend = html.find('<b', nameend+5)
    cadd = html[nameend+6:addend-2]
    print cadd
    cnames[num].append(cadd)

    
    #search for year of estd.
    cestd = html[addend+17:addend+21]
    print cestd
    try:
        cnames[num].append(int(cestd))
    except ValueError:
        pass
    
    html = html[nameend:]


for cname in cnames:    
    print cname



