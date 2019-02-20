#import pytest

from project0 import project0

database = 'normanpd.db'

def test_createdb():
    dbname  = project0.createdb()
    assert dbname == database

def test_populatedb():
    assert 1 == 1

def test_status():
    #links = project0.fetchincidents()
    #data = project0.extractincidents(links)
    randominfo = project0.status(database)
    assert type(randominfo)== list
    assert type(randominfo[0])== tuple
