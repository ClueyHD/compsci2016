# Ecocampus JMSS compsci2016 Tools

These error checking scripts are designed to be used with Atlas of Living Australia and Monash Ecocampus data to make your life a little easier. 

## Prerequisites

All scripts in this repo require Python 3.5 or higher (3.4 will probably work but is untested). 

Instructions here: https://www.python.org/downloads/

EcocampusAnalysis.py & EcocampusAnalysis-NoColour.py require the Plotly library be installed as well as Python. 

Instructions here: https://plot.ly/python/getting-started/

## Intro EcocampusAnalysis.py & EcocampusAnalysis-NoColour.py

These scripts take column data in csv files and count the occurrence of different entries. 
They then prompt you to export the occurrence data to another csv file or plot it using Plotly. 

NOTE: the -NoColour script is for use in command Windows where colouring is not supported. 

## Intro EarthWatch-NameCorrection.py

This script can be used to eliminate bad name entries in EarthWatch Data. 
It checks for double spaces and repeated first and last names. 

NOTE: this script is incomplete and should be considered unstable. 
Usage is same as Ecocampus scripts, but this does not need Plotly. 

## Usage EcocampusAnalysis.py & EcocampusAnalysis-NoColour.py

1. Install Python 3.5 and the Plotly library
2. Ensure all your csv files are in the same directory as the script
3. Run the desired script
4. Follow the prompts
5. Profit?

## Credits

Atlas of Living Australia

Plotly

JMSS

Monash University

## Copyright

'EarthWatch-NameCorrection.py', 'EcocampusAnalysis.py' & 'EcocampusAnalysis-NoColour.py' are covered under MIT License