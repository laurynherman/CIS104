pen_amnt = int(input('How many pennies do you have?  '))
nickl_amnt = int(input('How many nickels do you have?  '))
dime_amnt = int(input('How many dimes do you have?  '))
qurt_amnt = int(input('How many quarters do you have?  '))
hlf_dlr_amnt = int(input('How many half dollars do you have?  '))
dollar = int(input('How many dollars do you have?  '))

pen_val = float(pen_amnt * .01)
nickl_val = float(nickl_amnt * .05)
dime_val = float(dime_amnt * .1)
qurt_val = float(qurt_amnt * 0.25)
hlf_dlr_val = float(hlf_dlr_amnt * .50)
dollar = int(dollar * 1.00)

print('You have', pen_amnt, 'pennies.')
print('You have', nickl_amnt, 'nickels.')
print('You have', dime_amnt, 'dimes.')
print('You have', qurt_amnt, 'quarters')
print('You have', hlf_dlr_amnt, 'half dollars')
print('You have', dollar, 'dollars')

print('The value of all your coins is', pen_val + nickl_val + dime_val + qurt_val + hlf_dlr_val + dollar )


