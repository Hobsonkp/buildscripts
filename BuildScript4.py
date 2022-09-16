#############################################################################
##################  Kura Labs Cohort3 Build Script 4  #######################
#############################################################################
# Name: Kerri Smith
# Date: 15th September 2022
# kerri.p.h.smith@gmail.com
#---------------------------------------------------------------------------#
#
# Objective: Demonstrate your ability to gather data from an API and organize 
# that data into a specific format (see BuildScript4README.txt for more details)
# 
# FUNCTIONALITY
#   The script read a list of IP addresses from there were failed login attempts to an ftp server.
#   The location of these IP addresses are retrieved from the ipgeolcation api
#
#  The script uses the following files:
#   BuildScript4.py - generates output CSV file
#   BuildScript4_api.sh - gathers the IP addresses from the error report and accesses the api to retrieve the ipgeolocations

#  GitHub link for script: https://github.com/Hobsonkp/buildscripts/tree/build4

#############################################################################
# Limitations script can only access a specific log file in a set location
# Future versions will allow for the user to enter the location of the log file
# A web interface can also be introduced to allow the user to upload or drag and drop the error file and download the report
#############################################################################

from cgi import print_form
from pickle import TRUE
import subprocess
import json
import csv

# there are 24 headers returned by the api
headers=['ip', 'continent_code', 'continent_name', 'country_code2', 'country_code3', 'country_name', 'country_capital', 'state_prov', 'district', 'city', 'zipcode', 'latitude', 'longitude', 'is_eu', 'calling_code', 'country_tld', 'languages', 'country_flag', 'geoname_id', 'isp', 'connection_type', 'organization', 'currency', 'time_zone']

# get list of ip addresses from csv log file
result = subprocess.run(['./BuildScript4_api.sh','-r','FailedLogins_report.csv'], stdout=subprocess.PIPE).stdout.decode('utf-8')

with open('geoFailures.csv', 'w', newline='') as csvfile:
    fieldnames = headers
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ipInput in result.splitlines():
        if ipInput !="":
            jsonResult=json.loads(subprocess.run(['./BuildScript4_api.sh','-g',ipInput], capture_output=True).stdout.decode('utf-8'))
            writer.writerow(jsonResult)

#
#print(jsonResult.keys())
#for line in result.splitlines():
#    print(line)
#    print("no")


# remove duplicates
# verify that the number of IP addresses will not exceed the API limit (only use top 5 IP addresses)

#print(subprocess.run(["./BuildScript4.sh"], capture_output=TRUE))
#print("hello")