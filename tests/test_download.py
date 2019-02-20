import pytest

from project0 import project0

url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-17%20Daily%20Arrest%20Summary.pdf"

def test_fetchincidents():
    assert project0.fetchincidents(url) is not None
    
