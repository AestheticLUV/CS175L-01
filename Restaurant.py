#CS-175L-01
#Jarek Torres
#Restaurant

#List of restaurants 
#Joe's Gourmet Burgers - Vegetarian: No , Vegan: No , Gluten-Free: No
#Main Street Pizza Company - Vegetarian: Yes , Vegan: No , Gluten-Free: Yes
#Corners Cafe - Vegetarian: Yes , Vegan: Yes , Gluten-Free: Yes
#Mama's Fine Italian - Vegatarian: Yes , Vegan: No , Gluten-Free: No 
#The Chef's Kitchen - Vegatarian: Yes , Vegan: Yes , Gluten-Free: Yes

#ask wheather any members of your party are Vegetarian,Vegan, or Gluten-Free


vegetarian = input("Is anyone in your party a vegetarian? ")
if vegetarian == "yes":
    vegetarian = True  #does this if condition is true      
else:
    vegetarian = False  #does this if condition is false 


vegan = input("Is anyone in your party a vegan? ")
if vegan == "yes":
    vegan = True
else:
    vegan = False

gluten_free = input("Is anyone in your party gluten-free? ")
if gluten_free == "yes":
    gluten_free = True
else:
    gluten_free = False

print("Here are your restaurant choices:")

if vegetarian == False:
    if vegan == False:
        if gluten_free == False:
            print("Joe's Gourmet Burgers") 


if vegan == False:
    if gluten_free == False:
        print("Mama's Fine Italian")

if vegan == False:
    print("Main Street Pizza Company")



print("Corner Cafe")
print("The Chef's Kitchen ")