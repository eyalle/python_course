
def get_time(time_in_seconds):
    import datetime
    time_str = str(datetime.timedelta(time_in_seconds))
    time_fractions = time_str.split(":")
    time_str = f'{time_fractions[0]}h : {time_fractions[1]}m : {time_fractions[2]}s'
    return time_str

class Athlete:
    def __init__(self, name, weight, power, speed, endurance):
        self.name = name
        self.power = float(power)
        self.speed = int(speed)
        self.weight = float(weight)
        self.endurance = int(endurance)
        if (self.endurance < self.speed):
            self.endurance += 3

class Runner(Athlete):
    def __init__(self, name, weight=60.0, power=0, speed=0, endurance=0):
        Athlete.__init__(self, name, weight, float(power), int(speed), int(endurance))
        self.power += (self.weight * 0.1)
        self.speed += 25
        self.endurance += 8


    def get_duration(self, distance):
        acceleration = self.power / self.weight
        top_speed = self.speed
        time_to_reach_top_speed = top_speed / acceleration
        distance_to_top_speed = top_speed * time_to_reach_top_speed / 2

        if distance == distance_to_top_speed:
            duration = time_to_reach_top_speed

        elif distance < distance_to_top_speed:
            duration = (2 * distance / acceleration) ** (1 / 2)

        else:
            deceleration = acceleration
            endurance_speed = self.endurance
            time_to_reach_endurance_speed = top_speed - endurance_speed / deceleration
            distance_to_endurance_speed = top_speed * time_to_reach_endurance_speed / 2

            if distance == distance_to_top_speed + distance_to_endurance_speed:
                duration = time_to_reach_endurance_speed
            elif distance < distance_to_top_speed + distance_to_endurance_speed:
                duration = time_to_reach_top_speed + (2 * (distance - distance_to_top_speed) / deceleration) ** (1 / 2)
            else:
                time_to_reach_distance = (distance - (distance_to_top_speed + distance_to_endurance_speed)) / endurance_speed
                duration = time_to_reach_top_speed + time_to_reach_endurance_speed + time_to_reach_distance
        return duration
    
    def run(self, distance):
        import time
        t = self.get_duration(distance)
        # time.sleep(t)
        return self.name

class Sprinter(Runner):
    def __init__(self, name, weight=70.0, power=0, speed=0, endurance=0):
        Runner.__init__(self, name, float(weight), int(power), int(speed), int(endurance))
        self.power += (0.75 * self.weight)
        self.speed += 15
        self.endurance += 1

class MarathonRunner(Runner):
    def __init__(self, name, weight=55.0, power=0, speed=0, endurance=0):
        Runner.__init__(self, name, float(weight), int(power), int(speed), int(endurance))
        self.power /= 1.1
        self.speed -= 3
        self.endurance += 7
        self.speed = 8 if (self.speed < 8) else self.speed
        self.speed = self.endurance + 1 if (self.speed < (self.endurance + 1)) else self.endurance

def get_durations(distances, athletes):
    for distance in distances:
        for athlete in athletes:
            print(f'{athlete.run(distance)} ran {distance} meters in {get_time(athlete.get_duration(distance))}')

if __name__ == "__main__":
    runr = Runner("run", 90, 15, 30)
    sprt1 = Sprinter("sprnt1", 90, 15, 30)
    sprt2 = Sprinter("sprnt2", 80, 10, 25)
    mrtn = MarathonRunner("mrtn", 50, 6, 7)
    # print('getting running time..')
    # print(f'{runr.run(100)} ran for {runr.get_duration(100)}')
    distances = (100, 200, 800, 1600, 5000, 20000)
    athletes = (runr, sprt1, sprt2, mrtn)
    get_durations(distances, athletes)



