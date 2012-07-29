import sys
import re
import MySQLdb

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



def getData(filename):
    """Function which opens the file from which college names are to be extracted, extracts all the college names and stores them in a file named 'text.txt'.Then it calls another function enterData() for inserting data into database"""

    f = open(filename , 'rU')
    data = f.read()
    print data
    
    f.close()



def main():
    getData(sys.argv[1])


if __name__ == '__main__':
    main()
