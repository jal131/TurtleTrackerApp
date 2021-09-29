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


#Pretend we read one line of data from teh file
lineString = line_list[750]

#Split the string into a list of data items
lineData = lineString.split()

#Extrract items in list into variables 
record_id = lineData[0]
obs_date = lineData[2]
obs_lc= lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
