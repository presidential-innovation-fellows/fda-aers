import dse
import unicodecsv
import datetime

def looptest():
    with open('/vagrant/csv/DRUG12Q3.txt', 'rb') as file:
        drug = unicodecsv.reader(file, delimiter='$')
        for row in drug:
            if row:
                print row[7]
              