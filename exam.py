class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
    def get_data(self):
        pass


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()