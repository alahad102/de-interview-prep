
# for x in range(3):
#     for y in range(2):
#         for z in range(2):
#             print(f"({x},{y},{z})")

# use case 1

colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']

for color in colors:
    for size in sizes:
        print(f"COLOR: {color}, Size: {size}")

# use case 2

years = [2026, 2027]
months = ['jan', 'feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")
