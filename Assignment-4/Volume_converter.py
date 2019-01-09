# Asks the user for a measurement in cups.
# This may be a fractional number.
cups= float(input('Enter the amounts in cups:'))


# Asks the user for a unit to convert to from the following:
# oz, pint, tbsp, ml
convert_unit= str(input('Enter the unit to convert to (oz/pint/tbsp/ml):'))

if convert_unit=='oz':
  cups=cups*8
  print(str(cups)+ str(convert_unit)+'s')

  
elif convert_unit=='pint':
  cups= cups*0.5
  print(str(cups)+ str(convert_unit)+'s')

  
elif convert_unit=='tbsp':
  cups= cups*16
  print(str(cups)+ str(convert_unit)+'s')

  
else:
 cups= cups*207
 print(str(cups)+ str(convert_unit))


# Converts the measurement to the specified unit.

