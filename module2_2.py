first = int('112')
second = int('911')
third = int('112')
print(first)
print(second)
print(third)

if first == second and second == third:
    print('3')
elif first == third:
    print('2')
elif first == second:
    print('2')
elif second == third:
    print('2')
else:
    print('0')