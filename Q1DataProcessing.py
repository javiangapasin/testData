#Import modules
import sys
import csv

def main(argv):
    #Check if there are enough arguments for the command and print a message if there aren't
    if len(argv) < 7:
        print("Command Format: Q1DataProcessing.py <data file prefix> <population file> <output file> <national occupation classification> <age range> <year>")
        return
    #List of all the regions to use in this question
    regions = ["Alberta", "British Columbia", "Canada", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]
    #List of all the valid age ranges in the population file
    age_ranges = ["0 to 4 years","5 to 9 years","10 to 14 years","15 to 19 years","20 to 24 years","25 to 29 years","30 to 34 years","35 to 39 years","40 to 44 years","45 to 49 years","50 to 54 years","55 to 59 years","60 to 64 years",
                  "65 to 69 years","70 to 74 years","75 to 79 years","80 to 84 years","85 to 89 years","90 to 94 years","95 to 99 years","100 years and older","0 years","1 year","2 years","3 years","4 years","5 years","6 years","7 years",
                  "8 years","9 years","10 years","11 years","12 years","13 years","14 years","15 years","16 years","17 years","18 years","19 years","20 years","21 years","22 years","23 years","24 years","25 years","26 years","27 years",
                  "28 years","29 years","30 years","31 years","32 years","33 years","34 years","35 years","36 years","37 years","38 years","39 years","40 years","41 years","42 years","43 years","44 years","45 years","46 years","47 years",
                  "48 years","49 years","50 years","51 years","52 years","53 years","54 years","55 years","56 years","57 years","58 years","59 years","60 years","61 years","62 years","63 years","64 years","65 years","66 years","67 years",
                  "68 years","69 years","70 years","71 years","72 years","73 years","74 years","75 years","76 years","77 years","78 years","79 years","80 years","81 years","83 years","84 years","82 years","85 years","86 years","87 years",
                  "88 years","89 years","18 to 24 years","25 to 44 years","45 to 64 years","18 to 64 years","65 years and older","90 years","91 years","92 years","93 years","94 years","95 years","96 years","97 years","98 years","99 years",
                  "All ages", "90 years and older","0 to 14 years","0 to 15 years","0 to 16 years","0 to 17 years","15 to 49 years","15 to 64 years","16 to 64 years","17 to 64 years","18 years and older","Median age","Average age"]
    #Boolean that will store if the user entered a valid age range
    valid_range = False
    #Compare the user's entered age range to all the valid age ranges and set the valid_range variable accordingly
    for age_range in age_ranges:
        if argv[5] == age_range:
            valid_range = True
    #If the user didn't enter a valid range print an error and return
    if not valid_range:
        print("You have entered an invalid age range. Please see 17100005_MetaData.csv for a list of valid ranges.")
        print("Command Format: Q1DataProcessing.py <data file prefix> <population file> <output file> <national occupation classification> <age range> <year>")
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
        if rows[0] == argv[4]:
            valid_job = True
    #Tell the user if they entered an invalid job and then return
    if not valid_job:
        print("You have entered an invalid national occupation classification. Please see jobs.csv for a list of valid NOCs.")
        print("Command Format: Q1DataProcessing.py <data file prefix> <population file> <output file> <national occupation classification> <age range> <year>")
        return
    #Open our output file for writing
    try:
        output_handle = open(argv[3], "w")
    except OSError:
        print("Tried to open output file: \"{}\" but couldn't.".format(argv[3]), file=sys.stderr)
        return
    
    #Write a header to our output file
    output_handle.write("\"Region\",\"Jobs/Population\"\n")

    #Loop through every region
    for region in regions:
        #Open the file containing the data for the current region
        try:
            job_file_handle = open("{}_{}.csv".format(argv[1], region), "r")
        except OSError:
            print("Tried to open region job data file: \"{}\" but couldn't. Please check your <data file prefix> argument and ensure all your regions files are in the root directory.".format("{}_{}.csv".format(argv[1], region)), file=sys.stderr)
            return
        job_file_reader = csv.reader(job_file_handle)
        
        #Open the population data file
        try:
            population_file = open(argv[2], "r")
        except OSError:
            print("Tried to open population data file: \"{}\" but couldn't. Please check your <population file> argument and ensure the population file is in the root directory.".format(argv[2]), file=sys.stderr)
            return
        population_reader = csv.reader(population_file)
        
        #Create floats to store the population and job ration, set them to -1 as a fail state
        population = -1.0
        job_ratio = -1.0
        
        #Loop through our population file and when we find the appropriate population set the population variable accordingly
        for data_headers in population_reader:
            if data_headers[0] == argv[6] and data_headers[1] == region and data_headers[3] == "Total - gender" and data_headers[4] == argv[5]:
                    population = float(data_headers[11])
        
        #Loop through the job file and when the appropriate value is found calculate the job ratio
        for data_headers in job_file_reader:
            #Also, we make sure there is data and if there isn't we print a message and set the job ratio to zero
            if data_headers[0] == "{}-01".format(argv[6]) and data_headers[3] == argv[4] and data_headers[1] == region and data_headers[5] == "Job vacancies" and data_headers[4] == "Type of work, all types" and data_headers[12] != "":
                job_ratio = float(data_headers[12])/population
            elif data_headers[0] == "{}-01".format(argv[6]) and data_headers[3] == argv[4] and data_headers[1] == region and data_headers[5] == "Job vacancies" and data_headers[4] == "Type of work, all types" and data_headers[12] == "":
                print("The region {} has no quality data for the national occupation classification and year you provided. Its job ratio will be set to 0".format(region))
                job_ratio = 0
        #Output the job ratio of the current region to the output file
        output_handle.write("\"{}\",\"{}\"\n".format(region, job_ratio))
        
        #Close our open files for the next loop
        job_file_handle.close()
        population_file.close()
    
    #Close our output file
    output_handle.close()

    #Print a message to the user telling them how to get the visualization
    print("Data succesfully processed! You can view the result in {}.\nIf you would like to create a visualization of this data please use Q1Visualization.py.".format(argv[3]))


#Run our main file
main(sys.argv)