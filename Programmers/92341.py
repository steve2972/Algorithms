from math import ceil


def solution(fees, records):
    list_cars = {}
    def calc_time(old_time, new_time):
        (h, m), (h1, m1) = old_time.split(':'), new_time.split(':')
        h, m = int(h), int(m)
        h1, m1 = int(h1), int(m1)
        return 60 * (h1-h) + m1 - m

    for record in records:
        time, car, _ = record.split(" ")
        if car in list_cars:
            if list_cars[car][2]:   # if is parked
                list_cars[car][0] += calc_time(list_cars[car][1], time)
                list_cars[car][2] = 0
            else:
                list_cars[car][2] = 1
                list_cars[car][1] = time
        else:
            list_cars[car] = [0, time, 1] # (time elapsed, time, in parking)

    for car in list_cars.keys():
        if list_cars[car][2]:
            list_cars[car][0] += calc_time(list_cars[car][1], "23:59")
    times = [list_cars[car][0] for car in sorted(list_cars.keys())]
    answer = [fees[1] + ceil((time - fees[0])/fees[2]) * fees[3] if time >= fees[0] else fees[1] for time in times]
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))