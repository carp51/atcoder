def nearest_water_station(N):
    quotient, remainder = divmod(N, 5)
    if remainder < 2.5:
        return quotient * 5
    else:
        return (quotient + 1) * 5

N = int(input().strip())
print(nearest_water_station(N))
