import sys, random
sys.path.append("../../")
from in_class_excercises.date_24_7_19 import inherit
# from exercises.data import get_data

class Measurment:
    def __init__(self, date, run_time):
        self.date = date
        self.run_time = run_time

class Timer(inherit.Date):
    def __init__(self, f, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.operation = f(*self.args, **self.kwargs)
        self.last_measurement = Measurment(self.get_date(), self.get_time())
    
    def start(self):
        start_time = self.get_time()
        self.last_measurement.date = self.get_date()
        result = self.operation(*self.args, **self.kwargs)
        self.last_measurement.run_time = self.get_time - start_time
        return(result)



if (__name__ == "__main__"):
    from random import randint
    sys.path.append("../../../")
    from exercises.level_1.oop.athlete import Sprinter
    from exercises.data import get_data
    
