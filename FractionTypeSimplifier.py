# Description: 
'''This program helps the elementary school teacher to teach students about different types fractions andnhow to simplyfy the fractions. It takes the numerator and 
denominator from the user and sort the fractions into three types. Which are: Proper fractions, Improper fractions, and Mixed fractions proper fraction:
numerator<denominator. Improper fraction: numerator>=denominator. Mixed fractions: Whole number+properfraction.'''

import math 
#importing math module.
numerator = int(input("Enter a numerator: Value must be greater than 0: "))
if numerator <=0:
    numerator = int(input("Please re-enter the numerator. Value must be greater than 0: "))
#Here we need both the numerator and the denominator to be greater than zero. 
denominator = int(input("Enter a denominator: Value must be greater than 0: "))
if denominator <=0:
    denominator = int(input("Please re-enter the denominator. Value must be greater than 0: "))
#Here we need both the numerator and the denominator to be greater than zero.
gcd = math.gcd(numerator, denominator)
# Here we are finding the greatest common divisor of numerator and denominator.
if numerator<denominator:
    print(f'{numerator} / {denominator} is a proper fraction.')
    if gcd == 1:
        print("This proper fraction cannot be reduced any further.")
    else:
        numerator = int(numerator/gcd)
        denominator = int(denominator/gcd)
        print(f'This proper fraction can be reduced to: {numerator} / {denominator}')
#As I said in the description of the code if the fraction has numerator<denominator it is a Proper fraction and if its gcd is 1 it cannot be reduced any further.
else:
    print(f'{numerator} / {denominator} is an improper fraction')
    if gcd == 1:
        print("This improper fraction cannot be reduced any further.")
    else:
        new_numerator = int(numerator/gcd)
        new_denominator = int(denominator/gcd)
        print(f'This improper fraction can be reduced to: {new_numerator} / {new_denominator}')
 #If anything else it is a improper fraction and if its gcd is 1 it cannot be reduced any further.       
    remainder = numerator%denominator
    quotient = numerator//denominator
    remainder_gcd = math.gcd(remainder, denominator)
    if remainder_gcd == 1:
        if remainder == 0:
            whole_number = numerator//denominator
            print(f'The whole number is {whole_number}')
 # If the remainder is zero when we divide numerator by denominator then it is an whole number.           
        else:
            print(f'The mixed number is {quotient} and {remainder} / {denominator}')
 #If it has a remainder and a quotient it is mixed number.           
    else:
        new_remainder = int(remainder/remainder_gcd)
        new_denominator = int(denominator/remainder_gcd)
        if remainder == 0:
            whole_number = numerator//denominator
            print(f'The whole number is {whole_number}')
        else:
            print(f'The mixed number is {quotient} and {new_remainder} / {new_denominator}')
#It prints out the quotient and the new remainder divided by new denominator.

