name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False

ccard = input("Please enter the updated credit card number: ")
num = '1234 4334 1001 0000'
if verify_credit_card(num) == True:
  print('VALID')
  account_balance -= 39
else:
  print('INVALID')


help()
increase_age()
print(age)
