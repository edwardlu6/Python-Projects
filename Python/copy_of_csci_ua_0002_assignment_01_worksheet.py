# -*- coding: utf-8 -*-
"""Copy of CSCI-UA.0002 Assignment 01 Worksheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Spv1pPsLE7JCkZ1rCCSykntCkItbYe5u

# CSCI-UA.0002 Assignment 01 Worksheet

This is a Python "Notebook" which contains text and code packaged up into a single document.  

**To get started click the File menu and select Save.  This will allow you to edit this document and will cause the system to save a copy of this notebook into your own Google account.**

For this assignment you will be working through a series of challenges. After each challenge you will see some space for you to write code - this is where you should type your solution to the that particular challenge.

When you are finished you should click the File menu and select Download.  Download BOTH a copy of the .ipynb file AND the .py file.  Submit these files to Brightspace under the "Assignment 01" category.

# Challenge #1

Create 5 variables to store the following pieces of information

1.   Your first name
2.   Your last name
3.   Your class year (Freshman, Sophomore, Junior, Senior, etc.)
4.   Your age (whole number)
5.   Your major

Use valid, descriptive variable names (i.e. the variable name 'x' is not descriptive!)

Once you've created your variables write a program that uses those variables to generate the following output.  Your output should match the sample output here using your own information.

```
Hello, my name is Jane Doe.
I am currently a Senior at NYU.
I am a 20 year old Computer Science major.
```
"""

# Write your solution to Challenge #1 here.  
# Use the "run" button to the left to execute your program
first_name = "Edward"
last_name = "Lu"
class_year = "Freshman"
age = "18"
major = "Computer Science/Math"
print("Hello, my name is", first_name, last_name+".")
print("I am currently a", class_year, "at NYU.")
print("I am a", age, "year old", major, "major.")

"""# Challenge #2

Given the following variables, write a SINGLE call to the print function that generates the following output.  



```
Fruit   Amount
Apple   12
Pear    72
Peach   6
```




Hint: you may need to use the sep and end keyword arguments, as well as escape characters ("\n" and "\t")
"""

column_1 = "Fruit"
column_2 = "Amount"
fruit_1 = "Apple"
amount_1 = 12
fruit_2 = "Pear"
amount_2 = 72
fruit_3 = "Peach"
amount_3 = 6

# you may ONLY use a single call to the print function as part of this program,
# and you MUST use the variables above - you cannot use string literals
# as part of this program
print(column_1,"\t",column_2,"\n"+fruit_1,"\t",amount_1,"\n"+fruit_2,"\t",amount_2,"\n"+fruit_3,"\t",amount_3) # <- use this function call to print your output

"""# Challenge #3

For this problem you will break down the steps of an everyday activity into an algorithmic process and write a basic Python program that prints each step of your algorithm.

Think about a routine activity — it can be anything from buying lunch to brushing your teeth — and break it down into an algorithm. Make a detailed list of the steps involved in this activity. Your procedure should be at least 10 steps long and pay attention to the subconscious motions involved in the activity.

Assign each individual step of your algorithmic process to its own variable. Then, print all of the steps to the screen using these variables along with the print function. Your program should also include at least one code comment.
"""

# write your algorithm here
# A list of steps of buying coffe in Starbucks
first_thing = "I looked at the menu" # usually on a screen 
second_thing = "and thought about the price of each kind of coffee"
third_thing = "Then I considered the calories of the coffee" # I don't like high-calories
fourth_thing = "and thought about the flavor of the coffee"
fifth_thing = "I chose to buy latte" # because it is very popular
sixth_thing = "So I talked to the staff" # to buy latte
seventh_thing = "The staff asked how I paid" 
eighth_thing = "I chose to pay with dining dollar"
ninth_thing = "I gave her my name" # she wrote my name on a cup
tenth_thing = "And then I waited until my coffee is ready"
eleventh_thing = "I got my coffee and walked out the door"
print(first_thing, second_thing+".", third_thing, fourth_thing+".", fifth_thing+ ".", sixth_thing+".", seventh_thing+".", eighth_thing+".", ninth_thing+".", tenth_thing+".", eleventh_thing)
