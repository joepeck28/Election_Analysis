#What is the score?
score = int(input("What is you test score?"))

#User inputs their score to determine grade

# Determine the grade.
if score >=101:
    print('Your score is off the charts! A+')
elif score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')