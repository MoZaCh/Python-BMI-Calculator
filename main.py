
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
    print("This is a test!")
