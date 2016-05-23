__author__ = 'bchan'

import time

import csv
import DataMasker
from dateutil.parser import parse

def generateDemographics(input) :
    member = {}
    member["ssn"] = DataMasker.generateSSN()
    # Shift BirthDate
    bDate = parse(input["birthDate"])
    member['birthDate'] = DataMasker.add_days(bDate, 10).strftime('%m-%d-%Y')

    # Name acccording to gender
    member['gender'] = input['gender']
    name = DataMasker.generateName(member['gender'])
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


def main():
    start = time.time()
    list = []
    with open('data/demographics.csv') as inFile:
        reader = csv.DictReader(inFile)
        for row in reader:
            result = generateDemographics(row)
            list.append(result)
    inFile.close()
    with open('demographicsMasked.csv', 'w') as outFile:
        fieldnames = ['ssn','birthDate','gender','firstName','lastName',
                      'address','city','state','postalCode','email','phone']
        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)
    outFile.close()
    end = time.time()
    elapsed = end - start

if __name__ == "__main__":
    main()

