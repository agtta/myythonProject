import csv

row = ['radek', 'code', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
dict2 = dict(zip(fields, row))
print(dict2)

dict_x = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.10'},
    {'name': 'radek', 'branch': 'coe', 'year': 2, 'cgpa': '9.0'},
    {'name': 'radek', 'branch': 'coe', 'year': 1, 'cgpa': '9'},

]

filename = 'records.csv'
with open(filename, 'w', encoding='utf-8', ) as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict2)


   # csvwriter = csv.writer(csv_f)
   # csvwriter.writerow(row)

