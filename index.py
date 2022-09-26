number_of_people = 20
number_of_seats = 10
number_of_trips = 0

if number_of_people > number_of_seats:
    number_of_trips = number_of_people / number_of_seats

#print(number_of_trips)

number_of_fat_people = 4
if number_of_fat_people > 0 and number_of_people > 10:
    number_of_seats -= number_of_fat_people
    print(number_of_seats)