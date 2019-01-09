# Asks the user to choose a passcode

pass_code= int(input('passcode:'))

if pass_code>1000000000 or pass_code<1000:
 print('Invalid passcode.')

  
elif pass_code>=1000 and pass_code<10000000:  # Prints whether the passcode is secure, not secure,
   print('Passcode is not secure.')
 
elif pass_code>=10000000: 
   print('Passcode is secure.')

# or invalid, depending on the number of digits.

else:
  print('Valid')
