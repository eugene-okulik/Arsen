temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hot_days = (list(filter(lambda temp: temp > 28, temperatures)))
hot_day = []
cold_day = []
days = []
for temp in hot_days:
    if temp >= 32:
        hot_day.append(temp)
    elif temp <= 31 and temp >= 30:
        days.append(temp)
    else:
        cold_day.append(temp)

print(hot_day)
print(cold_day)
print(days)
