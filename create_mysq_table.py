#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","shrikanth","GPSDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS GPS")

# Create table as per requirement
sql = "CREATE TABLE GPS(`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,`device` INT NOT NULL,`lat` FLOAT( 10, 6 ) NOT NULL ,`lng` FLOAT( 10, 6 ) NOT NULL)ENGINE = MYISAM"

cursor.execute(sql)

# disconnect from server
db.close()
