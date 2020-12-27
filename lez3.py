dates=[]
values=[]
realvalues=[]
values2=[]

my_file=open("shampoo_sales.csv","r")

for i in my_file:
    elements=i.split(",")
    dates.append(elements[0])
    values.append(elements[1])

dates.pop(0)
values.pop(0)

for i in values:
   realvalues.append(i[0:-1])

for i in realvalues:
    values2.append(float(i))

s=0
for i in values2:
    s=s+i

print("La somma è {}".format(s))

print(float(ciao))