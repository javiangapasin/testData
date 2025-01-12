# Statistics Canada Project
A group project from CIS 2250 where we created a Python project that worked with data from Statistics Canada to create visualizations using Pandas.

**PLEASE NOTE**: For this project, we required many large files from Statistics Canada.

The data that we downloaded can be found here: https://www150.statcan.gc.ca/n1/en/type/data?MM=1#tables

The data sources and files that will be required for these questions will be the statistics on employment data from across the country, from Statistics Canada.
Within that data source, all files can be used for this question as they all involve vacancies changing over a period of time, but a specific example is the 1410032803-databaseLoadingData.csv file. The fields in these files that will be required for this question are “REF_DATE”, “GEO” and “VALUE”.


The question to be answered: How have job vacancies been changed over the years across regions and job categories?

Data Transformations

The data we used for this program will be found in the 14100328.csv file. We will first split the data into different regions for it to be easier to manage later. The naming scheme for these files will be testData_<region name>.csv. Next, the program will grab the REF_DATE, GEO, National Occupational Classification, and VALUE values from the region csv file. It will then write these values into a separate csv file with the headers “Number of vacancies”, "Year/Quarter","Province", and"Job category". This csv file will then be used later for visualization.

Programs That Need to Be Run

The first program that will need to be run is makeTestData.py. This program will split the original 14100328.csv file up by region. (This program only needs to be run once) This is the command format:
makeTestData.py <job data file name> <prefix of output files>
After that, Q2DataProcessing.py should be run to create the csv file containing the values for number of vacancies, the ending year/quarter values, province and job category. The command line format will be:
Q2DataProcessing.py <data file prefix> <\"region\"> <\"national occupation classification\"> <end year-quarter> <output file>

Notes: The data file prefix should be the same as the second argument of makeTestData.py. Also, the national occupation classification must be a complete string including the name and id (e.g "Health occupations [3]"), and observe the quotation marks around the region as well (e.g “Ontario”).

After this csv file is generated, it can be used to create a visualization using the program Q2Visualization.py, and using the following command format:
Q2DataVisualization.py <input file>.csv <output file>.pdf

Note: The input file should be the same as the “output file” of Q1DataProcessing.py


