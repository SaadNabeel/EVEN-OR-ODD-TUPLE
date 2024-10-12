
t1 = (2, 7, 6, 15, 18, 36)
t2=list(t1)

evennumbers = []
oddnumbers = []


for number in t1:
    if number % 2 == 0:
        evennumbers.append(number) 
    else:
        oddnumbers.append(number)

eventuple = tuple(evennumbers)
oddtuple = tuple(oddnumbers)


print("Even numbers tuple:", eventuple)
print("Odd numbers tuple:", oddtuple)
