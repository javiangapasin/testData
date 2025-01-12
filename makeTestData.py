import csv
import sys

#Our main function
def main(argv):
    #Ensure the user's command matches our command format
    if(len(argv) < 3):
        print("Command Format: <data file> <test file prefix>")
        return

    #Open the full data file the user entered
    file_handle = open(argv[1], encoding="utf-8-sig")
    #Open the file in a csv reader
    file_reader = csv.reader(file_handle)
    #Create lists to hold the names of the files for each region and the region name itself
    regions_files = []
    regions = []
    #Store the current line count
    line_count = 1
    #Empty string to create the header
    header = ""

    #Loop through the file
    for row_data_headers in file_reader:
        #Create a flag to say if the region is already in our list
        already_found = -1
        #Will store the index of the current region
        region_index = 0
        #If we are now in the header
        if line_count > 1:
            #Loop through the regions and check if the region already has a file
            for region in regions:
                if row_data_headers[1] == region:
                    already_found = region_index
                    break
                region_index += 1
            #If the region already has a file
            if already_found != -1:
                element_count = len(row_data_headers)
                element_index = 0
                #Open the appropriate region file 
                region_file_handle = open(regions_files[already_found], "a")
                #Write the line to the appropriate file
                for elements in row_data_headers:
                    if(element_index != element_count-1):
                        region_file_handle.write("\"{}\",".format(elements))
                    else:
                        region_file_handle.write("\"{}\"\n".format(elements))
                    element_index += 1
                #Close the current file
                region_file_handle.close()
            #If the reigon file doesn't already exist
            else:
                #Create a new region name and region file name for our list
                regions.append(row_data_headers[1])
                regions_files.append("{}_{}.csv".format(argv[2], row_data_headers[1]))
                #Open the region file
                region_file_handle = open(regions_files[len(regions_files)-1], "w")
                #Write our header to the file
                region_file_handle.write(header)
                element_count = len(row_data_headers)
                element_index = 0
                #Print the line to the file
                for elements in row_data_headers:
                        if(element_index != element_count-1):
                            region_file_handle.write("\"{}\",".format(elements))
                        else:
                            region_file_handle.write("\"{}\"\n".format(elements))
                        element_index += 1
                #Close the region file
                region_file_handle.close()
        #If this is the first line
        else:
            element_count = len(row_data_headers)
            element_index = 0
            #Save the headers in our header string
            for elements in row_data_headers:
                    if(element_index != element_count-1):
                        header += "\"{}\",".format(elements)
                    else:
                        header += "\"{}\"\n".format(elements)
                    element_index += 1
        line_count += 1

#Run main with user arguments
main(sys.argv)

                

        
