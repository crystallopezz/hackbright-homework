def incorrect_payment(customer_orders_file):
  '''incorrect_payment should take the file of customers and return if any of the customer did not pay the correct price for melons

    for each customer, 

    find the customer name
    find the numbe of melons purchased
    find how much they paid

    find out how much they should have paid based on the price

    if the amount they paid does not equal the price

    say "customer_name paid $amount_paid, expected $amount_expected"

    otherwise, move on to the next customer'''
  melon_cost = 1.00
  
  #open the file
  customer_orders = open(customer_orders_file)

  #iterate through each line in the file
  for line in customer_orders:

    #split line by "|" to get a list of the tx details
    customer_details = line.split("|")

    #find customer name
    name = customer_details[1]

    #find out how many melons they purchased and turn it into a float
    number_melons_purchased = float(customer_details[2])

    #find out how much they paid and turn it into a float
    paid_amount = float(customer_details[3])

    #find out how much they were supposed to pay
    expected_amount = number_melons_purchased*melon_cost

    #compare how much paid vs expected to see if they don't match
    if paid_amount != expected_amount:
      #if they don't match, print who paid, how much and what they were supposed to pay
      print(f"{name} paid ${paid_amount:.2f}, expected ${expected_amount:.2f}")

  customer_orders.close()

incorrect_payment("customer-orders.txt")