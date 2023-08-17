import random

def generate_random_pattern():
    digits = list(range(1, 10))
    random.shuffle(digits)
    pattern = ''.join(map(str, digits))
    return pattern

def calculate_sums(pattern):
    sums = []
    for indices in [(0, 1, 3, 4), (1, 2, 4, 5), (3, 4, 6, 7), (4, 5, 7, 8)]:
        sums.append(sum(int(pattern[i]) for i in indices))
    return sums

def calculate_mode01(pattern):
    mode01 = []
    for indices in [(0, 1, 3), (2, 4, 5, 8), (6, 7)]:
        mode01.append(sum(int(pattern[i]) for i in indices))
    return mode01

def calculate_mode02(pattern):
    mode02 = []
    for indices in [(3, 6, 7), (2, 4, 5, 8), (0, 1)]:
        mode02.append(sum(int(pattern[i]) for i in indices))
    return mode02

def calculate_mode03(pattern):
    mode03 = []
    for indices in [(1, 2, 5), (0, 3, 4, 6), (7, 8)]:
        mode03.append(sum(int(pattern[i]) for i in indices))
    return mode03

def calculate_mode04(pattern):
    mode04 = []
    for indices in [(5, 7, 8), (0, 3, 4, 6), (1, 2)]:
        mode04.append(sum(int(pattern[i]) for i in indices))
    return mode04

def calculate_mode05(pattern):
    mode05 = []
    for indices in [(3, 6, 7), (0, 1, 2, 4), (5, 8)]:
        mode05.append(sum(int(pattern[i]) for i in indices))
    return mode05

def calculate_mode06(pattern):
    mode06 = []
    for indices in [(5, 7, 8), (0, 1, 2, 4), (3, 6)]:
        mode06.append(sum(int(pattern[i]) for i in indices))
    return mode06

def calculate_mode07(pattern):
    mode07 = []
    for indices in [(0, 1, 3), (4, 6, 7, 8), (2, 5)]:
        mode07.append(sum(int(pattern[i]) for i in indices))
    return mode07

def calculate_mode08(pattern):
    mode08 = []
    for indices in [(1, 2, 5), (4, 6, 7, 8), (0, 3)]:
        mode08.append(sum(int(pattern[i]) for i in indices))
    return mode08

random_pattern = generate_random_pattern()
print("Random Pattern:", random_pattern)

sums = calculate_sums(random_pattern)
print("Sums:", sums)

mode01 = calculate_mode01(random_pattern)
print("Model#01:", mode01)

mode02 = calculate_mode02(random_pattern)
print("Model#02:", mode02)

mode03 = calculate_mode03(random_pattern)
print("Model#03:", mode03)

mode04 = calculate_mode04(random_pattern)
print("Model#04:", mode04)

mode05 = calculate_mode05(random_pattern)
print("Model#05:", mode05)

mode06 = calculate_mode06(random_pattern)
print("Model#06:", mode06)

mode07 = calculate_mode07(random_pattern)
print("Model#07:", mode07)

mode08 = calculate_mode08(random_pattern)
print("Model#08:", mode08)
