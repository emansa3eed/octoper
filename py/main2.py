import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


while True :
    password = int(input())
    if password == 1999 :
        print("Correct")
        break
    else :
        print("Wrong")

# num = int(input("enter a num"))
# flag = False
# if num == 1:
#     print(num ,"is not prime")
# elif num > 1:
#   for i in range(2, num):
#     if (num % i ) == 0:
#      flag = True
#      break
#   if flag :
#    print(num,"is not prime")
#   else:
#    print(num,"is prime")