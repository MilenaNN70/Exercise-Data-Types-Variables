from math import ceil

number_of_peoples = int(input())
capacity = int(input())

current_courses = ceil(number_of_peoples / capacity)
print(current_courses)
