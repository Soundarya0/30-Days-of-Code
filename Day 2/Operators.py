#Input Format

#There are  lines of numeric input:
#The first line has a double,  (the cost of the meal before tax and tip).
#The second line has an integer,  (the percentage of  being added as tip).
#The third line has an integer,  (the percentage of  being added as tax).

#Output Format

#Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).


#Sample Input

#12.00
#20
#8

#Sample Output

#15

#!/bin/python3

import sys
import math
import os


# Complete the solve function below.
if __name__ == "__main__" :
    
 #The strip() removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).
    meal_cost = float(input().strip()) 
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

tip_amount = meal_cost * tip_percent / 100

tax_amount = meal_cost * tax_percent / 100

total_Cost = round(meal_cost + tip_amount + tax_amount)

print(str(total_Cost))
