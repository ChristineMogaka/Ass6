print("--------------------------------------------------")
print("--------------CHRISTINE MOGAKA--------------------")
print("----------INTRODUCTION TO PYTHON 2021-------------")
print("----------------ASSIGNMENT 6----------------------")
print("--------------------------------------------------")

import awoc #to check countries
import re #for regex

names = input("Enter full name: ")
country = input("Enter country: ")
gender = str.lower(input("Enter gender(f for female and m for male): "))
phone_number = input("Enter phone number(including country e.g +254..): ")

print(names)
print(phone_number)

#Initialize the AWOC class- create an object.
my_world = awoc.AWOC()

#List of countries in Africa
countries = my_world.get_countries_list_of('Africa')

#Get the exact country code of the country given as input.
real_code = my_world.get_country_phone_code(country)

print(countries)

#Create a list of country codes.
africa_country_codes = []
    
for c in countries:
    country_codes = my_world.get_country_phone_code(c)
    africa_country_codes.append(country_codes)
    
print(africa_country_codes)
#regular expression to return country code.
def phone_regex():
    match = (re.search(r'\+\d{3}', phone_number))
    code = match.group()
    return code[1:] #exclude the + dign
phone_regex()

def test_average():
    global average_score
    

    #use float values
    quiz1 = float(input("Enter quiz1: "))
    quiz2 = float(input("Enter quiz2: "))
    quiz3 = float(input("Enter quiz3: "))
    test1 = float(input("Enter test1: "))
    test2 = float(input("Enter test2: "))
    average_score = (quiz1+quiz2+quiz3+test1+test2)/5
    average_score = round(average_score,2)
    return average_score
   

def participation():
    assignment = int(input("Enter number of assignments submitted (should be between 0 and 10) : "))
    zoom = int(input("Enter number of zoom sessions attended: "))
    activity = str.lower(input("Was the student active (Yes/No): "))
    
    global zoom_score
    global score
    
    if activity == "yes" and zoom <=3:
        zoom_score = zoom *3
    elif activity == "no" and zoom <= 3:
        zoom_score = zoom *1
   
        
    if assignment + zoom_score <= 5:
        score = "Poor"
    elif assignment + zoom_score <= 14:
        score = "Good"
    elif assignment + zoom_score <= 19:
        score = "Excellent"
    else:
        score = print("Not valid")
    
    return score
    

if country in countries: #and phone_regex() == real_code: Use this to validate that phone number is from the country entered
    test_average()
    participation()
    if gender == "m" and average_score >= 80 and score == "Excellent":
        print("Your average score is "+ str(average_score) + " and your participation was "+ str(score) )
        print("You deserve a scholarship")
    elif gender == "f" and average_score >= 76 and score == "Excellent":
        print("Your average score is "+ str(average_score) + " and your participation was "+ str(score) )
        print("You deserve a scholarship")
    else:
        print("Your average score is "+ str(average_score) + " and your paticipation was "+ str(score) )
        print("You are not eligible for a scholarship")
else:
    print("You are not eligible for a scholarship")
   