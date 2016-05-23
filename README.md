### Data Masking Utilities ###
This Python utility utilizes "fake-factory" module to generate fake name, address, phones, and other personal information.   
More info here: https://fake-factory.readthedocs.io/en/v0.4/index.html#

####Python Runtime Requirements:####
* Python3
* pip3 install fake-factory

####Execution:####
Running the following script will take data from /data/demographics.csv and mask all the fields with fake values. 
first name is generated based on the gender of the original record, birth date will be shift by 10 days.
> python3 DemographisMasking.py
