import csv

file = 'wk2_test1_in.csv'

file_my = open(file, 'r')
csv_reader = csv.reader(file_my)

lists_from_csv = []

for row in csv_reader:
    lists_from_csv.append(row)

lists_from_csv_2 = lists_from_csv.copy()

i = 0
j = 0
for row_items in lists_from_csv_2:
    i = 0
    for item in row_items:
        if len(item) < 10:
            missing = 10 - len(item)
            item = item + (missing * " ")
            if '\n' in item:
                item = ""
        elif 10 < len(item) < 15:
            item = item[:15]

        else:
            item = item[:15]
        row_items[i] = item
        i += 1
    lists_from_csv_2[j] = row_items
    j += 1

with open('wk2_test1_out.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lists_from_csv_2)
