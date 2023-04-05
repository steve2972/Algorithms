import itertools

def solution(users, emoticons):
    sales = range(10, 50, 10)
    combinations = []
    for i in itertools.product(sales, repeat=len(emoticons)):
        combinations.append(list(zip(emoticons, i)))

    answer = [0,0]
    for combination in combinations:
        profit = 0
        subscription = 0
        for user in users:
            u_profit = 0
            u_sale, u_money = user
            for price, discount in combination:
                price = int(price * (100 - discount)/100)
                if discount >= u_sale:
                    if price < u_money:
                        u_profit += price
                        u_money -= price
                    else:
                        u_profit = 0
                        subscription += 1
                        break
            profit += u_profit
        answer = max(answer, [subscription, profit])
    
    return answer
                



users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))
