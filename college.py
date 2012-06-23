import urllib2
import sys
import re

"""Script to find names of colleges from ugc website
and print them

<tr><td valign=top ><ul><li> <font color=#006699>A. Veeriya Vendayar Memorial, Sri Pushpam College</font> POONDI. DIST.:Thanjavur TAMIL NADU-613   <b>Yr Estd.:</b> 1956 <b>Status:</b> 2(f)&12(B)
 </ul></td></tr>




<tr><td valign=top ><ul><li> <font color=#006699>A.B.M. College, SINGHBHUM.</font> DIST.:Purbi Singhbhum Jharkhand    <b>Yr Estd.:</b> 1981 <b>Status:</b> 2(f)&12(B)
 </ul></td></tr>




<tr><td valign=top ><ul><li> <font color=#006699>A.B.M. Degree College, </font> Ongole Distt.: Prakasam Andhra Pradesh   <b>Yr Estd.:</b> 1981 <b>Status:</b> 2(f)&12(B) </ul></td></tr>

"""

def find_colleges(text):
    """Given a file name, it open, reads and return a list of college names from it
    """

    colleges = []

    #f = open(filename, 'rU')
    #text = f.read()

    tuples =re.findall(r'<tr><td valign=top ><ul><li> <font color=#006699>([\w\s%.,(&:)\'\-]+)</font> ([\w.,:()\-\s]+)<b>Yr Estd.:</b> (\d+) <b>Status:</b> ([\w\s()&]+) </ul></td></tr>', text)
    #print len(tuples)
    for college in tuples:
        try:
            logfile = open('colleges.txt', 'a')
            try:
                logfile.write(','.join(map(str,college))+'\n')
            finally:
                logfile.close()
        except IOError:
            pass

        #print college
    print len(tuples)

def main():
    """Parses filename as first arguement and call find_college function to get a list of colleges and then it prints them
    """

    #args = sys.argv[1:]

    #if not args:
        #print 'usage: filename'
        #sys.exit(1)
    html = ''
    for num in range(1,82):
        link = 'http://www.ugc.ac.in/inside/reco_college_search.php?resultpage='+str(num)+'&search=%'
        response = urllib2.urlopen(link)
        html += response.read()
    #print html
    find_colleges(html)

    #print colleges


if __name__=='__main__':
    main()
