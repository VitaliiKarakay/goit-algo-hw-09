import heapq
import time
import tracemalloc


def measure_performance(func, *args):
    tracemalloc.start()

    start_time = time.time()
    result = func(*args)
    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Результат: {result}")
    print(f"Час виконання: {end_time - start_time:.6f} секунд")
    print(f"Використання пам'яті: {current / 1024:.2f} KB; Пікове: {peak / 1024:.2f} KB\n")


def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113

print("Жадібний алгоритм:")
measure_performance(find_coins_greedy, amount)

print("Алгоритм динамічного програмування:")
measure_performance(find_min_coins, amount)
