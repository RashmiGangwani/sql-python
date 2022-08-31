'''


Mysql :

    1. Create a  table attribute dataset and dress dataset
    2. Do a bulk load for these two table for respective dataset
    3. read these dataset in pandas as a dataframe
    4. Convert attribute dataset in json format
    5. Store this dataset into mongodb
    6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
    7. Write a sql query to find out how many unique dress that we have based on dress id
    8. Try to find out how many dress is having recommendation 0
    9. Try to find out total dress sale for individual dress id
    10. Try to find out a third highest most selling dress id '''

import mysql.connector as connection
import csvkit
import pandas as pd

mydb=connection.connect(host="localhost",user="root",passwd="Asdfghjkl$1")
cursor = mydb.cursor()

