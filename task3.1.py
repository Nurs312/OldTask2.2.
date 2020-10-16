hour1 = int(input('Enter first hour: '))
min1 = int(input('Enter first min: '))
sec1 = int(input('Enter first sec: '))
time1 = (hour1 * 3600) + (min1 * 60) + sec1
hour2 = int(input('Enter second hour: '))
min2 = int(input('Enter second min: '))
sec2 = int(input('Enter second sec: '))
time2 = (hour2 * 3600) + (min2 * 60) + sec2
difference = time1 - time2
print(f'Difference is equal to: {abs(difference)} seconds')