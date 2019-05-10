print("Welcome to Negar's BMI calculator !\n :D ")

print("First, Please tell me, will you use SI units?\n Answer with Yes or No ")

answer = input()

print('Please enter your weight:')
weight = float(input())
print('Almost there, now please enter your height:')
height = float(input())

BMI = weight / (height * height)
print(weight, height)


# if answer == 'Yes' or answer == 'yes':
# if answer in ['Yes', 'yes']:
if answer.lower() == 'yes':
    print('and your BMI is: ', BMI)

    if BMI <= 18.5:
        print('Result is : Underweight :(')
    elif 18.5 < BMI <= 25:
        print('Result is : Normal :P Great !')
    elif 25 < BMI < 30:
        print('Result is : Overweight :(')
    else:
        print('Result is : Obesity :,((')

if answer == 'No' or answer == 'no':
    BMI = BMI * 703
    print('and your BMI is: ', BMI)

    if BMI <= 18.5:
        print('Result is : Underweight :(')
    elif 18.5 < BMI <= 25:
        print('Result is : Normal :P Great !')
    elif 25 < BMI < 30:
        print('Result is : Overweight :(')
    else:
        print('Result is : Obesity :,((')