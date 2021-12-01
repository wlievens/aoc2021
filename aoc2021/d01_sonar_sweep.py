data_path = 'input/d01_sonar_sweep.txt'
with open(data_path, 'r') as file:
    measurements = list(map(int, file.readlines()))
increases = 0
for n in range(0, len(measurements) - 1):
    m1 = measurements[n]
    m2 = measurements[n + 1]
    if m2 > m1:
        increases = increases + 1
print('increases:', increases)
