import csv

classes = {'Cinthol Soap': 10, 'Coconut Oil': 30, 'Colgate:Active Salt-200g': 40, 
'Colgate:Active Salt-50g': 10,'Ghadi Detergent Soap': 10,'Lemon Facewash': 80,'Neutrogena Moisturizer': 220}
reader = csv.reader(open('hitlist.csv', 'r'))
detected = {}
for row in reader:
   index, value = row
   detected[index] = value
print(detected)