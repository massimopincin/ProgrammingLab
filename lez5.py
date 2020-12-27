class CSVFile(): 
    def __init__(self,name):
            self.name = name
    def __str__(self):
        return "CSVFILE {}".format(self.name)
    def get_data(self):
        dates=[]
        values=[]
        values2=[]
        realvalues=[]
        file=open(self.name,"r")

        for i in file:
            elements=i.split(",")
            dates.append(elements[0])
            values.append(elements[1])
        
        dates.pop(0)
        values.pop(0)

        for i in values:
            realvalues.append(i[0:-1])
        
        for i in realvalues:
            try:
                values2.append(float(i))
                print(i)
            except:
                print("ERROR: i")
        

myfile=CSVFile("shampoo_sales.csv")

try:
    myfile.get_data()
except:
    print("hell no")
    import sys
    sys.exit()