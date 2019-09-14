def main():
	import csv

	classes = {'Cinthol Soap': 10, 'Coconut Oil': 30, 'Colgate:Active Salt-200g': 40, 'Colgate:Active Salt-50g': 10, 
	'Ghadi Detergent Soap': 10,'Lemon Facewash': 80,'Neutrogena Moisturizer': 220}
	reader = csv.reader(open('D:/Object Recognition/usr_interface/data/hitlist3.csv', 'r'))
	detected = {}
	for row in reader:
		index, value = row
		detected[index] = value
	print(detected)
	total = 0
	for key in detected:
		if key in classes:
			print(key, ":", classes[key],"Rupees")
			total += classes[key]
	print("Total : ",(total),"Rupees")

if __name__ == '__main__':
	main()