#Links used for help: https://codescracker.com/python/program/python-program-make-calculator.htm
#https://www.programiz.com/python-programming/examples/calculator
#


import calculator

  #Choose operation:

while True:
      print('''Please choose the operation you would like to use:  
      '+' = addition
      '-' = substraction
      '*' = multiplication
      '/' = division
      'X' = exit
      'x' = exit
      ''')
      choice = int(input('Enter your operation choice:'))
      if (choice>=1 and choice<=4):
        print(('Enter first number: ')        #Choose two numbers:
        nmbr1 = int(input())
        print('Enter your second number: ')
        nmbr2 = int(input())
        if choice == '+':
          res = nmbr1 + nmbr    #'res' is short for response
          print('Answer = ', res)
        elif choice == '-':
          res = nmbr1 - nmbr2
          print('Answer =', res)
        elif choice == '*':
          res = nmbr1 * nmbr2
          print('Answer =', res) 
        else:
          res = nmbr1 / nmbr2
          print('Answer =', res)
      elif choice == 'X', 'x'
             break
      else:
           print('ERROR ERROR ERROR!!!')      