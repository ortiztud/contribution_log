#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:32:49 2023

@author: javierortiz
"""

import csv

# Open the CSV file with the correct encoding
with open('contribution_list.csv', 'r', encoding='ISO-8859-1') as file:
    # Create a CSV reader using a semicolon as the delimiter
    reader = csv.reader(file, delimiter=';')
    
    # Get the first row with the variable names
    header = next(reader)
    
    # Create a list of dictionaries, one for each row of data
    data = [dict(zip(header, row)) for row in reader]
    
    # Sort the list of dictionaries by the year, in descending order
    data.sort(key=lambda x: -int(x["Year"]))
    
    # Open the output file with the correct encoding
    with open('formatted_contributions.txt', 'w', encoding='ISO-8859-1') as output:
        # Loop through the sorted list of dictionaries
        for row in data:
            # Get the value of the "Country" variable
            country = row["Country"]
            
            # If the "Country" variable is empty, use a different format for the sentence
            if not country:
                sentence = " {} ({}). {}. {}. {}. ({}). {}".format(row["Authors"], row["Year"], row["Title"], row["Acronym"], row["Organiser"], row["City"], row["Contribution_type"])
            else:
                sentence = " {} ({}). {}. {}. {}. {} ({}). {}".format(row["Authors"], row["Year"], row["Title"], row["Acronym"], row["Organiser"], row["City"], row["Country"], row["Contribution_type"])
            
            # Write the sentence to the output file
            output.write(sentence + '\n')