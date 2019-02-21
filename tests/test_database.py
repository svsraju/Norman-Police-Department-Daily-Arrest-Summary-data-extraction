import pytest

from project0 import project0

database = 'normanpd.db'

def test_createdb():
    dbname  = project0.createdb()
    assert dbname == database

def test_populatedb():
    assert 1 == 1

