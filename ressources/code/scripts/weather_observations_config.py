#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from optionsparser import get_parameters
import matplotlib.pyplot as plt
import argparse 

# Lets start reading our confg file. we'll use argparse to get the config file.
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str,
                    help="Config File name ")
args = parser.parse_args()

# Set optional parameters with default values and required parameter values with their type
defaults = {
           "xlabel" : "Date of observation",
           "title"  : "Observations in Tapiola",
           "start_date" : "01/06/2021",
           "end_date" : "01/10/2021",
           "output_file" : "weather.png",
           }

required = {
           "ylabel" : str,
           "data_column" : str,
           }
           
# now, parse the config file
parameters = get_parameters(args.input, required, defaults)

url = "../python-for-scicomp/data/weather_tapiola.csv"
weather = pd.read_csv(url,comment='#')
# The date format in the file is in a day-first format, which matplotlib does nto understand.
# so we need to convert it.
weather['Local time in Espoo / Tapiola'] = pd.to_datetime(weather['Local time in Espoo / Tapiola'],dayfirst=True)

# Now, we have the data loaded, and adapted to our needs. So lets get plotting


# start the figure.
fig, ax = plt.subplots()
# define the start and end time for the plot 
start_date=pd.to_datetime(parameters.start_date,dayfirst=True)
end_date=pd.to_datetime(parameters.end_date,dayfirst=True)
# select the data
weather = weather[weather['Local time in Espoo / Tapiola'].between(start_date,end_date)]
ax.plot(weather['Local time in Espoo / Tapiola'], weather[parameters.data_column])
# label the axes
plt.xlabel(parameters.xlabel)
plt.ylabel(parameters.ylabel)
plt.title(parameters.title)
# save the figure
plt.savefig(parameters.output_file)



