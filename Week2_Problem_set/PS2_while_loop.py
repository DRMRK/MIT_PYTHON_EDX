#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:40:13 2020

@author: Mukut Ranjan Kalita
"""

def rem_balance(balance,annualInterestRate,monthlyPaymentRate, n=12):
    month=0
    while month <12:
        balance=balance-balance*monthlyPaymentRate
        balance=balance+balance*annualInterestRate/12
        month+=1
        print('Month '+str(month)+ ' Remaining balance:' + str(round(balance,2)))

rem_balance(42,0.2,0.04)