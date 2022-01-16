csv = 'Eric,John,Michael,Terry,Graham,TerryG,Brian'
friends_list = []
splitcsv = csv.split(',')


for name in splitcsv:
    friends_list.append(name)

print(friends_list)