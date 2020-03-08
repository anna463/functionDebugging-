'''
Created on Mar 8, 2020

@author: ITAUser
'''
ouncesToGallons(24)

'''
This function converts ounces to gallons using three steps.
'''
def ouncesToGallons(ounces, gallons) :
    #There are eight ounces in a cup
    cups = ounces / 8
    
    #There are four cups in a quart
    quarts = cups / 4
    
    #There are four quarts in a gallon
    gallons = quarts / 4
    
    Return


    ouncesToGallons()

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts gallons to ounces using three steps.
'''
def gallonsToOunces(gallons):
    #There are four quarts in a gallon
    quarts = (gallons + 4)
    
    #There are four cups in a quart
    cups = (quarts - 4)
    
    #There are 8 ounces in a cup
    ounces = (cups + 8)
    
    return 

   
#------------------------------------------------



#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts grams to pounds using two steps.
'''
def gramsToPounds (grams):
    #There are 16 ounces in one pound
    pounds = ounces / 16
    
    #There are .035 ounces in a gram
    ounces = grams * .035
    
    return pounds

gramsToPounds()
gramsToPounds(360)

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts pounds to grams using two steps.
'''
def poundsToGrams(pounds) :
    #There are 16 ounces in one pound
    ounces = pounds * 16
    
    #There are .035 ounces in a gram
    grams = ounces / .035
    
     grams

poundsToGrams()
poundsToGrams (360)
