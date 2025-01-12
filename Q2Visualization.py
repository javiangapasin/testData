#Import all the required libraries
#!/opt/anaconda3/bin/python
import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as ticktools
from matplotlib import pyplot as plt           # Plotting and visualization library.
from matplotlib.ticker import FuncFormatter    # Formatting of tick labels.

# Additional imports for more specific functionality within matplotlib
import matplotlib.ticker as ticker  # Ticker module contains classes to support completely configurable tick locating and formatting.

#Function to format large numbers so they don't appear as decimal numbers, we'll use this later in the program
def format_large_numbers(x, pos):
    return '{:.0f}'.format(x)

def main(argv):
    #Set seaborn to its default theme
    sns.set_theme()

    #Print the command format if the user gets it wrong
    if len(argv) < 3:
        print("Command Format: Q2DataVisualization.py <input file>.csv <output file>.pdf")
        return
    
    #Open the csv file with the data the user specifies
    try:
        rankings = pd.read_csv(argv[1])
    except:
        print("Failed to open the file: {}. Please ensure this file exists.\n(This program should be run after Q1DataProcessing.py)".format(argv[1]))
        return
    
    #Set the size of our plot to be 10x6
    plt.figure(figsize=(15, 11))

    #Create a plot using our opened data (the type will be a line graph, the data will be on the x-axis and will use the column "Year/Quarter", the y-axis will use the column "Number of vacancies
    #the x-axis will be the column "Number of vacancies")
    lineplot = sns.lineplot(data=rankings, x="Year/Quarter", y="Number of vacancies")

    #We want the title of the plot to be the Number of Vacancies Over Time in the province that the user entered
    #We will use iloc, which takes the integer location of a column in the input data and gets that value
    #In the CSV, the province is the third column, so we will use iloc[2] to get the province (python is zero-indexed)
    province = rankings['Province'].iloc[2]
    job_category = rankings['Job category'].iloc[3]
    lineplot.set(title="Number of Vacancies Over Time in {} for job category: \"{}\"".format(province,job_category), xlabel="Year/Quarter", ylabel="Number of Vacancies")

    # Rotate the x axis ticks 90 degrees to make it more readable
    plt.xticks(rotation=90)

    #Using that formatter function we earlier defined, we'll use it to format numbers on the y axis
    formatter = FuncFormatter(format_large_numbers)
    lineplot.yaxis.set_major_formatter(formatter)

    #Uncomment this line to customize the number of ticks in the x axis
    #lineplot.xaxis.set_major_locator(ticker.LinearLocator(numticks=7))
    

    #Save the defined plot to a file specified in argv[2]
    lineplot.figure.savefig(argv[2])


main(sys.argv)
