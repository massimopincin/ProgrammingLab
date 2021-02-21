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
    for i in series:
        epoch.append(i[0])
        values.append(i[1])

    





time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
hourly_trend_changes(time_series)