# Statistics Canada Project
A group project from CIS 2250 where we created a Python project that worked with data from Statistics Canada to create visualizations using Pandas.

Data Transformations
The data we need is stored in the 14100328 and 17100005 files. The data from 14100328 is split up by region into separate files to make the data more manageable. Then the data processing program extracts the number of job vacancies for the job type that the user entered in all regions in the year the user entered. It then finds the population of the regions in the year and age range the user mentioned. The number of jobs is then divided by the population and output into a data file with a name specified by the user. A visualization can then be generated from this file. 
Programs That Need to Be Run
The first program that will need to be run is makeTestData.py. This program will split the original 14100328.csv file up by region. (This program only needs to be run once) This is the command format:
makeTestData.py <job data file name> <prefix of output files>
After that, run Q1DataProcessing.py. This program will create a csv file with the “job ratios” (number of job vacancies according to user parameters divided by population according to user parameters) and their corresponding regions. This is the command format:
Q1DataProcessing.py <data file prefix> <population file> <output file> <national occupation classification> <age range> <year>
Notes: The data file prefix should be the same as the second argument of makeTestData.py. Also, the national occupation classification must be a complete string including the name and id (e.g "Health occupations [3]")
After the data file is generated a visualization can be created with the Q1Visualization.py program. This is the command format:
Q1DataVisualization.py <input file> <output file>.pdf
Note: The input file should be the same as the “output file” of Q1DataProcessing.py


Note: This graph was created on a system running Linux. While the functionality of the program will remain the same on all platforms the bars may appear a different color due to variations in seaborn’s default theme across operating systems.

Question 2: How have job vacancies been changed over the years across regions and job categories?

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

Question 3: How have wages for jobs of a specific region changed over the years?
(Note: This question has been changed since the previous milestone, it was changed due to the fact that specific categories/regions was a very open ended question and not so specific, making it harder to program when finding data to visualize. Focusing on a specific region is a much simpler way for me to gather data.)

Data Transformations:
Using the given datasets from 14100328.csv, the data required is not as large as the given data sets, so the first transformation done is actually splitting the main data file into different region files with separate names, they all follow a naming scheme of testData_<region name>.csv. Next, the program for this question only grabs data that meets the requirements, first being data that has the “Average offered hourly wage” as its Statistics field. Next the data is then checked to make sure the National Occupational Classification field is “Total, all occupations” and checking if “Job vacancy characteristics” field is “Type of work, all types”. From there, the datasets with the given following field values have both its REF_DATE and VALUE printed and separated by comma, (REF_DATE,VALUE). This transformed data is then used for visualization.

Programs That Need to Be Run
The first program that needs to be run is Q3DataProcessing.py, it has two required parameters being the Region name (this will be used to find the actual file, as we have organized the datasets by region as testData_<Region name>.csv), and a output file (this is the file that will get the output from the data processing).
After Q3DataProcessing.py, the next program that will be run is Q3Visualization.py, this is for visualizing the data provided by the first program, this program has three parameters, first is the input file, which will be the file with the output from Q3DataProcessing.py, the next will be the output file, which is what you want the graph to be saved to, so name.pdf, lastly the region name, which will give the graph of the region you did data processing and visualizing on.


Question 4: Which region has the most job vacancies in a specific category?

Data Transformations
For this question, our analysis began with data contained within the 14100328.csv file. The transformation process involved extracting job vacancy information specific to the user-inputted job category across all Canadian regions ( including Canada itself as a whole).  The data processing script Q4DataProcessing.py was designed to count the number of job vacancies for each region and record these figures into an output CSV file that can later be used for visualization.

Programs That Need to Be Run
To prepare the data for visualization, the Q4DataProcessing.py script needs to be executed with the following command:
Q4DataProcessing.py <input_file> <job_category> <output_file>

The following command line instance would be specific to the "Software engineers and designers [2173]" job category. For others, the user is only required to change the string for the desired specific job category:
Q4DataProcessing.py 14100328.csv "Software engineers and designers [2173]" processed_data1.csv 

This script reads the input file, filters it by the job category, and aggregates the total job vacancies per region into the specified output file.
After the data processing is complete, the Q4Visualization.py script is used to create a bar chart visualization of the data. The command format for this script is:
Q4Visualization.py <processed_data_file> <visualization_output_file>.pdf

For a specific visualization, such as for the job category "Software engineers and designers [2173]", the user must first generate the processed data using the Q4DataProcessing.py script with the appropriate job category argument. Then, to visualize the results, the Q4Visualization.py script is run using the processed data and the job category as arguments. It is important to note that if the user wishes to analyze a different job category, both the data processing and visualization scripts must be re-run with the new job category string. Additionally, the output_chart.pdf file will be overwritten if the same file name is used for subsequent visualizations. To retain previous visualizations, the user should specify a unique output file name for each visualization, such as output_chart_2.pdf. For instance:
Q4Visualization.py processed_data1.csv output_chart.pdf "Software engineers and designers [2173]"

If the user wishes to create a new visualization for a different job category without overwriting the previous one, they could run:
Q4Visualization.py processed_data1.csv output_chart_2.pdf "New Job Category [ID]"

This approach ensures that each visualization is saved to a separate PDF file.
Visualization
The bar chart visualizes the aggregated job vacancy data, providing a clear comparison of the number of job vacancies in each Canadian region for the chosen job category. This visualization makes it easy to identify regions with the highest concentration of job vacancies.
Note: The visualization's appearance, such as colour and style, may vary depending on the Seaborn and Matplotlib library versions used.

