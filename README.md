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