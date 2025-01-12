import sys
import csv

def main(argv):
    #Ensure the user input matches our command format
    if len(argv) < 5:
        print("Command Format: Q2DataProcessing.py <data file prefix> <\"region\"> <\"national occupation classification\"> <end year-quarter> <output file>")
        return
     #List of all the regions to use in this question
    regions = ["Alberta", "British Columbia", "Canada", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]
    valid_years = ["2015-01", "2015-04", "2015-07", "2015-10", "2016-01", "2016-04", "2016-07", "2016-10", "2017-01", "2017-04", "2017-07", "2017-10", "2018-01", "2018-04", "2018-07", "2018-10", "2019-01", "2019-04", "2019-07", "2019-10", "2020-01", "2020-04", "2020-07", "2020-10", "2021-01", "2021-04", "2021-07", "2021-10", 
                   "2022-01", "2022-04", "2022-07", "2022-10", "2023-01", "2023-04", "2023-07"]
    #Check if the user entered a valid region
    if argv[2] not in regions:
        print("You have entered an invalid region. The valid regions are:")
        for region in regions:
            print(region)
        print("Please re run the program and re-enter a valid region.")
        return
    
    #Check if the user entered a valid year-quarter
    if argv[4] not in valid_years:
        print("You have entered an invalid year-quarter. The valid year-quarters are:")
        for year in valid_years:
            print(year)
        print("Please re run the program and re-enter a valid year-quarter.")
        return
    
    #Open our "jobs.csv" file which stores all the valid national occupation classifications 
    try:
        valid_jobs_file = open("jobs.csv", "r")
    except OSError:
        print("Unable to find \"jobs.csv\" please ensure it is in the root directory.", file=sys.stderr)
        return
    valid_jobs_reader = csv.reader(valid_jobs_file)

    #Create a flag to store if the user's entered job was valid
    valid_job = False
    #Loop through every job in the file and check if the user's job matches one, set the valid_job flag accordingly
    for rows in valid_jobs_reader:
        if rows[0] == argv[3]:
            valid_job = True
    #Tell the user if they entered an invalid job and then return
    if not valid_job:
        print("You have entered an invalid national occupation classification. Please see jobs.csv for a list of valid NOCs.")
        return
    
    #Open the appropriate region file
    file_handle = open("{}_{}.csv".format(argv[1],argv[2]), encoding="utf-8-sig")
    #Open a CSV reader for the file
    file_reader = csv.reader(file_handle)

    #Open the output file for writing
    try:
        output_handle = open(argv[5], "w")
    except OSError:
        print("Tried to open output file: \"{}\" but couldn't.".format(argv[4]), file=sys.stderr)
        return
    
    #Store the user's end year-quarter
    end_year = argv[4]


    #Write a header to our output file
    output_handle.write("\"Number of vacancies\",\"Year/Quarter\",\"Province\",\"Job category\",\n")  
    for row_data_headers in file_reader: 

        #Find a row which matches what we are looking for and print the data
        if row_data_headers[0] == end_year:
            return
        if row_data_headers[1] == argv[2] and row_data_headers[3] == argv[3] and row_data_headers[4] == "Type of work, all types" and row_data_headers[5] == "Job vacancies" and row_data_headers[12] != "":
            output_handle.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(row_data_headers[12], row_data_headers[0], argv[2],argv[3]))
            #Uncomment this to manually print the data
            #print("{} had {} job vacancies of the type \"{}\" during {}".format(row_data_headers[1], row_data_headers[12], row_data_headers[3], row_data_headers[0]))

#Run main file
main(sys.argv)