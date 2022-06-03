from optimal_change import optimal_change
#The following Test cases should return true

print("1:", optimal_change(62.13, 100)=="The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51,50)=="The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(99.99,100)=="The optimal change for an item that costs $99.99 with an amount paid of $100 is 1 pennie.")
print("4:", optimal_change(53.27,250)=="The optimal change for an item that costs $53.27 with an amount paid of $250 is 1 $100 bill, 1 $50 bill, 2 $20 bills, 1 $5 bill, 1 $1 bill, 2 quarters, 2 dimes, and 3 pennies.")
print("5:", optimal_change(23.17,97.99)=="The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickle, and 2 pennies.")
print("6:", optimal_change(37.78,40)=="The optimal change for an item that costs $37.78 with an amount paid of $40 is 2 $1 bills, 2 dimes, and 2 pennies.")
print("7:", optimal_change(23.17,97.99)=="The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickle, and 2 pennies.")
print("8:", optimal_change(5.07,100)=="The optimal change for an item that costs $5.07 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 4 $1 bills, 3 quarters, 1 dime, 1 nickle, and 3 pennies.")
print('9:', optimal_change(100, 63.13)=="The item cost is $100 and you only have $63.13. You need $36.87 to afford this item.")
print('10:', optimal_change(63.13, 63.13)=='The item cost was $63.13 and you made an exact payment of $63.13. There is no change to return')
print('11:', optimal_change(90, 100)=='The optimal change for an item that costs $90 with an amount paid of $100 is 1 $10 bill.')
