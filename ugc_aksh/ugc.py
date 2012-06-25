import sys
import re
import MySQLdb

def getData(filename):
	"""Function which opens the file from which college names are to be extracted, extracts all the college names and stores them in a file named 'text.txt'.Then it calls another function enterData() for inserting data into database"""

	f = open(filename , 'rU')
	data = f.read()
	match = re.findall( r'<tr><td[\w\s=<>"]+font[\w\s#\d"=]+>([\w\s\',.()]+)',data)
	f.close()

	f = open('text.txt' , 'w')
	for i in range(len(match)):
		f.write(match[i]+'\n')
	
	f.close()
	enterData()


def enterData():
	"""Function which inserts data of the file 'text.txt' into database named 'sample'. Problem you might be facing was that maybe you were not commiting the database. And there are many colleges which has '(single quote) in their names. So while writing these names inside values(' ') it gets clashed with opening and closing single quotes"""

	db = MySQLdb.connect("localhost","root","$avt12104","sample")
	cursor = db.cursor()
	
	f = open('text.txt','rU')
	data = f.readlines()

	for i in range(len(data)):# i will have index no. of text of each line of the file i.e the name of each college
		dt = data[i]
		
		insertData = 'insert into ex values ("%s")' %dt
		cursor.execute(insertData)
		db.commit()

	f.close()
	db.close()




def main():
	getData(sys.argv[1])


if __name__ == '__main__':
	main()
	
