
# Q.1

# Explain what this program does
# for number in range(100):
#  output = 'o' * number
#  print(output)

# Ans.1


# This code creates a set of lines, each of which contains a string of "o" characters.
# Each line contains between 1 and 99 "o" characters.

# For Example:

# The first line contains 1 'o' character.
# The second line contains 2 'o' characters.
# The third line contains 3 'o' characters.
# The fourth line contains 4 'o' characters.
# [continued to reach 99 'o' in one line]

# Practice_Only
for num in range(100):
 result_output = 'o' * num
 print(result_output)







# Q.2
# def calculate_vat(amount):
#  amount * 1.2
# total = calculate_vat(100)
#  print(total)


#Ans.2

def calculate_vat(amount):
 total = amount * 1.2
 return total

total = calculate_vat(100)
print(total)

# practice_only
def calculate_vat(raqam):
  kul = raqam * 2.1
  return kul

kul =calculate_vat(100)
print(kul)








# Q.3
#
# Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes,
# food, events etc).
# It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.
# For example (input):
# Item_1_name = ‘Trainers’
# Item_1_price = 50.45
# Item_2_name = ‘T-shirt
# Item_2_price = 12
# Output:
# Trainers …….50.45
# T-shirt………..12.00
# TOTAL 62.45

# Ana.3

item_1_name = input('item_1_name =', )
item_1_cost = float(input('item_1_cost =', ))
item_1_quantity = float(input('item_1_quantity =', ))
item_2_name = input('item_2_name =', )
item_2_cost = float(input('item_2_cost =', ))
item_2_quantity = float(input('item_2_quantity =', ))
item_3_name = input('item_3_name =', )
item_3_cost = float(input('item_3_cost =', ))
item_3_quantity = float(input('item_3_quantity =', ))

print( 'total_cost_of ' + str(item_1_name), 'is ',  item_1_quantity * item_1_cost)
print( 'total_cost_of ' + str(item_2_name), 'is ',  item_2_quantity * item_2_cost)
print( 'total_cost_of ' + str(item_3_name), 'is ',  item_3_quantity * item_3_cost)