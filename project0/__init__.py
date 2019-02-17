import argparse
import project0
def main(url):
    # Download data
    project0.fetchincidents(url)
    # Extract Data
    incidents = project0.extractincidents()
    # Create Dataase
    db = project0.createdb()
    # Insert Data
    project0.populatedb(db, incidents)
    # Print Status
`    project0.status(db)
