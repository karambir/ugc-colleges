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

def find_colleges(text):
    """Given a string, reads and return a list of college names from it
    """

    colleges = []

   
    tuples =re.findall(r'<tr><td valign=top ><ul><li> <font color=#006699>([\w\s%.,(&:)\'\-]+)</font> ([\w.,:()\-\s]+)<b>Yr Estd.:</b> (\d+) <b>Status:</b> ([\w\s()&]+) </ul></td></tr>', text)

    db = MySQLdb.connect(user='root',
            db='amity',
            passwd='myarmy66',
            host='localhost')
    cursor=db.cursor()
    cursor.execute("""
    create table if not exists colleglist
    (
    id integer(5) auto_increment primary key,
    name varchar(160) not null,
    address varchar(200),
    estd year,
    section varchar(40)
    )
    """)

    q_insert = "insert into collegelist (name, address) values (%s, %s)"
    for college in tuples:
    
       #To write in a file
       """
       try:
            logfile = open('colleges.txt', 'a')
            try:
                logfile.write(','.join(map(str,college))+'\n')
            finally:
                logfile.close()
        except IOError:
            pass
        """
        #To write in a database
        cursor.execute(q_insert, (college[0], college[1]))
        db.commit()
    db.close()
    print len(tuples)  #To verify number of college names captured

def main():
    """call find_college function to get a list of colleges and then it prints them
    """

    html = ''
    for num in range(1,414):
        link = 'http://www.indiacollegesearch.com/colleges-india?page='+str(num)
        response = urllib2.urlopen(link)
        html += response.read()
    find_colleges(html)  #To call find colleges function and write them in database or file



if __name__=='__main__':
    main()
