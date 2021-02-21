class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
    def get_data(self):
        epoch=[]

        myfile=open(self.name,"r")
        for i in myfile:
            elements=i.split(",")
            if elements[0]!="epoch":
                elements[0]=int(elements[0])
                elements[1]=float(elements[1])
                epoch.append(elements)
        pass
        myfile.close()

        return epoch

def hourly_trend_changes(series):
    epoch=[]
    values=[]
    inv=[]
    inv2=[]
    hours=[]
    l1=[]
    inv2.append(0)
    for i in series:
        epoch.append(i[0])
        values.append(i[1])

    for i in range(1,len(values)):
        if values[i]>values[i-1]:
            inv.append(1)
        elif values[i]==values[i-1]:
            inv.append(0)
        else:
            inv.append(-1)
    
    cycle=inv[0]
    
    for i in range(0,len(inv)):
        if inv[i]==0:
            inv2.append(0)
        elif inv[i]==cycle:
            inv2.append(0)
        else:
            inv2.append(1)
            cycle=inv[i]

    for i in epoch:
        hours.append(int(i/3600))
    
    for i in hours:
        if i not in l1:
            l1.append(i)

    


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
hourly_trend_changes(time_series)