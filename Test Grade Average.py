# 5 Test Average and Grade

#Enter 4 test scores
test1 = int(input('Enter test grade 1: '))
test2 = int(input('Enter test grade 2: '))
test3 = int(input('Enter test grade 3: '))
test4 = int(input('Enter test grade 4: '))

total =(test1 + test2 + test3 + test4 )
#Calculate average
def calc_average(total):
    return total / 4

#Grading levels
def determine_score(grade):
    if 90 >= grade <= 100:
        return 'A'
    elif 80 >= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

grade = total
avg = calc_average(total)
abc_grade = determine_score(grade)

print('Average grade is: ' + str(avg))
print("That's an: " + determine_score(grade))

