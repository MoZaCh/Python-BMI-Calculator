
def check_weight_function(num):
    """Returns true or false if the given value is a valid number

    Parameter
    ---------
    num : str
        A value that is passed to be validated

    Returns
    -------
    is_num : boolean
        True or False depending on if the value is a valid number
    """

    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    is_num = True

    for i in num:
        if i not in num_list:
            is_num = False
            break
        else:
            is_num = True

    return is_num


def bmi_calculator(height, weight):
    """Returns the BMI result for given inputs weight and height

    Parameters
    ----------
    height : str
        The height of the individual in metres.
    weight : str
        The weight of the individual in KG.

    Returns
    -------
    bmi : int
        The BMI for given inputs weight and height.
    """

    height = float(height)  # Converting string to float
    weight = float(weight)
    bmi = weight / height**2  # Formula to work out BMI
    bmi = int(bmi)
    print(f'Your BMI: {bmi}')
    return bmi


if __name__ == '__main__':
    print(bmi_calculator(1.7, 58))
    print(check_weight_function('58'))
    print(check_weight_function('5R'))
