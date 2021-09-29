#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Juliette Lee (juliette.lee@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Create a variable pointing to line data file
file_name = "./data/raw/sara.txt"

#Create a file opbject from the file 
file_object = open(file_name, 'r')

#Read contents of file into a list 
line_list = file_object.readlines()

#Close the file 
file_object.close()

#Create two empty dictionary objects 
date_dict = {}
coord_dict = {}

#Iterate through all lines in the linelist
for lineString in line_list[17:]:
    if lineString[0] in ("#","u"): continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables 
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc= lineData[4]
    if obs_lc not in ("1","2","3"):
        continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat,obs_lon)
    