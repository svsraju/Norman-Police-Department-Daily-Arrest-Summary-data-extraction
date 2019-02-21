import pytest
  
from project0 import project0

url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf"

def test_status():
    links = project0.fetchincidents(url)
    data = project0.extractincidents(links)
    database = project0.createdb()  
    randominfo = project0.status(database)
    assert type(randominfo)== str
