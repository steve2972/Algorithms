def time_to_seconds(t):
    h, m, s = map(lambda x: int(x), t.split(":"))
    return 3600 * h + 60 * m + s

def seconds_to_time(s):
    secs = s % 60
    s //= 60
    m = s % 60
    h = s // 60
    return f"{h:02d}:{m:02d}:{secs:02d}"

def solution(play_time, adv_time, logs):
    adv_duration = time_to_seconds(adv_time)
    video_duration = time_to_seconds(play_time)
    adv_start, max_watched = 0, 0
    if adv_duration == video_duration: return "00:00:00"
    times_best = []
    sec_logs = []
    times_to_check = [0, video_duration-adv_duration]

    for log in logs:
        t1, t2 = map(lambda x: time_to_seconds(x), log.split('-'))
        times_to_check.append(t1)
        sec_logs.append((t1, t2))

    for adv_start in times_to_check:
        sum_watched = 0
        for t1, t2 in sec_logs:
            if adv_start+adv_duration < t1 or t2 < adv_start:
                pass
            else:
                sum_watched += min(adv_start + adv_duration, t2) - max(adv_start, t1)
        if sum_watched > max_watched:
            times_best = [adv_start]
            max_watched = sum_watched
        elif sum_watched == max_watched:
            times_best.append(adv_start)

        adv_start += 1

    answer = seconds_to_time(min(times_best))
    return answer


import numpy as np



def solution_numpy(play_time, adv_time, logs):
    play_sec = time_to_seconds(play_time)
    sec_table = np.zeros(shape=(play_sec+1,), dtype=np.int32)

    for log in logs:
        t1, t2 = map(lambda x: time_to_seconds(x), log.split('-'))
        sec_table[t1:t2] += 1

    adv_sec = time_to_seconds(adv_time)
    total = np.sum(sec_table[:adv_sec])
    max_sec = 0
    maxi = total
    for i in np.arange(1, play_sec - adv_sec + 1):
        # Sliding window
        total += sec_table[i + adv_sec - 1] - sec_table[i-1]
        if maxi < total:
            maxi = total
            max_sec = i

    return seconds_to_time(max_sec)

play_time = "00:00:10"
adv_time = 	"00:00:05"
logs = ["00:00:08-00:00:10"]

print(solution_numpy(play_time, adv_time, logs))