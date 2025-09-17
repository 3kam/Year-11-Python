pet1 = {
'name' : 'Miss Bonnie',
'animal category' : 'Cat',
'age' : 4,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}

pet1['vaccinated'] = 'John Smith'

for item in pet1:
    print(item, ':', pet1[item])
    
pet2 = {
'name' : 'Max',
'animal category' : 'Dog',
'age' : 25,
'vaccinated' : True,
'credit card' : '1234 4435 1245 8715',
'billing address' : '18 Spooner Circuit, North Shore 2582',
'owner name' : 'Adam Jenkins',
'account balance' : 129.95,
}

pet2['vaccinated'] = 'Jane Smith'

for item in pet2:
    print(item, ':', pet2[item])
    
