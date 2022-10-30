"""
Author: James Roberts
Last Update: 10/30/2022

This program allows the user to create a
Weight Loss Log or interact with an old one via the console.
"""
import string
import random
from HealthLog import HealthLog



def bmr(sex, age, height, weight):
    """
    This function calculates the bmr given
    weight in LBS
    height in Inches
    sex as MALE, FEMALE or other
    and age in Years

    and returns the BMR in calories
    """
    SEX_DICT = {'MALE': 1, 'FEMALE': 2}

    # Calculate BMR
    bmr_male = 66 + (6.2 * weight) + (12.7 * height) - (6.8 * age)
    bmr_female = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    bmr_other = (bmr_female + bmr_male) / 2

    # Return BMR depending on SEX
    if sex.upper() not in SEX_DICT:
        return int(bmr_other)

    elif SEX_DICT[sex.upper()] == 2:
        return int(bmr_female)

    elif SEX_DICT[sex.upper()] == 1:
        return int(bmr_male)

close = False
i = 0
while close != True:

    # Welcome
    if i == 0:
        print('Welcome to your Weight Loss Log! \n')
        print('What would you like to do?')

        #no input_file
        input_file = None

    elif i != 0:
        print('--------------------------------------------------------------------')
        print('\nIs there anything else you would like to do?\n')

    print('Enter "1" for Create New Log / Overwrite Old One')
    print('Enter "2" to record weight')
    print('Enter "3" to get your bmr')
    print("Enter '4' to calculate a person's bmr")
    print('Enter "5" to change height')
    print('Enter "6" to change age')
    print('Enter "7" to get your current weight lossed')
    print('Enter "8" to get a weight on a certain date')
    print('Enter "s" to close program\n')

    # Get User Input
    valid_input = False
    while valid_input != True:
        user_input = input('Please Enter a number or s to close program: ')

        # Check to see if user input is a number between 1-7 or s
        if user_input not in ['1','2','3','4','5','6','7','8','s','S']:
            print('Please enter only a number or the letter s\n')
        else:
            valid_input = True
            print('--------------------------------------------------------------------')


    # Use User input

    #Check to see if they already have a log if they choose 2,3,5,6,7

    if input_file == None:
        if user_input in ['2','3','5','6','7','8']:
            print('Do you already have a log?\n')

            valid_input = False
            while valid_input != True:
                input_file = input('Please enter the txt file of your log (file.txt): ')
                try:
                    file = open(input_file, 'r')
                    file.close()
                    input_file = input_file.replace('.txt', '')
                    print('\nFile Found!\n')
                    valid_input = True
                except:
                    print('This file does not exist')
                    print('Would you like to try again?')
                    try_again = input('Try again (y/n): ')
                    if try_again == 'y':
                        pass
                    elif try_again == 'n':
                        user_input = '1'
                        valid_input = True

    # Close Program
    if user_input == 's' or user_input == 'S':
        close = True
        closing = ['Adios!', 'See ya Later!', 'PEACE!', 'Come back soon!', 'See you tomorrow!']
        choice = random.choice(closing)
        print(choice)

    # Create User Log
    elif user_input == '1':
        print('Creating New Log...\n')

        # Get log name
        valid_input = False
        while valid_input != True:
            log_name = input('\nPlease Enter a name for you log (letters and underscores): ')

            # Check to see if log_name is valid
            for char in log_name:
                if char in string.punctuation and char != '_':
                    print('Please enter with only underscores')
            else:
                valid_input = True
                print('perfect!')

        # Get user name
        user_name = input('\nPlease Enter your name: ')
        print('perfect!')

        # Get user sex
        user_sex = input(('\nPlease Enter your sex (Male, Female, Other): '))
        print('perfect!')

        # Get user age
        valid_input = False
        while valid_input != True:
            try:
                user_age = int(input(('\nPlease Enter your age (integer or float): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        # Get user Height
        valid_input = False
        while valid_input != True:
            try:
                user_height = int(input(('\nPlease Enter your height (inches): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        start_date = input("\nplease enter your start date (MM/DD/YYYY): ")
        print('perfect!')

        # Get user starting weight
        valid_input = False
        while valid_input != True:
            try:
                start_weight = int(input(('\nPlease Enter your starting weight (LBS): ')))
                valid_input = True
                print('perfect!\n')
            except:
                print('\nPlease only Enter a number or integer')

        # Create Instance
        user_log = HealthLog(log=log_name,
                             name=user_name,
                             sex=user_sex,
                             age=user_age,
                             height=user_height,
                             start_date=start_date)

        # Create New Log
        user_log.new_log(starting_weight=start_weight)

        print('Log Succesfully Created')
        print(user_log)
        print()

    # Record Weight
    elif user_input == '2':
        print('Record Weight: ')

        # Get date for weight
        user_date = input("\nplease enter your start date (MM/DD/YYYY): ")
        print('perfect!')

        # Get user weight
        valid_input = False
        while valid_input != True:
            try:
                user_weight = int(input(('\nPlease Enter your weight (LBS): ')))
                valid_input = True
                print('perfect!\n')
            except:
                print('\nPlease only Enter a number or integer')

        user_log = HealthLog(log=input_file)

        user_log.record_weight(weight=user_weight, date=user_date)
        print('Weight recorded Successfully')

    # Get user bmr
    elif user_input == '3':
        print('Get BMR: ')

        print('\nYour current Basal Metabolic Rate: ')
        user_log = HealthLog(log=input_file)
        print(str(user_log.get_bmr()) + ' Calories per Day')

    # Calculate anyones bmr
    elif user_input == '4':
        print('Calculating BMR: ')

        # Get sex
        user_sex = input(('\nPlease Enter sex (Male, Female, Other): '))
        print('perfect!')

        # Get age
        valid_input = False
        while valid_input != True:
            try:
                user_age = int(input(('\nPlease Enter age (integer or float): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        # Get Height
        valid_input = False
        while valid_input != True:
            try:
                user_height = int(input(('\nPlease Enter height (inches): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        # Get user current weight
        valid_input = False
        while valid_input != True:
            try:
                user_weight = int(input(('\nPlease Enter weight (LBS): ')))
                valid_input = True
                print('perfect!\n')
            except:
                print('Please only Enter a number or integer')

        Cal = bmr(user_sex, user_age, user_height, user_weight)

        print('BMR for a {:} year old {:} with a height of {:} inches, and weighs {:} LBS: \n{:,} Calories'.format(
            user_age,
            user_sex,
            user_height,
            user_weight,
            Cal
            ))

    # Change height in log
    elif user_input == '5':
        print('Changing height in log...')

        # Get Height
        valid_input = False
        while valid_input != True:
            try:
                user_height = int(input(('\nPlease Enter height (inches): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        user_log = HealthLog(log=input_file)

        user_log.change_height(height=user_height)
        print('Height Changed Successfully')

    # Change age in log
    elif user_input == '6':
        print('Changing age in log...')
        # Get age
        valid_input = False
        while valid_input != True:
            try:
                user_age = int(input(('\nPlease Enter age (integer or float): ')))
                valid_input = True
                print('perfect!')
            except:
                print('Please only Enter a number or integer')

        user_log = HealthLog(log=input_file)
        user_log.change_age(age=user_age)
        print('Age Changed Successfully')

    # Get weight lossed
    elif user_input == '7':
        print('Weight lossed:')
        try:
            user_log = HealthLog(log=input_file)
            lossed = user_log.get_weight_loss()
            print('\nYou have lossed: ' + lossed + 'LBS')
        except:
            print('You have not recorded any weight change')

    # Get weight on certain date
    elif user_input == '8':
        print('Weight on a certain date: ')

        try:
            date = input('\nPlease enter date (mm/dd/yyyy): ')

            user_log = HealthLog(log=input_file)
            weight = user_log.__index__(date)

            print('\nDate found!\n')

            print('Weight on {:}: {:} LBS'.format(date, str(weight)))

        except:
            print('\nNo weight at that date')


    i+=1
