def solution(tickets):
    graph, travel_len = {}, len(tickets)+1
    for departure, destination in tickets:
        if departure in graph:
            graph[departure].append(destination)
        else: graph[departure] = [destination]

    answers = []
    def dfs(itinerary, tickets):
        dep = itinerary[-1]
        if len(itinerary) == travel_len:
            answers.append(itinerary)
            return
        if dep in tickets:
            for dest in sorted(tickets[dep]):
                tck = {k:v[:] for k,v in tickets.items()}
                it = itinerary[:]
                it.append(dest)
                tck[dep].remove(dest)
                dfs(it, tck)

    dfs(["ICN"], graph)
    return answers

tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
print(solution(tickets))