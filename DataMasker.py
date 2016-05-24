__author__ = 'bchan'

import time
import datetime
from faker import Factory
from dateutil.parser import parse

fake = Factory.create()

# ======================= Common Functions =====================

def generate_uuid() :
    fake = Factory.create()
    uuid = fake.uuid4()
    uuid = uuid.replace("-", "").upper()
    return uuid

def generateSSN() :
    return fake.ssn()

def generateCreditCardNumber() :
    return fake.credit_card_number();

def add_days(startdate, days):
  return startdate + datetime.timedelta(days=days)

def generateAddress() :
    address = {}
    fullAddress = fake.address()
    addressParts = fullAddress.splitlines()
    address["address"] = addressParts[0]
    if "," in addressParts[1] :
        cityStateZip = addressParts[1].split(",")
        stateZip = cityStateZip[1].split()
        address["city"] = cityStateZip[0]
        address["state"] = stateZip[0]
        address["postalCode"] = stateZip[1]
    else :
        cityStateZip = addressParts[1].split()
        address["city"] = cityStateZip[0]
        address["state"] = cityStateZip[1]
        address["postalCode"] = cityStateZip[2]
    return address

def generateName(gender=None):
    name = {}
    if gender is None:
        name['firstName'] = fake.first_name()
    else :
        if gender == 'Male':
            name['firstName'] = fake.first_name_male()
        else:
            name['firstName'] = fake.first_name_female()
    name["lastName"] = fake.last_name()
    return name

def generateContact() :
    contact = {}
    contact["email"] = fake.email()
    contact["phone"] = fake.phone_number()
    return contact


