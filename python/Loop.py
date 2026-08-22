# loops

for i in (1,2,3,4,5):
    print(f"round: {i}")

items = (1,2,3)
for item in items:
    print(f"round {item}")

items = [1,2,3,"hello"]

for item in items:
    print(f"this is : {item}")

items = "python"
for item in items:
    print(f"letter: {item}")

for i in range(2, 10, 2):
    print(f"number is : {i}")

scores = [80,50,60,75]

total = 0

for score in scores:
    total = total + score
    print(f"current total: {total}")

print(total)

files = ['  report.csv ', 'DATA.csv  ', 'final.TXT']
new_file = []
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"processing {file}")
    new_file.append(file)
print(new_file)


for i in range(1,11):
    print(f"7 x {i} = {7 * i}")

a ="*"
for i in range(1,7):
    print(f"{a * i}")