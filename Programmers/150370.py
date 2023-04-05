def solution(today, terms, privacies):
    today = [*map(int, today.split('.'))]
    calc = lambda x: x[0] * 12 * 28 + x[1]*28 + x[2]
    today = calc(today)

    term_dict = {k:int(v)*28 for k,v in map(lambda x: x.split(), terms)}

    answer = []
    for idx, privacy in enumerate(privacies):
        date, ptype = privacy.split()
        date = [*map(int, date.split('.'))]
        date = calc(date)
        if date + term_dict[ptype] <= today:
            answer.append(idx+1)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))