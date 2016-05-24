### Data Masking Utilities ###
This project illustrates how to mask sensitive data from a real production dataset to 
comply with user privacy law. It also include utilities for generating data for testing or analytics.
"fake-factory" module is utilized to generate fake name, address, phones, and other personal information.   
More info here: https://fake-factory.readthedocs.io/en/v0.4/index.html#

####Python Runtime Requirements:####
* Python3
* pip3 install fake-factory

####Execution:####
* Running the following script will take data from /data/demographics.csv and mask all the fields with fake values. 
first name is generated based on the gender of the original record, birth date will be shift by 10 days.
    * python3 DemographisMasking.py
* Running the following script will generate random demographics data
    * python3 DemographicsGenerator.py