import math

def std_dev(population):
    mean = sum(population) / len(population)
    sum_pop_mean_sq = 0
    for item in range(len(population)):
        sum_pop_mean_sq += (population[item] - mean) ** 2
    return math.sqrt(sum_pop_mean_sq / len(population))
