import urllib2
import sys
import re
import MySQLdb

"""Script to find names of colleges from indiacollegesearch.com website
and print them


<div class="marginBottom7">
    <h2 ><a style="text-decoration:underline;" href="http://indiacollegesearch.com/colleges/Indian_Institute_of_Technology_(IIT)_Delhi"  target="_blank" onclick="return go_to_college_profile('middle_results_form', 1028,'Indian Institute of Technology (IIT) Delhi');">Indian Institute of Technology (IIT) Delhi</a></h2>
</div>

<div class="marginBottom7">
    <h2 ><a style="text-decoration:underline;" href="http://indiacollegesearch.com/colleges/Indian_Institute_of_Technology_(IIT)_Bombay"  target="_blank" onclick="return go_to_college_profile('middle_results_form', 1027,'Indian Institute of Technology (IIT) Bombay');">Indian Institute of Technology (IIT) Bombay</a></h2>
</div>

"""

def find_colleges(html):
    """Given a string, reads and return a list of college names from it
    """

    cnames = [[],[],[],[],[],[],[],[],[],[]]
    for num in range(10):
        nametip =  html.find('<a style="text-decoration:underline;"')
        namestart = html.find(';">', nametip)
        nameend = html.find('</a>', namestart)
        cname = html[namestart+3:nameend]
        #print cname
        cnames[num].append(cname)
        
        #now search for college address
        addstart = html.find('location.png"')
        addend = html.find(' <span class="bold" style="color:#686868;"></span>', addstart)
        cadd = html[addstart+16:addend]
        #print cadd
        cnames[num].append(cadd)

        html = html[nameend:]


    db = MySQLdb.connect(user='root',
            db='amity',
            passwd='myarmy66',
            host='localhost')
    cursor=db.cursor()
    #cursor.execute("""
    #create table if not exists enggcollege
    #(
    #id integer(5) auto_increment primary key,
    #name varchar(360) not null,
    #address varchar(200),
    #estd year,
    #section varchar(40)
    #)
    #""")

    q_insert = "insert into enggcollege (name, address) values (%s, %s)"
    for college in cnames:
        cursor.execute(q_insert, (college[0], college[1]))
        db.commit()
    db.close()


def main():
    """call find_college function to get a list of colleges and then it prints them
    """

    for num in range(415,416):
        link = 'http://www.indiacollegesearch.com/colleges-india?page='+str(num)
        response = urllib2.urlopen(link)
        print "Retrieving Page - " + str(num)
        find_colleges(response.read())  #To call find colleges function and write them in database or file



if __name__=='__main__':
    main()
