import sys
import re

"""
This file is tested with test-page3.html

"""


"""Key for searching:

for college name: 

search for            <h2 ><a style="text-decoration:underline;"
then search for        ">
after that is the college name. 
Stop at                </a>


for college address:

search for            location.png" />
after that s college location
Stop at               <span

"""

cname='some'

f = open(sys.argv[1] , 'rU')
html = str(f.read())
f.close()

cnames = [[],[],[],[],[],[],[],[],[],[]]
for num in range(10):
    nametip =  html.find('<a style="text-decoration:underline;"')
    namestart = html.find(';">', nametip)
    nameend = html.find('</a>', namestart)
    cname = html[namestart+3:nameend]
    print cname
    cnames[num].append(cname)
    
    #now search for college address
    addstart = html.find('location.png"')
    addend = html.find(' <span class="bold" style="color:#686868;"></span>', addstart)
    cadd = html[addstart+14:addend]
    print cadd
    cnames[num].append(cadd)

    
    #search for year of estd.
    estdstart = html.find('Established in')
    estdend = html.find('<', estdstart+19)
    cestd = html[estdstart+22:estdend]
    print cestd
    cnames[num].append(int(cestd))
    
    html = html[nameend:]


for cname in cnames:    
    print cname



