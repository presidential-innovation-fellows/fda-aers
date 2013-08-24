import unicodecsv
import datetime

#from reports.models import *

def datetime_validator(value):
    if value:
        try:
            return datetime.datetime.strptime(value, '%Y%m%d')
        except:
            return None
    
def boolean_validator(value):
    if value == "Y":
        return True
    if value == "N":
        return False
    else:
        return None

def float_validator(value):
    try:
        value = float(value)
        return value
    else:
        return None           
            
def integer_validator(value):
    try:
        value = int(value)
        return value
    except:
        return None

def string_validator(value):
    try:
        value = str(value)
        return value
    except:
        return None
    


def import_demographics():
    with open('/vagrant/csv/DEMO12Q3.txt', 'rb') as file:
        demo = unicodecsv.reader(file, delimiter='$')
        firstline = True
        values = []
        list = []
        for row in demo:
            if firstline:
                firstline = False
                continue
            else:
                isr = integer_validator(row[0])
                case_number = integer_validator(row[1])
                i_f_cod = string_validator(row[2])
                image = string_validator(row[4])
                event_dt = datetime_validator(row[5])
                mfr_dt = datetime_validator(row[6])
                fda_dt = datetime_validator(row[7])
                rept_cod = string_validator(row[8])
                mfr_num = string_validator(row[9])
                mfr_sndr = string_validator(row[10])
                age = float_validator(row[11])
                age_cod = string_validator(row[12])
                gndr_cod = string_validator(row[13])
                e_sub = boolean_validator(row[14])
                wt = float_validator(row[15])
                wt_cod = string_validator(row[16])
                rept_dt = datetime_validator(row[17])
                occp_cod = string_validator(row[18])
                death_dt = datetime_validator(row[19])
                to_mfr = boolean_validator(row[20])
                confid = boolean_validator(row[21])
                reporter_country = string_validator(row[22])
                
                print case_number
                
        
import_demographics()
