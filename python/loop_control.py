# looo control statements, break, continue, pass

# break

for i in range(1, 10):
    if(i == 5):
        pass
    
    print("number: ", i)

days = ['sat','mon','sun','tues', 'wed', 'friday', 'thrus']

for day in days:
    if day == 'sat' or day == 'sun':
        continue
    print(day)

weekends = ['sat','sun']
for day in days:
    if day in weekends:
        continue
    print(day)

# using else with for loop


for i in (1,2,3):
    print(i)
else:
    print("end")

# else only make sense if we combined it with break

for i in (1,2,3):
    if i == 2:
        break
    print(i)
else:
    print("loop not completed")

for i in (1,2,3):
    if i == 2:
        break
    print(i)

print("loop not completed")

