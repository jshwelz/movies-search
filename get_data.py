import requests 
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'


def download_data():      
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall()

  
if __name__ == "__main__":
    download_data()
