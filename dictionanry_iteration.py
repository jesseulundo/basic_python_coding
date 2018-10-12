"""
Iteration over dictionaries
"""

capitals = {'USA': 'Washington, D.C.',
			'China': 'Beijing',
			'France': 'Paris',
			'England': 'London',
			'Italy': 'Rome',
			'Russia': 'Moscow',
			'Australia': 'Canberra',
			'Peru': 'Lima',
			'Japan': 'Tokyo'}
			
print("Direct Iteration")
print("================")

for country in capitals:
	print("{}, {}".format(capitals[country], country))
	
print("")

print("Iteration over Keys")
print("====================")

for country in capitals.keys():
	print("{}, {}".format(capitals[country], country))
	
print("Iteration over Values")
print("====================")

for country in capitals.keys():
	print("Capital city: {}".format(country))
	
print("")

print("Iteration over Items")
print("====================")

for country, city in capitals.items():
	print("{}, {}".format(city, country))
	
print("")

print("Checking Membership")
print("====================")

print('England' in capitals)
print('Lima' in capitals)
print('Moscow' in capitals)
print('Italy' in capitals)
print('Houston' in capitals)
print('Beijing' in capitals)