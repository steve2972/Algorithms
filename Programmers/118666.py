def solution(survey, choices):
    personality = {k:0 for k in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    for types, choice in zip(survey, choices):
        l, r = types[0], types[1]

        if choice < 4:
            personality[l] += abs(choice - 4)
        elif choice > 4:
            personality[r] += abs(choice - 4)

    
    answer = []
    if personality["R"] >= personality["T"]:
        answer.append("R")
    else:
        answer.append("T")

    if personality["C"] >= personality["F"]:
        answer.append("C")
    else:
        answer.append("F")

    if personality["J"] >= personality["M"]:
        answer.append("J")
    else:
        answer.append("M")

    if personality["A"] >= personality["N"]:
        answer.append("A")
    else:
        answer.append("N")

    
    return ''.join(answer)