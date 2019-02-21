#project0, function definitions

import argparse
import requests

import urllib
import json
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter
from bs4 import BeautifulSoup

import re
import sqlite3
from sqlite3 import Error


#we are fetching incidents from the url provided by the user

def fetchincidents(url):
    
    data = urllib.request.urlopen(url).read()# using urllib library to read the data from the url
    
    return data

def extractincidents(all_incidents):
    
    data = all_incidents
    
    #creating the tempfile
    fp = tempfile.TemporaryFile()
    # Write the pdf data to a temp file
    fp.write(data)
    # Set the curser of the file back to the begining
    fp.seek(0)
    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()
    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    
    #insering ';' at the end of first row to make sure all the rows have ';' at the end 
    page_changes =  re.sub(r'(.*Officer)(\W)',r'\1;\2',page1)
    
    #clening the data
    page_changes2 = re.sub(r"\s\n"," ",page_changes)
    
    page_changes2 = re.sub(r"-\n"," ", page_changes2)
    
    
    page_changes2 =  re.sub(r'(.*REVOKE)(\W)',r'\1-\2',page_changes2)
    
    page_changes2 = re.sub(r"-\n"," ", page_changes2)
    
    #spliting the data
    page_changes2 = page_changes2.split(';')
    
    for i in range(len(page_changes2)):
        page_changes2[i] = page_changes2[i].split('\n') 
    
    
    page_changes2.pop(len(page_changes2)-1)
    
    for i in range(1,len(page_changes2)):
        page_changes2[i].pop(0)
    
    
    page_changes2.pop(0)
  
    # combining the columns , so as to push 9 values into the database
    for i in range(0,len(page_changes2)):
        
        if len(page_changes2[i]) == 12:
            
            page_changes2[i][len(page_changes2[i]) - 1]
            
            page_changes2[i][6] = page_changes2[i][6] + " " + page_changes2[i][7] + " "+ page_changes2[i][8] + " "+ page_changes2[i][9]
            del(page_changes2[i][7:10])

        if len(page_changes2[i]) == 11:
            
            page_changes2[i][6] = page_changes2[i][6] + " " + page_changes2[i][7] + " "+ page_changes2[i][8]
            
            del((page_changes2[i][7:9]))
            
        if len(page_changes2[i]) == 10:
            
            page_changes2[i][6] = page_changes2[i][6] + " " + page_changes2[i][7]
            
            del((page_changes2[i][7]))
        
    return page_changes2

#creating the database to push the data 
def createdb():
    
    conn = sqlite3.connect(r"normanpd.db")
    cur = conn.cursor()

    arrests_data = """    
    CREATE TABLE IF NOT EXISTS arrests (

        arrest_time TEXT,
        case_number TEXT,
        arrest_location TEXT,
        offense TEXT,
        arrestee_name TEXT,
        arrestee_birthday TEXT,
        arrestee_address TEXT,
        status TEXT,
        officer TEXT)"""
    
    cur.execute(arrests_data)

    return 'normanpd.db' 

# Pushing the data into the database  
def populatedb(db,incidents):
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    for i in range(len(incidents[1])):
        arrests_data  = "INSERT INTO arrests(arrest_time,case_number,arrest_location,offense,arrestee_name,arrestee_birthday,arrestee_address,status,officer) VALUES(?,?,?,?,?,?,?,?,?)"
        cur.execute(arrests_data, (incidents[i][0],incidents[i][1],incidents[i][2],incidents[i][3],incidents[i][4],incidents[i][5],incidents[i][6],incidents[i][7],incidents[i][8] ))
        conn.commit()
    
    cur.close()
    conn.close() 
        

#quering through the database and returning the function at random
def status(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1")
    
    results = cur.fetchall()
        
    #for i in results:
     #   print(i)
    #return results

    new_list = []
    for columns in results:
        new_list.append('þ'.join(columns))

    print(new_list[0])
    return new_list[0]

        
    
