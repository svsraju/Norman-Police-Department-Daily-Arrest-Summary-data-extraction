# -*- coding: utf-8 -*-
# Example main.py

import argparse
import requests

import urllib
import json
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter
from bs4 import BeautifulSoup



def fetchincidents(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    tag = soup.find_all('a')
    print(type(tag))
     
    list1=[]
    for link in tag:
        list1.append(link.get('href'))
    #return list1

    import re
    r = re.compile(".*Arrest")
    newlist = list(filter(r.match, list1))
    st = "http://normanpd.normanok.gov" 
    
    finallist= []
    for i in newlist:
        i = st + i
        finallist.append(i)
    
    return finallist    
        

    


def extractincidents():
    
    url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-12%20Daily%20Arrest%20Summary.pdf"
    data = urllib.request.urlopen(url).read()
    
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
    
    print(page1)
    
    #page1.strip()
    
    page_changes =  re.sub(r'(.*Officer)(\W)',r'\1;\2',page1)
    
    page_changes
    
    page_changes2 = re.sub(r"\s\n"," ",page_changes)
    page_changes2
    
    page_changes2 = page_changes2.split(';')
    
    
    for i in range(len(page_changes2)):
        page_changes2[i] = page_changes2[i].split('\n') 
    
    #str.split(page1,"\n")
    
    page_changes2.remove
    
    type(page1)


"""def createdb():
    

    CREATE TABLE arrests (
            arrest_time TEXT,
            case_num ber TEXT,
            arrest_location TEXT,
            offense TEXT,
            arrestee_name TEXT,
            arrestee_birthday TEXT,
            arrestee_address TEXT,
            status TEXT,
            officer TEXT
    );"""



#def populateddb(db, incidents):

    
    
#def status(db):




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True, 
                         help="The arrest summary url.")
     
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)

