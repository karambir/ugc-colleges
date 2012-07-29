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

search for            coll_location.png" />
after that s college location
Stop at               <span

"""

cname='some'

f = open(sys.argv[1] , 'rU')
html = str(f.read())
f.close()

cnames = []
for num in range(10):
    nametip =  html.find('<a style="text-decoration:underline;"')
    namestart = html.find(';">', nametip)
    nameend = html.find('</a>', namestart)
    cname = html[namestart+3:nameend]
    cnames.append(cname)
    html = html[nameend:]

for cname in cnames:    
    print cname



