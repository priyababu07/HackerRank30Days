"""
Author: Priya Babu

Date  : 9/03/2023

DEscription:Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer.
"""

import math
import os
import random
import re
import sys



def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost/100*tip_percent
    tax = tax_percent/100*meal_cost
    total_cost=meal_cost+tip+tax
    print(round(total_cost))
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
