import MySQLdb
import csv

conn = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="nickbelgau",         # your username
                     passwd="?Chemical6",  # your password
                     db="generaldb")        # name of the data base

cursor = conn.cursor()

if conn:
    print("Connection successful")
else:
    print("Connection unsuccessful")


#Dropping table if already exists.
cursor.execute("DROP TABLE IF EXISTS spacex")


#Creating table as per requirement
createtable ='''CREATE TABLE spacex(
   DATE varchar(20),
   BOOSTER_VERSION char(100),
   LAUNCH_SITE char(100),
   PAYLOAD char(100),
   PAYLOAD_MASS__KG_ int,
   ORBIT char(100),
   CUSTOMER char(100),
   MISSION_OUTCOME char(100),
   LANDING_OUTCOME char(100)
)'''

cursor.execute(createtable)

'''
#LOAD DATA INTO FILE isnt working from IDE, so ran from SQL shell
#upload csv to sql table
uploadcsv = 
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Spacex.csv'
INTO TABLE spacex
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
;

cursor.execute(uploadcsv)'''

conn.close()

