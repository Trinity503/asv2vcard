#https://pypi.org/project/csv2vcard/#description
#last_name, first_name, org, title, phone, email, website, street, city, p_code, country
# csv2vcard.test_csv2vcard()

import csv2vcard
from csv2vcard import csv2vcard

#csv2vcard.test_csv2vcard()
csv2vcard.csv2vcard('export.csv', ';')
