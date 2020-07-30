#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:32:40 2020

@author: Mukut Ranjan Kalita
"""

"""
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not 
change each month, but instead is a constant amount that will be paid each 
month. Use bisection search.
"""
import datetime
def min_payment(balance,annualInterestRate):
    lower_pay = balance/12.0
    upper_pay = balance*(1+annualInterestRate)/12
    min_pay = lower_pay
    bal=balance
    j=0
    while abs(bal)>0.001:
        bal = balance
        min_pay = (upper_pay+lower_pay)/2.0 
        for i in range(12):
            bal = (bal-min_pay)*(1+annualInterestRate/12.0)
        if bal > 0.001:
            lower_pay = min_pay
        elif bal<-0.001:
            upper_pay = min_pay
        else:
            break
        j+=1
    print('Lowest Payment', min_pay,'balance:',bal)

begin_time = datetime.datetime.now()
min_payment(320000,0.2)    
print("time to complete",datetime.datetime.now()-begin_time)