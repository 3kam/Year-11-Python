#Define the list of pets
name = ['Foxxy', 'Bella', 'Hootie']
#Define the list of animal cateogory corresponding to the pet names
animal_category = ['Dog', 'Rabbit', 'Blowfish']
#Define the pet age corresponding
age = [5,8,34]
#Define if the animal was previouslly vaccinated
unvaccinated = ['Unvaccinated', 'Unvaccinated', 'Unvaccinated'] #All pets were initally unvaccinated
#Define Vaccinate the unvaccinated to vaccinated pets
vaccinated = ['Vaccinated', 'Vaccinated', 'Vaccinated'] #All pets now given treatment and now vaccinated


for i in range(len(name)): #Iterates  over the indices corresponding to the names list
    print('Pet Name: ' , name[i]) #Display pet names
    print('Animal Category: ' , animal_category[i]) #Display pets category
    print('Age:' , age[i]) #Display pets age
    print('Vaccinated Status: ' , unvaccinated[i]) #Display initial pet vaccination status
    print('Updating Vaccination Status: ' , vaccinated[i]) #Display updated pet status
