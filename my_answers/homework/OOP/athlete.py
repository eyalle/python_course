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
        power=int(power) + (0.1*weight)
        speed=int(speed) + 25
        endurance=int(endurance) + 8
        power = (float(power)+(0.1*float(weight)))
        Athlete.__init__(self, name, weight, power, speed, endurance)

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
        time.sleep(t)
        return self.name

if __name__ == "__main__":
    runr = Runner("sir", 90, 15, 30)
    print('getting running time..')
    print(f'{runr.run(100)} ran for {runr.get_duration(100)}')
