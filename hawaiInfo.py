# -*- coding: utf-8 -*-
"""
Sunny Nagdev
Class: CS 521 - Summer Term 2
Term Project
Date: 8/23/2019
Description of Problem: Class hawaiInfo and some user defined functions to calculate cost
"""

class hawaiInfo_class:
    
    def __init__(self,id = 1,islandID = 1,monthID = 1, starID = 3, nights = 0,cost = 0):
        self.__id = int(id)
        self.__islandID = int(islandID)
        self.__monthID = int(monthID)
        self.starID = int(starID)
        self.nights = int(nights)
        
    def getID(self):
        return self.__id
    
    def setID(self,id):
        self.__id = id
     
    def __getIslandID(self):           ## Private method
        return self.__islandID
    
    def setIslandID(self,islandID):
        self.__islandID = islandID

    def getMonthID(self):
        return self.__monthID
    
    def setMonthID(self,monthID):
        self.__monthID = monthID        
        
    def getStarID(self):
        return self.starID
    
    def setStarID(self,starID):
        self.starID = starID     
        
    def getNights(self):
        return self.nights
    
    def setNights(self,nights):
        self.nights = nights 
        
    def getCost(self):
        return self.__cost
    
    def setCost(self,cost):
        self.__cost = cost
        
    def get_IslandHotelTaxRate(self):     
#        if (self.__islandID == 1):
        if self.__getIslandID() == 1:   ## Calling Private method within class only
            return 14.96
        else:
            return 14.41
     
    a = "Class Name is HawaiInfo_class. This message is for repr Demo only"
    
    def __repr__(self):        
        return repr(self.a)

    
def print_IslandSelections():
    # Travel Selections for Hawaii Islands
    print("Select from below Hawaii Islands:")
    print("-----------------------------------")
    print("1. Oahu")
    print("2. Maui")
    print("3. Big Island")
    print("4. Kaui")
    print("")
    
def get_IslandSelection():
    # Get Islands selection
    while True:
        try:
            selection = int(input("Choose from above options :"))
            if (selection < 1) or (selection > 4):
                print("Please select an option between 1 and 4.")
                continue
        except ValueError:
            print("Invalid Selections. Try again!")
        else:
            return selection            
            
def get_IslandName(selection):  
    if (selection == 1):
        return "Oahu"

    elif (selection == 2):
        return "Mauii"

    elif (selection == 3):
        return "Big Island"
    
    elif (selection == 4):    
        return "Kauii"
        
#########  Estimation based on Month of Travel   #################################
    
def print_Months():
    # Travel Selections for Hawaii Islands
    print("\nMonth of Travel:")
    print("---------------------------------------------------")
    print(f'1. January        2. Febraury       3. March\n4. April          5. May            6. June\n7. July           8. August         9. September\n10. October       11. November      12. December')  
    print("")
    
def get_Month():
    while True:
        try:
            month = int(input("Enter Month of Travel:"))
            if (month < 1) or (month > 12):
                print("Please select an option between 1 and 12.")
                continue
        except ValueError:
            print("Invalid Month. Try again!")
        else:
            return month
        
def get_Month_CostFactor(month):
    if (month == 1):
        return "January", 0.75
    elif (month ==2):
        return "Febraury", 0.80
    elif (month ==3):
        return "March", 0.90
    elif (month ==4):
        return "April", 1.1
    elif (month ==5):
        return "May", 1.2
    elif (month ==6):
        return "June", 1.25
    elif (month ==7):
        return "July", 1.30
    elif (month ==8):
        return "August", 1.30
    elif (month ==9):
        return "September", 1
    elif (month ==10):
        return "October", 0.90 
    elif (month ==11):
        return "November", 0.85
    elif (month ==10):
        return "December", 1.2
        
#######   Estimation Based on Island Selected
    
def get_IslandCostFactor(islandName): 
    
    if (islandName == "Oahu"):
        return 1
    elif (islandName == "Mauii"):
        return 1.25
    elif (islandName == "Big Island"):
        return 0.8
    elif (islandName == "Kauii"):
        return 0.9    
    
  
# Estimation Based on Star level of Property Selected
        
def print_PropertyStar():
    # Travel Selections for Hawaii Islands
    print("Select your preferred Star Level:")
    print("-----------------------------------")
    print(f'1. 1 Star        2. 2 Stars       3. 3 Stars        4. 3.5 Stars\n5. 4 Stars       6. 4.5 Stars     7. 5 Stars        8. 6 Stars')  
##    print("")

def get_PropertyStar():
    # Get Islands selection
    while True:
        try:
            selection = float(input("Enter Property Star "))
            if (selection < 1) or (selection > 7):
                print("Please select an option between 1 and 5.")
                continue
        except ValueError:
            print("Invalid Selections. Try again!")
        else:
            return selection
    
def get_PropertyCostFactor(starNumber):
    if (starNumber == 1):
        return 50
    elif (starNumber == 2):
        return 80
    elif (starNumber == 3):
        return 120
    elif (starNumber == 3.5):
        return 150
    elif (starNumber == 4):
        return 180
    elif (starNumber == 4.5):
        return 220
    elif (starNumber == 5):
        return 300
    elif (starNumber == 6):
        return 600

# Applying Tax to Hotel Stays. Tax Rate varies as per island selected

#def get_IslandHotelTaxRate(islandName): 
#    
#    if (islandName == "Oahu"):
#        return 14.96
#    else:
#        return 14.41
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    