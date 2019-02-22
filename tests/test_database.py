import pytest
import sqlite3
url =  "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf"

from project0 import project0

database = 'normanpd.db'

def test_createdb():
    dbname  = project0.createdb()
    assert dbname == database

def test_populatedb():
    dbname  = project0.createdb()
    data = project0.fetchincidents(url)
    incidents = project0.extractincidents(data)
    sql = sqlite3.connect(database)
    cur = sql.cursor()
    cur.execute("SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1")
    
    results = cur.fetchall()

    assert results is not None




