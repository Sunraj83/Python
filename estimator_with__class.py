# -*- coding: utf-8 -*-
"""
Sunny Nagdev
Class: CS 521 - Summer Term 2
Term Project
Date: 8/23/2019
Description of Problem: Program to create expense estimation for accomodation
in Hawaii islands

"""

# Import destination class
from hawaiInfo import hawaiInfo_class
import hawaiInfo


def welcome():
    print(f'\nAloha! Welcome to Hawaii Vacation Cost Estimator')
    print(f'----------------------------------------------------\n')

def getItinNumber(n):
    return (n + 1)

def main():
    
    itinList = []
    for i in range(0, 3):
        itinerary = hawaiInfo_class(id = i)
        itinList.append(itinerary)

# Calling User Defined function Welcome
    welcome()

# Display all island destinations from hawaiInfo
    hawaiInfo.print_IslandSelections()
# Selecting Destination
    selection = hawaiInfo.get_IslandSelection()
    
# Display all months for selectin
    hawaiInfo.print_Months()
# Selecting month
    month = hawaiInfo.get_Month()    
    
# Display Property Stars for selection
    hawaiInfo.print_PropertyStar()
# Selecting Property Stars
    propertyStars = hawaiInfo.get_PropertyStar()

# Determine Nights of stay
    while True:
        try:
            nights = int(input("Enter number of nights you will be staying in: "))
            # Check for neagtive input
            if (nights < 0):
                print("Please enter a positive number of days.")
                continue
        except ValueError:
                print("Invalid number of nights. Only numerical values are valid.")
#            else:
        break
    
# Setting 'itinerary' object by passing parms to hawaiInfo class public methods
# as earlier for lop initialized 3 itinerary objects, this program can be scalable to add 3 itineraries to file
# for now, i worked with just 1 itinerary object
        
## public methods of class hawaiInfo to take arguments

    itinList[0].setIslandID(selection)   
    itinList[0].setMonthID(month)
    itinList[0].setStarID(propertyStars)
    itinList[0].setNights(nights)
    
## Demo for accessing 2 public attributes of class hawaiInfo_class directly
    
    print(f'\nYou chose {itinList[0].nights} nights at {itinList[0].starID} star property')
    
# getting values from user defined functions based on 'itinerary' object values.
    
    islandName = hawaiInfo.get_IslandName(selection)
 
   ## Below statement will give error because getIslandID is Private Method within class
#   islandName = hawaiInfo.get_IslandName(itinList[0].getIslandID())   
    
## Showing public methods of class hawaiInfo to return values
    
    propertyCostFactor = hawaiInfo.get_PropertyCostFactor(itinList[0].getStarID())    
# get cost factor dependent on month
    monthCostFactor = hawaiInfo.get_Month_CostFactor(itinList[0].getMonthID())[1]
    monthName = hawaiInfo.get_Month_CostFactor(itinList[0].getMonthID())[0]
    islandCostFactor =  hawaiInfo.get_IslandCostFactor(islandName) 
    
    print(f'\n{repr(hawaiInfo_class())}')

# Calculating Total Cost of Stay
# Calculate cost before Tax
    costBeforeTax = (nights * monthCostFactor * islandCostFactor * propertyCostFactor) ## $20 is Average Resort fees
# Calculate total cost after tax as per the Island selected
    
# Accessing public method get_IslandHotelTaxRate() of class, which uses private method '__getIslandID()' within class
    costAfterTax = costBeforeTax + (costBeforeTax * itinList[0].get_IslandHotelTaxRate()/100)
    
        
# ****** FILE HANDLING LOGIC STARTS HERE**********************************************************************
# Program will read from existing file, get all previous itineraries and write a new itinerary
   
##  Reading from existing file. File can be a blank text file with same name
    
    fileName = "itinerary.txt"
    input_itinerary_file = open(fileName, "r")              # open file in read mode
    lines = input_itinerary_file.readlines()  
    input_itinerary_file.close()                            # closing the file
    
    if lines == []:                                         # checking whether file is blank text file or not
        new_itin_num = '1         '                         # if runing program for first time
    else:
        new_itin_num = getItinNumber(int(lines[3][14:24]))  # reading itinerary number for last printed itinerary
        
    # Open existing file to create new itinerary
    itinerary_file = open(fileName, "w+")
    
    # Write itinerary and estimate information
    itinerary_file.write(f'\nHawaii Trip Accomodation Cost Estimation')
    itinerary_file.write("\n------------------------------------------------------------------")
    itinerary_file.write(f'\nItinerary # : {new_itin_num}')
    itinerary_file.write(f'\n\nDestination Island(s) Selected         : {str(islandName)}')
    itinerary_file.write(f'\nMonth of Vacation                           : {str(monthName)}')
    itinerary_file.write(f'\nProperty Status                               : {str(propertyStars)} stars')
    itinerary_file.write(f'\nNumber of Nights                           : {str(nights)}')    
    itinerary_file.write(f'\nTotal Itinerary Cost                        : ${str(format(costAfterTax,"<10.3f"))}')
    itinerary_file.write(f'\n-----------------------------------------------------------------')
    
# Appending the previous itinerarries to output file for comparison
    for line in lines:
        itinerary_file.write(line)

    itinerary_file.close()     # Close the file
    
# *********FILE HANDLING LOGIC ENDS HERE  *****************************************************************************
    
    print(f'-----------------------------------------------------------------------------------------------')    
    print(f'\nEstimated cost for Hawaii Island {islandName} in {monthName} month is ready for your review')
    print(f'Please open file "itinerary.txt"')

main()


