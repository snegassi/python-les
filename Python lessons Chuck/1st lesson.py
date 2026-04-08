
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
  discount = 3
  print('User qualifies for membership discount')
else:
  print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)



if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = extra_charges + base_price + service_charges - discount
    print('Final price of ticket:', final_price)
else:
  print('Ticket booking failed due to restrictions')

  """
  Let's walk through the if condition step by step to see why it evaluates to True:

Your if condition is: age >= 21 or age >= 18 and (show_time != 'Evening' or is_member)

Given the initial values:

age = 21
show_time = 'Evening'
is_member = False
Let's evaluate each part:

age >= 21: 21 >= 21 is True

age >= 18: 21 >= 18 is True

show_time != 'Evening': 'Evening' != 'Evening' is False

is_member: This is False

Now, substitute these back into the if condition, keeping in mind operator precedence (AND is evaluated before OR):

True or True and (False or False)

First, evaluate the innermost parentheses: (False or False) which is False. The condition becomes: True or True and False

Next, evaluate the and operation: True and False which is False. The condition becomes: True or False

Finally, evaluate the or operation: True or False which is True.

Since the entire if condition evaluates to True, the code inside the if block is executed, and the else block is skipped. This is why you see the "Ticket booking condition satisfied" message and the service charges.
  """