# challenge problem

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
dup_list = []

for file in file_list:
    if file in dup_list:
        print("duplicate found")
        break
    dup_list.append(file)
    print(file)
else:
    print("All files are unique")
