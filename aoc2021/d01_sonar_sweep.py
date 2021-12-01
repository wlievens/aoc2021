data_path = 'input/d01_sonar_sweep.txt'
with open(data_path, 'r') as file:
    measurements = list(map(int, file.readlines()))

# Part One
increases = 0
for n in range(len(measurements) - 1):
    m1 = measurements[n]
    m2 = measurements[n + 1]
    if m2 > m1:
        increases = increases + 1
print('increases:', increases)

# Part Two
window = 3
rolling_sums = []
for n in range(len(measurements) - window + 1):
    rolling_sums.append(sum(measurements[n:n + window]))
increases = 0
for n in range(len(rolling_sums) - 1):
    s1 = rolling_sums[n]
    s2 = rolling_sums[n + 1]
    if s2 > s1:
        increases = increases + 1
print('rolling sum increases:', increases)
