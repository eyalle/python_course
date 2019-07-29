import time, datetime

class Time:
    # def __init__(self, a, b):
    #     self.a = int(a)
    #     self.b = int(b)
    def get_time(self):
        return time.time()

class Date(Time):
    def get_date(self):
        return datetime.date.today()

if __name__ == "__main__":
    d = Date()
    t = Time()
    print(d.get_time())
    print(d.get_date())

    print(f'time is {t.get_time()}')