'''
Promopts the user for a credit card number and checks if it is a valid number
and which company it is made by 
Hina Sekine 
'''

# user input 
creditNum = input("Number: ")
while creditNum.isdigit() == False:
    creditNum = input("Number: ")

# multiplies every other number by 2 and stores them in an array 
everyOtherMultiply = ''
for i in range(len(creditNum) - 2, -1, -2):
    everyOtherMultiply = everyOtherMultiply + str(int(creditNum[i]) * 2)

# adds the products' digits together
productDigitSum = 0
for i in everyOtherMultiply:
    productDigitSum = productDigitSum + int(i)

# adds all the digits that weren't multiplied by 2 together
notMultipliedSum = 0
for i in range(len(creditNum) - 1, -1, -2):
    notMultipliedSum = notMultipliedSum + int(creditNum[i])

# check sum is the products' digit sum and the not multipled sum 
checkSum = productDigitSum + notMultipliedSum

# checks if the card is valid by (check sum) modulo 10 == 0 
if checkSum % 10 == 0:
    valid = True
else:
    valid = False

# identifies which company the card belongs to
if valid:
    first2Digits = creditNum[:2]
    if (len(creditNum) == 15) and (first2Digits in ['34', '37']):
        print('AMEX')
    elif (len(creditNum) == 16) and (first2Digits in ['51', '52', '53', '54',
                                                           '55']):
        print('MASTERCARD')
    elif (len(creditNum) in [13, 16]) and (first2Digits[0] == '4'):
        print('VISA')
    else:
        print('No Company Identified')
else:
    print('INVALID')
