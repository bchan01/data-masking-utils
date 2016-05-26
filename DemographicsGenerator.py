__author__ = 'bchan'

import time
import sys
import csv
import DataMasker
from dateutil.parser import parse

def generateDemographics() :
    member = {}
    member["ssn"] = DataMasker.generateSSN()
    member['creditCard'] = DataMasker.generateCreditCardNumber()
    name = DataMasker.generateName()
    member['firstName'] = name['firstName']
    member['lastName'] = name['lastName']

    # Address
    address = DataMasker.generateAddress()
    member['address'] = address["address"]
    member['city'] =  address["city"]
    member['state'] = address["state"]
    member['postalCode'] = address["postalCode"]

    # Contact
    contact = DataMasker.generateContact()
    member["phone"] = contact["phone"]
    member["email"] = contact["email"]

    return member


def main(records):
    start = time.time()
    list = []
    for x in range(0, records):
        list.append(generateDemographics())

    with open('demographicsData.csv', 'w') as outFile:
        fieldnames = ['ssn','creditCard','firstName','lastName',
                      'address','city','state','postalCode','email','phone']
        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)
    outFile.close()
    end = time.time()
    elapsed = end - start

if __name__ == "__main__":
    records = 100
    print('Generating %d records'% records)
    main(records)

