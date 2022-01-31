import os
from math import sqrt

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

table = [int(item) for item in open(path).read().split(", ")]

mean = int(sum(table) / len(table))
print(f"Mean: {mean}")

away = [int(abs(mean - item)) for item in table]
print(f"Away from Mean: {away}")

variance = sum([item ** 2 for item in away]) / len(table)
print(f"Variance: {variance:.2f}")

standard_deviation = sqrt(variance)
print(f"Standard Deviation: {standard_deviation:.2f}")