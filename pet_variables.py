# Define pet details
name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

# Apply updates
age += 1  # Increase age by 1 year
billing_address = '17 Park Street'  # Change address
vaccinated = False  # Update vaccination status
owner_name = 'Alex Jones'  # Update owner name
account_balance -= 25  # Subtract $25 from account balance

# Prompt for updated credit card number
ccard = input("Please enter the updated credit card number: ")

# Display updated details
print(f"Name: {name}")
print(f"Animal Category: {animal_category}")
print(f"Age: {age}")
print(f"Vaccinated: {vaccinated}")
print(f"Credit Card: {ccard}")
print(f"Billing Address: {billing_address}")
print(f"Owner Name: {owner_name}")
# we use the $ to indicate the currency and the .2f to indicate we want our number to format two decimal places.
print(f"Account Balance: ${account_balance:.2f}")