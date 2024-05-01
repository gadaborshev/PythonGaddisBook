# Get required future value
future_value = float(input('Enter required future value: '))

# Get annual interest rate
rate = float(input('Enter annual interest rate: '))

# Get the number of years the money has been kept in the account
years = int(input('Enter number of years the money has been kept in the account: '))

# Calculate the amount required to deposit into the account
present_value = future_value / (1.0 + rate) ** years

# Show the amount required to deposit into the account
print('You will need to deposit the amount:', present_value)