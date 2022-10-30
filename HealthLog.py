"""
Author: James Roberts
Last Update: 10/30/2022

This program has the class HealthLog that manages
the txt file.
"""


class HealthLog:

    """
    This HealthLog class allows you to:
    Start a New Log
    Record Weight (lbs)
    Record Height (inches)
    Record Age
    Find Basal Metabolic Rate (BMR)
    Find weight on given date
    Find weight lossed thus far
    """


    def __init__(self, log, sex='', age=0, height=0, name='', start_date=''):
        """
        This constructor takes a
        log name
        gender
        age
        height
        name
        """
        self.log = log.upper() + '.txt'
        self.sex = sex.upper()
        self.age = age
        self.height = height
        self.__name = name.upper()
        self.start_date = start_date


    def __repr__(self):
        """
        This Magic Method returns the name of the txt file
        """
        return f'HealthLog: "{self.log}"'


    def __index__(self, date):
        """
        This magic method returns the weight at a given date
        """

        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if date in line:
                weight = int(line.split(': ')[1])


        return (weight)


    def __bmr(self, weight):
        """
        This method calculates the basal metabolic rate
        """
        try:
            lines = []
            output_file = open(self.log, "r")
            for line_str in output_file:
                lines.append(line_str.strip('\n'))
            output_file.close()

        except:
            pass

        for line in lines:
            if 'Age' in line:
                self.age = int(line.split(': ')[1])

            elif 'Height' in line:
                self.height = int(line.split(': ')[1])

            elif 'Sex' in line:
                self.sex = line.split(': ')[1]

        # Calculate BMR
        bmr_male = 66 + (6.2 * weight) + (12.7 * self.height) - (6.8 * self.age)
        bmr_female = 655 + (4.35 * weight) + (4.7 * self.height) - (4.7 * self.age)
        bmr_other = (bmr_female + bmr_male) / 2

        # Return BMR depending on SEX
        if self.sex == 'FEMALE':
            return int(bmr_female)

        elif self.sex == 'MALE':
            return int(bmr_male)

        else:
            # avg bmr between men and women
            return int(bmr_other), self.sex


    def new_log(self, starting_weight):
        """
        This public method creates a new txt file
        to house the HealthLog or overwrite an old one.
        """
        self.starting_weight = starting_weight

        self.weight_dict = {self.start_date: self.starting_weight}

        lines = ['Name: ' + self.__name,
                 'Sex: ' + self.sex,
                 'Current Age (years): ' + str(self.age),
                 'Current Height (inches): ' + str(self.height),
                 '-',
                 'Basal Metabolic Rate (Calories): ' + str(self.__bmr(self.starting_weight)),
                 '-',
                 'START DATE: ' + self.start_date,
                 'Starting Weight (LBS): ' + str(self.starting_weight),
                 'Current Weight (LBS): ' + str(self.starting_weight),
                 'Weight Loss (LBS): ',
                 '-',
                 'Weight (LBS) over time:']

        output_file = open(self.log, "w+")
        for line in range(len(lines)):
            print(lines[line], file=output_file)
        output_file.close()


    def record_weight(self, weight, date):
        """
        This public method records the date and weight of
        person and adds it to the log txt file and updates
        current weight and weight loss in txt file
        """

        self.weight_dict= {date: weight}

        weight = str(weight)

        # Append recorded weight to last line of txt file
        output_file = open(self.log, "a")
        print(date + ': ' + weight, file=output_file)
        output_file.close()



        # Update Current Weight, weight loss, and bmr in txt file
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Current Weight' in line:
                lines[lines.index(line)] = 'Current Weight: ' + weight

            elif 'Starting Weight' in line:
                self.starting_weight = int(line.split(': ')[1])

            elif 'Weight Loss' in line:
                lines[lines.index(line)] = 'Weight Loss: ' + str(self.starting_weight - int(weight))

            elif 'Basal' in line:
                lines[lines.index(line)] = 'Basal Metabolic Rate (Calories): ' \
                                           + str(self.__bmr(int(weight)))

        output_file = open(self.log, "w")
        for line_str in lines:
            print(line_str, file=output_file)
        output_file.close()


    def get_bmr(self):
        """
        This public method allows the user to
        get their basal metabolic at their current weight
        """
        # Find
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Basal' in line:
                bmr = line.split(': ')
                bmr = bmr[1]
                break

        return bmr


    def change_height(self, height):
        """
        This public method allows the user to change their
        height and update the bmr
        """

        self.height = height

        # Find Current Weight
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Current Weight' in line:
                self.weight = int(line.split(': ')[1])



        # Update height and bmr in txt file
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Height' in line:
                lines[lines.index(line)] = 'Current Height (inches): ' + str(self.height)

            elif 'Basal' in line:
                lines[lines.index(line)] = 'Basal Metabolic Rate (Calories): ' \
                                           + str(self.__bmr(int(self.weight)))
        # Update txt file
        output_file = open(self.log, "w")
        for line_str in lines:
            print(line_str, file=output_file)
        output_file.close()


    def change_age(self, age):
        """
        This public method allows the user to change their
        Age and update the bmr
        """
        self.age = age

        # Find Current weight
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Current Weight' in line:
                self.weight = int(line.split(': ')[1])

        # Update age and bmr in txt file
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Age' in line:
                lines[lines.index(line)] = 'Current Age (years): ' + str(self.age)

            elif 'Basal' in line:
                lines[lines.index(line)] = 'Basal Metabolic Rate (Calories): ' \
                                           + str(self.__bmr(int(self.weight)))

        # Update txt file
        output_file = open(self.log, "w")
        for line_str in lines:
            print(line_str, file=output_file)
        output_file.close()


    def get_weight_loss(self):
        """
        This public method retrieves their current
        weight lossed
        """

        # Get weight loss from txt file
        lines = []
        output_file = open(self.log, "r")
        for line_str in output_file:
            lines.append(line_str.strip('\n'))
        output_file.close()

        for line in lines:
            if 'Weight Loss' in line:
                lossed = line.split(': ')
                lossed = lossed[1]
                break

        return lossed






if __name__ == '__main__':
    # Test Code

    # Constants
    LOGNAME = 'Weight_Loss_Log'
    NAME = 'Amy'
    SEX = 'Female'
    AGE = 26
    HEIGHT = 72
    START_DATE = '9/6/2022'
    STARTINGWEIGHT = 400
    DATE = '10/22/2022'
    WEIGHT_NOW = 260

    # Create Instance
    new_log = HealthLog(log=LOGNAME,
                        name=NAME,
                        sex=SEX,
                        age=AGE,
                        height=HEIGHT,
                        start_date=START_DATE)

    # Create New Log
    new_log.new_log(starting_weight=STARTINGWEIGHT)


    # Unit Tests

    # Check get_weightloss is correct
    # Record Weight
    new_log.record_weight(weight=WEIGHT_NOW, date=DATE)
    weight_loss = new_log.get_weight_loss()
    assert new_log.get_weight_loss() == '140', "Weight loss is not correct"
    unittest_1 = True

    # Check Index finds correct weight
    weight = new_log.__index__(DATE)
    assert weight == WEIGHT_NOW, "Weight found is incorrect"
    unittest_2 = True

    # Check get_bmr
    cal = new_log.get_bmr()
    assert cal == '2002', "Incorrect BMR"

    if unittest_1 == unittest_2 == True:
        print('HealthLog unit tests successful!')





