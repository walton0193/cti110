# Sales Prediction - get projected total sales
# 18 February 2020
# CTI-110 P2T1 - Sales Prediction
# Kenneth Walton
#

total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales

profit = total_sales * 0.23

# Display the profit
print('The profit is $', format(profit, ',.2f'))
