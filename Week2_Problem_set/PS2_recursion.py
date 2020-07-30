#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:17:25 2020
Say you've made a $5,000 purchase on a credit card with an 
18% annual interest rate and a 2% minimum monthly payment rate. 
If you only pay the minimum monthly amount for a year, 
how much is the remaining balance?

@author: Mukut Ranjan Kalita
"""

def rem_balance(balance,annualInterestRate,monthlyPaymentRate,month):
    balance=balance*(1-monthlyPaymentRate)*(1+annualInterestRate/12)
    print('Month '+str(13-month)+ ' Remaining balance:' + str(round(balance,2)))
    if month<=1:
        return print('balance',round(balance,2),'month ', str(round(month)))
    else:
        return (rem_balance(balance,annualInterestRate,monthlyPaymentRate,month-1))
    
rem_balance(484,0.2,0.04,12)

"""
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not 
change each month, but instead is a constant amount that will be paid each 
month."""

print(" \n ")
print("Now the second problem\n")

import datetime
def min_payment(balance,annualInterestRate):
    min_pay=0
    bal=1
    while bal>=0:
        bal=balance
        for i in range(12):
            bal = (bal-min_pay)*(1+annualInterestRate/12.0)
            #print('balance ',bal)
        min_pay+=1
    print('Lowest Payment', min_pay-1)
begin_time = datetime.datetime.now()
min_payment(320000,0.2)    
print(datetime.datetime.now()-begin_time)








